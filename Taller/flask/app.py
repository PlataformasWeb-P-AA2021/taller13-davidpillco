from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Administración Edificios</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
            auth=('david', 'david'))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)




@app.route("/losdepartamentos")
def los_departamentos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=('david', 'david'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nomPropietario':d['nomPropietario'], 'costo':d['costo'], 'num_cuartos':d['num_cuartos'], 'edificio':d['edificio'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('david', 'david'))
    edificio = json.loads(r.content)['nombre'] + " - " + json.loads(r.content)['direccion'] + " - " + json.loads(r.content)['ciudad'] + " - " + json.loads(r.content)['tipo_edificio']
    return edificio

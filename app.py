from flask import Flask, render_template, request, jsonify
import urllib.request
import json
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Configura tu API key y endpoint
load_dotenv()
API_KEY = os.getenv('API_KEY')
ENDPOINT = os.getenv('ENDPOINT')

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Recoge los datos del formulario
        form = request.form
        input_values = [
            form['marca'],
            form['modelo'],
            form['version'],
            int(form['startYear']),
            int(form['endYear']),
            int(form['cilindrada']),
            int(form['cv']),
            form['id_carroceria'],
            int(form['pf']),
            int(form['puertas']),
            form['id_combustible'],
            int(form['matriculacion']),
            form['periodoDescripcion'],
            int(form['Anno']),
        ]

        # Insertar null como precio_compra si lo necesitas (en el índice 11)
        # input_values.insert(11, None)  # Solo si tu modelo lo espera

        payload = {
            "input_data": {
                "columns": [
                    "marca", "modelo", "version", "startYear", "endYear", "cilindrada", "cv",
                    "id_carroceria", "pf", "puertas", "id_combustible", "matriculacion",
                    "periodoDescripcion", "Anno"
                ],
                "index": [0],
                "data": [input_values]
            }
        }

        # Preparar la solicitud
        body = str.encode(json.dumps(payload))
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {API_KEY}'
        }
        req = urllib.request.Request(ENDPOINT, body, headers)

        try:
            response = urllib.request.urlopen(req)
            result = json.loads(response.read())
            price = "${:,.2f}".format(result[0])
            return render_template('index.html', resultado=price)
        except urllib.error.HTTPError as error:
            error_msg = f"Error {error.code}: {error.read().decode()}"
            return render_template('index.html', error=error_msg)

    return render_template('index.html')

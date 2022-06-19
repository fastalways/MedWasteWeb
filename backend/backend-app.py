import os
from time import time
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/')
def show_index():
    str =  """<!DOCTYPE html>
<html>
<head>
<title>MedWaste-Prediction-BACKEND-API</title>
</head>
<body>

<h1>Welcome to MedWaste-Prediction-BACKEND-API</h1>
<p>This is MedWaste-Prediction-BACKEND-API</p>

</body>
</html>"""
    return str
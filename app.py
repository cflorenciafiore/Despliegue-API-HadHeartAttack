from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "mensaje": "API de prediccion de ataque cardiaco",
        "endpoint": "/predict",
        "metodo": "POST"
    }

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    try:
        result = predict(data)
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

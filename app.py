from flask import Flask, request, jsonify
from model import predict

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "mensaje": "API de predicción de ataque cardiaco",
        "descripcion": "Recibe datos de salud y devuelve una predicción usando un modelo ML",
        "uso_GET": "/predict?Sex=Male&AgeCategory=Age 60-64&GeneralHealth=Good&SleepHours=7&WeightInKilograms=80",
        "uso_POST": "Enviar JSON al endpoint /predict"
    }


@app.route("/predict", methods=["GET", "POST"])
def predict_endpoint():

    # GET: parámetros en URL
    if request.method == "GET":
        data = request.args.to_dict()
    else:
        # POST: JSON
        data = request.get_json(silent=True)

    # Datos por defecto si no se envían
    if not data:
        data = {
            "Sex": "Male",
            "AgeCategory": "Age 60-64",
            "GeneralHealth": "Good",
            "PhysicalHealthDays": 0,
            "MentalHealthDays": 0,
            "LastCheckupTime": "Within past year",
            "PhysicalActivities": "Yes",
            "SleepHours": 7,
            "RemovedTeeth": "None",
            "HadAngina": "No",
            "HadStroke": "No",
            "HadCOPD": "No",
            "HadDiabetes": "No",
            "HadKidneyDisease": "No",
            "HadArthritis": "No",
            "HadSkinCancer": "No",
            "AlcoholDrinkers": "Yes",
            "SmokerStatus": "Never smoked",
            "DifficultyWalking": "No",
            "DifficultyDressingBathing": "No",
            "DifficultyErrands": "No",
            "DeafOrHardOfHearing": "No",
            "BlindOrVisionDifficulty": "No",
            "DifficultyConcentrating": "No",
            "WeightInKilograms": 80,
            "CovidPos": "No",
            "ChestScan": "No",
            "PneumoVaxEver": "Yes",
            "State": "California"
        }

    # Convertir numéricos (IMPORTANTE para GET)
    numeric_fields = [
        "PhysicalHealthDays",
        "MentalHealthDays",
        "SleepHours",
        "WeightInKilograms"
    ]

    for field in numeric_fields:
        if field in data:
            try:
                data[field] = float(data[field])
            except:
                pass

    try:
        result = predict(data)

        return jsonify({
            "input": data,
            "prediction": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "type": type(e).__name__
        }), 500


# Solo para local
if __name__ == "__main__":
    app.run(debug=True)

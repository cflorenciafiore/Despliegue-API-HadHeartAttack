import joblib
import pandas as pd
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "heart_attack_model.pkl")

model = None

columns = [
    "State","Sex","GeneralHealth","PhysicalHealthDays","MentalHealthDays",
    "LastCheckupTime","PhysicalActivities","SleepHours","RemovedTeeth",
    "HadAngina","HadStroke","HadCOPD","HadDiabetes","HadKidneyDisease",
    "HadArthritis","HadSkinCancer","AlcoholDrinkers","SmokerStatus",
    "DifficultyWalking","DifficultyDressingBathing","DifficultyErrands",
    "DeafOrHardOfHearing","BlindOrVisionDifficulty","DifficultyConcentrating",
    "AgeCategory","WeightInKilograms","CovidPos","ChestScan","PneumoVaxEver"
]

defaults = {
    "State": "California",
    "Sex": "Male",
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
    "AgeCategory": "Age 60-64",
    "WeightInKilograms": 80,
    "CovidPos": "No",
    "ChestScan": "No",
    "PneumoVaxEver": "Yes"
}

def predict(features: dict):
    global model

    if model is None:
        model = joblib.load(model_path)

    # Rellenar campos faltantes con defaults
    complete_features = {**defaults, **features}

    df = pd.DataFrame([complete_features])
    df = df[columns]

    prediction = model.predict(df)

    return int(prediction[0])
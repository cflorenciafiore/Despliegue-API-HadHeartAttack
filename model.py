import joblib
import pandas as pd
import os

MODEL_PATH = "heart_attack_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"No se encontró el modelo en {MODEL_PATH}")

try:
    model = joblib.load(MODEL_PATH)
    print("Modelo cargado correctamente")
except Exception as e:
    raise RuntimeError(f"Error cargando el modelo: {e}")

columns = [
    "State","Sex","GeneralHealth","PhysicalHealthDays","MentalHealthDays",
    "LastCheckupTime","PhysicalActivities","SleepHours","RemovedTeeth",
    "HadAngina","HadStroke","HadCOPD","HadDiabetes","HadKidneyDisease",
    "HadArthritis","HadSkinCancer","AlcoholDrinkers","SmokerStatus",
    "DifficultyWalking","DifficultyDressingBathing","DifficultyErrands",
    "DeafOrHardOfHearing","BlindOrVisionDifficulty","DifficultyConcentrating",
    "AgeCategory","WeightInKilograms","CovidPos","ChestScan","PneumoVaxEver"
]

def predict(features: dict):
    df = pd.DataFrame([features])
    df = df.reindex(columns=columns)
    prediction = model.predict(df)
    return int(prediction[0])

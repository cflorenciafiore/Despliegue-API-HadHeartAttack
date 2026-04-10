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

def predict(features: dict):
    global model

    if model is None:
        model = joblib.load(model_path)

    df = pd.DataFrame([features])
    df = df[columns]

    prediction = model.predict(df)

    return int(prediction[0])

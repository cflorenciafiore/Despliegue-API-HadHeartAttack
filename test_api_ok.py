import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "Sex": "Male",
    "AgeCategory": "Age 60-64",
    "GeneralHealth": "Good"
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

print(f"Status: {response.status_code}") 
print(f"Respuesta: {response.json()}")
import requests

url = "http://127.0.0.1:5000/predict"

# Caso 1: vacío
response = requests.post(url, json={})
print("Vacío:", response.json())

# Caso 2: tipo incorrecto
response = requests.post(url, json={"Sex": 123})
print("Tipo incorrecto:", response.json())

print("Vacío:", response.status_code, response.json())
print("Tipo incorrecto:", response.status_code, response.json())
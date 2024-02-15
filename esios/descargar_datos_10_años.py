import requests
import os
import json

# URL base de la API
base_url = "https://api.esios.ree.es/archives"

# Clave de API
api_key = "6b0463ce7476aa84e1c86a550d56572733ab7fbd421c3c700d270a3269cc2c6b"

# Crear la carpeta media si no existe
if not os.path.exists('media'):
    os.makedirs('media')

# Iterar sobre los últimos diez años
for year in range(2014, 2025):
    # Parámetros de la solicitud
    params = {
        "date": f"{year}-12-31T23:59:59+00:00"
    }

    # Encabezados de la solicitud
    headers = {
        "Accept": "application/json; application/vnd.esios-api-v1+json",
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    # Realizar la solicitud GET a la API
    response = requests.get(base_url, headers=headers, params=params)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Convertir la respuesta a formato JSON
        data = response.json()

        # Guardar los datos en un archivo en la carpeta media
        with open(f'media/data_{year}.json', 'w') as f:
            json.dump(data.get("archives", []), f)
    else:
        print(f"Error al obtener los datos para el año {year}")

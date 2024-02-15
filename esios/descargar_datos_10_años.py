'''import requests

# URL base de la API
base_url = "https://api.esios.ree.es/archives"

# Clave de API
api_key = "6b0463ce7476aa84e1c86a550d56572733ab7fbd421c3c700d270a3269cc2c6b"

# Lista para almacenar los datos de los archivos
all_archives = []

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
        # Convertir la respuesta a formato JSON y agregarla a la lista
        data = response.json()
        all_archives.extend(data.get("archives", []))
    else:
        print(f"Error al obtener los datos para el año {year}")

# Procesar los datos de los archivos obtenidos según sea necesario
for archive in all_archives:
    # Procesar cada archivo aquí
    print(archive)  # Por ejemplo, imprimir los detalles del archivo
'''

# 1. Sin dependencias externas
import urllib.request
import json

# api jsonplaceholder post
api_post = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_post)
    data = response.read()

    json_data = json.loads(data.decode("utf-8"))
    # print(json_data)

    response.close()
except urllib.error.URLError as e:
    print("Error: ", e)


# 2. Usando la dependencia requests
import requests

api_post = "https://jsonplaceholder.typicode.com/posts"

# Get
try:
    response = requests.get(api_post)
    data = response.json()

    # print(data[0])
except requests.exceptions.RequestException as e:
    print("Error: ", e)


# Post
try:
    post_input = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(api_post, json=post_input)
    data = response.json()

    # print(data)
except requests.exceptions.RequestException as e:
    print("Error: ", e)


# Put
try:
    put_input = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.put(api_post, json=put_input)
    data = response.json()

    # print(data)
except requests.exceptions.RequestException as e:
    print("Error: ", e)


# 3. Consumir la api de Deepseek
import os
import requests
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Get API key
api_key = os.getenv("DEEPSEEK_APIKEY")

# API endpoint corregido
api_url = "https://api.deepseek.com/v1/chat/completions"  # Dominio y ruta correctos

# Headers actualizados
headers = {
    "Authorization": f"Bearer {api_key}",  # Formato correcto de autenticación
    "Content-Type": "application/json"
}

# Payload requerido
payload = {
    "model": "deepseek-chat",  # Modelo válido
    "messages": [
        {"role": "user", "content": "Hola, ¿cómo estás?"}  # Mensaje de ejemplo
    ]
}

try:
    # Hacer la solicitud POST
    response = requests.post(
        api_url, 
        headers=headers, 
        json=payload
    )
    
    response.raise_for_status()  # Verificar errores HTTP
    data = response.json()
    print("API Response:", data)

except Exception as e:
    if hasattr(e, 'response') and e.response is not None:
        print(f"Status Code: {e.response.status_code}")
        print(f"Error Details: {e.response.text}")
    else:
        print(f"Error: {e}")
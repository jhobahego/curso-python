# 1. Introducción a clases
# Una clase es un modelo que define el comportamiento de los objetos.
# Un objeto es una instancia de una clase.

class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def acelerar(self):
        print(f"El coche de la marca {self.marca} y modelo {self.modelo} aceleró")

    def frenar(self):
        print(f"El coche de la marca {self.marca} y modelo {self.modelo} frenó")


# my_car = Coche("Ford", "Mustang", "Rojo")
# my_car.acelerar()
# my_car.frenar()

# hiunday_car = Coche("Hyundai", "i30", "Azul")
# hiunday_car.acelerar()
# hiunday_car.frenar()


# 2. Crear una clase para llamar a una AI, sea OpenAI, Deepseek o la que se desee...
import requests
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class AI:
    def __init__(self, api_key, url, model):
        self.model = model
        self.api_key = api_key
        self.url = url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def ask(self, prompt):
        try:
            response = requests.post(
                self.url,
                headers=self.headers,
                json={
                    "model": self.model,  
                    "messages": [{"role": "user", "content": prompt}]
                }
            )
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            if hasattr(e, 'response') and e.response is not None:
                print(f"Error: {e.response.status_code} - {e.response.text}")
            else:
                print(f"Error: {e}")
            return None


url = "https://api.deepseek.com/v1/chat/completions"
model = "deepseek-chat"
api_key = os.getenv("DEEPSEEK_APIKEY")
my_ai = AI(api_key, url, model)
my_ai.ask("Escribeme un poema sobre programación en lenguaje español")

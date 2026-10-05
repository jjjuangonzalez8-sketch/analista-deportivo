import os
import requests
from datetime import datetime

TOKEN = os.environ["TELEGRAM_TOKEN"]

def enviar_mensaje(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

def obtener_partidos_nhl():
    fecha = datetime.now().strftime("%Y-%m-%d")
    url = f"https://api-web.nhle.com/v1/schedule/{fecha}"

    respuesta = requests.get(url, timeout=20)
    respuesta.raise_for_status()

    return respuesta.json()

print("Analista Deportivo - NHL")
partidos = obtener_partidos_nhl()

print("Datos NHL recibidos correctamente.")
print(f"Fecha consultada: {datetime.now().strftime('%Y-%m-%d')}")

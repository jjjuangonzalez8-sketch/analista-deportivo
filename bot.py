import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

def enviar_mensaje(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

print("Analista Deportivo conectado")

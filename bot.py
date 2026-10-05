import os
import requests

TOKEN = os.environ["TELEGRAM_TOKEN"]

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
respuesta = requests.get(url, timeout=20)
datos = respuesta.json()

for actualizacion in datos.get("result", []):
    mensaje = actualizacion.get("message", {})
    chat_id = mensaje.get("chat", {}).get("id")
    texto = mensaje.get("text", "")

    if chat_id and texto == "/start":
        enviar = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(enviar, json={
            "chat_id": chat_id,
            "text": "🏒 Analista Deportivo\n\n✅ ¡Bot conectado correctamente!\n\nYa puedo recibir tus comandos."
        })

print("Bot ejecutado correctamente.")

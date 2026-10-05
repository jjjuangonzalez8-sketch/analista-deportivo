import os
import requests
import time

TOKEN = os.environ["TELEGRAM_TOKEN"]

def enviar_mensaje(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": chat_id,
        "text": texto
    })

def obtener_actualizaciones(offset=None):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    respuesta = requests.get(url, params={"offset": offset}, timeout=30)
    return respuesta.json()

print("Analista Deportivo conectado")

offset = None

while True:
    datos = obtener_actualizaciones(offset)

    for actualizacion in datos.get("result", []):
        offset = actualizacion["update_id"] + 1

        mensaje = actualizacion.get("message", {})
        chat_id = mensaje.get("chat", {}).get("id")
        texto = mensaje.get("text", "")

        if texto == "/start":
            enviar_mensaje(
                chat_id,
                "🏒 Analista Deportivo\n\n"
                "Bot conectado correctamente.\n\n"
                "Escribe /ayuda para ver los comandos."
            )

        elif texto == "/ayuda":
            enviar_mensaje(
                chat_id,
                "📊 Comandos disponibles:\n\n"
                "/start - Iniciar el bot\n"
                "/ayuda - Ver ayuda\n"
                "/analizar - Analizar partidos"
            )

        elif texto == "/analizar":
            enviar_mensaje(
                chat_id,
                "🔎 Estoy preparando el análisis deportivo.\n"
                "Próximamente recibirás los partidos con datos verificables."
            )

    time.sleep(2)

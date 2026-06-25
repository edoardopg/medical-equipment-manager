import requests
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_incident_notification(equipment_name, type_error, description):
    """Envía notificación a Telegram cuando se crea una incidencia"""
    
    message = f"""
🚨 *Nueva Incidencia Creada*

📋 Equipo: {equipment_name}
⚠️ Tipo de error: {type_error}
📝 Descripción: {description}
    """
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    
    try:
        response = requests.post(url, json=data)
        if response.ok:
            print("✅ Notificación enviada a Telegram")
            return True
        else:
            print(f"❌ Error Telegram: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error enviando a Telegram: {e}")
        return False
import pywhatkit as kit
from datetime import datetime, timedelta

# Função para enviar mensagem
def send_whatsapp_message(phone_no, message):
    now = datetime.now() + timedelta(minutes=2)  # Enviar a mensagem dois minutos a partir de agora
    hour = now.hour
    minute = now.minute
    kit.sendwhatmsg(phone_no, message, hour, minute)

# Lista de contatos e mensagens
contacts = {
    "pessoa1": "+55 91 xxxx-xxxx",
    "pessoa2": "+55 91 xxxx-xxxx"
}

message = "Olá! Esta é uma mensagem automática do bot de WhatsApp."

# Enviar mensagem para cada contato
for name, phone_no in contacts.items():
    try:
        send_whatsapp_message(phone_no, message)
        print(f"Mensagem enviada para {name} ({phone_no})")
    except Exception as e:
        print(f"Falha ao enviar mensagem para {name} ({phone_no}): {e}")

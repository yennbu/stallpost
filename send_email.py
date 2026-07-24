import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# 1. DINA INSTÄLLNINGAR
MY_EMAIL = os.environ["GMAIL_USER"]
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"].replace(" ", "")
if len(APP_PASSWORD) != 16:
    raise ValueError(
        f"Fel APP-lösenord."
    )
SMTP_SERVER = "smtp.gmail.com"          # Använd smtp.office365.com för Outlook/Hotmail
SMTP_PORT = 587                            # Standard för säker SSL-anslutning

# 2. MOTTAGARE OCH MEDDELANDE
receiver = os.environ["RECIPIENT_EMAIL"]
# last_farrier_visit = input("När var hovslagaren ute senast? (ÅÅÅÅ-MM-DD): ")

msg = EmailMessage()
msg['Subject'] = 'Boka hovis: Hästarna vill ha pedikyr!'
msg['From'] = f'Hästarna <{MY_EMAIL}>'
msg['To'] = receiver

# Skriv ditt meddelande här
msg.set_content(f'''Hej!

Det här är en automatisk påminnelse från vår stallmail. 

Det är dags att boka hovis för hästarna. 
                
Hälsningar,
Elsa, Indra, Simbi & Bibbi''')

# 3. SKICKA MEJLET
try:
    # Skapa ett SSL-context med säkra standardinställningar
    context = ssl.create_default_context()

    # Använd SMTP_SSL istället för SMTP
    with smtplib.SMTP_SSL(SMTP_SERVER, 465, context=context) as smtp:
        smtp.login(MY_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
    print("Stallmejlet skickades utan problem!")
except Exception as e:
    print(f"Något gick fel: {e}")
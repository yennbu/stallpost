import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# 1. DINA INSTÄLLNINGAR
MY_EMAIL = os.environ["MY_EMAIL"]
APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"].replace(" ", "")
if len(APP_PASSWORD) != 16:
    raise ValueError(
        f"Fel APP-lösenord."
    )
SMTP_SERVER = "smtp.gmail.com"          # Använd smtp.office365.com för Outlook/Hotmail
SMTP_PORT = 587                            # Standard för säker SSL-anslutning

# 2. MOTTAGARE OCH MEDDELANDE
receiver = os.environ["RECEIVER_EMAIL"]
last_farrier_visit = input("När var hovslagaren ute senast? (ÅÅÅÅ-MM-DD): ")

msg = EmailMessage()
msg['Subject'] = 'Hästarna vill ha pedikyr, dags att boka hovis!'
msg['From'] = f'Hästarna <{MY_EMAIL}>'
msg['To'] = receiver

# Skriv ditt meddelande här
msg.set_content(f'''Hej stallgänget!

Det här är en automatisk påminnelse från vårt stallskript. 

Det är dags att boka hovis för hästarna. 
Hovslagaren var ute senast den {last_farrier_visit}.
                
Hälsningar,
Elsa, Indra, Simbi & Bibbi''')

# 3. SKICKA MEJLET
try:
    # Vi använder vanliga SMTP istället för SMTP_SSL för port 587
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.ehlo()          # Identifiera dig mot servern
        smtp.starttls()      # Kryptera anslutningen säkert
        smtp.ehlo()
        smtp.login(MY_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
    print("Stallmejlet skickades utan problem!")
except Exception as e:
    print(f"Något gick fel: {e}")
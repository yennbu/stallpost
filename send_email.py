import os
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
from datetime import datetime

load_dotenv() # Ladda miljövariabler från .env-filen för att hålla känslig information som e-post och lösenord utanför koden.

# INSTÄLLNINGAR
MY_EMAIL = os.getenv("GMAIL_USER")
APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD").replace(" ", "")
if len(APP_PASSWORD) != 16:
    raise ValueError(
        f"Fel APP-lösenord."
    )
SMTP_SERVER = "smtp.gmail.com"          # Använd smtp.office365.com för Outlook/Hotmail
SMTP_PORT = 465                            # " 465 [...] is the standard port for SMTP over SSL."

# MOTTAGARE OCH MEDDELANDE
receiver = os.getenv("RECIPIENT_EMAIL")
# last_farrier_visit = input("När var hovslagaren ute senast? (ÅÅÅÅ-MM-DD): ")

# Bestäm vilka månader de årliga mailen ska skickas
ANNUAL_EMAIL_VACCINE_MONTH = 5    # Maj
ANNUAL_EMAIL_DENTIST_MONTH = 7    # Juli

today = datetime.now()

# STEG 1: Bestäm vilka mail som ska skickas
send_vaccine_email = today.month == ANNUAL_EMAIL_VACCINE_MONTH
send_dentist_email = today.month == ANNUAL_EMAIL_DENTIST_MONTH
send_farrier_email = True

# STEG 2: Bygg lista över mail som ska skickas
emails_to_send = []

if send_vaccine_email:
    emails_to_send.append({
        'subject': 'Vaccination: Påminnelse från hästarna',
        'content': 'Hej! \n\nDet här är en automatisk påminnelse från våra hästar. \n\nDet är dags att kolla upp hästarnas vaccinationer. \n\nHälsningar,\nElsa, Indra, Simbi och Bibbi'
    })

if send_dentist_email:
    emails_to_send.append({
        'subject': 'Tandvård: Påminnelse från hästarna',
        'content': 'Hej!\n\nDet här är en automatisk påminnelse från vår stallmejl. \n\nDet är dags att boka tid för hästarnas tandvård.\n\nHälsningar,\nElsa, Indra, Simbi och Bibbi'
    })

if send_farrier_email:
    emails_to_send.append({
        'subject': 'Boka hovis: Hästarna vill ha pedikyr!',
        'content': 'Hej!\n\nDet här är en automatisk påminnelse från vår stallmejl. \n\nDet är dags att boka hovis för hästarna.\n\nHälsningar,\nElsa, Indra, Simbi och Bibbi'
    })

# STEG 3: Skicka alla mail som ska skickas
try:
    # Skapa ett SSL-context med säkra standardinställningar
    context = ssl.create_default_context()

    # Använd SMTP_SSL istället för SMTP
    with smtplib.SMTP_SSL(SMTP_SERVER, 465, context=context) as smtp:
        smtp.login(MY_EMAIL, APP_PASSWORD)
        
        for email in emails_to_send:
            msg = EmailMessage()
            msg['Subject'] = email['subject']
            msg['From'] = f'Hästarna <{MY_EMAIL}>'
            msg['To'] = receiver
            msg.set_content(email['content'])
            smtp.send_message(msg)
            print(f"{email['subject']} skickat")

except Exception as e:
    print(f"Något gick fel: {e}")
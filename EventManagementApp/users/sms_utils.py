from twilio.rest import Client
import os

# Optionally, load from environment variables
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1XXXXXXXXXX'  # Your Twilio number

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to, message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )

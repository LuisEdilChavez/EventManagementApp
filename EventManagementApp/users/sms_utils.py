from twilio.rest import Client
import os

# Optionally, load from environment variables
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+1XXXXXXXXXX'  # The number registered with a users account gets stored and the twilio library handles the SMS stuff.

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # SMS function itself
def send_sms(to, message):
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
import os
from twilio.rest import Client
account_sid = "ACaf83636b47eed191dabfa7f7dde52d05"
auth_token = "5d9c5a3a7d9aab953f6ac92d4a40cb96"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+2250769217459',
                     to='+2250545842131'
                 )

print(message.sid)
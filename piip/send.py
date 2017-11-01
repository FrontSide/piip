#!/usr/bin/env python3
from twilio.rest import Client

def send(twilio_id, twilio_secret, target_phone, source_phone, ips):
    if len(ips) > 1:
        message = "Your RPi's IPs are %s" % ", ".join(ips)
    else:
        message = "Your RPi's IP is %s" % ips[0]

    client = Client(twilio_id, twilio_secret)
    message = client.messages.create(
        target_phone,
        body=message,
        from_=source_phone)

    print(message.sid)

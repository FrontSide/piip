#!/usr/bin/env python3
from twilio.rest import Client
import getip

account_sid = ""
auth_token = ""
target_number = ""
source_number = ""

ips = getip.get_ips()
if len(ips) > 1:
    message = "Your RPi's IPs are %s" % ", ".join(ips)
else:
    message = "Your RPi's IP is %s" % ips[0]

client = Client(account_sid, auth_token)
message = client.messages.create(
         target_number,
         body=message,
	 from_=source_number)

print(message.sid)


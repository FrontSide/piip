#!/usr/bin/env python3

"""
PiIP
A command line app that will send a rapberry Pi's private IP address per SMS to a phone
"""

from piip import send, getip
import yaml

CONFIG_FILE = "/etc/piipconf.yaml"

def main():

    stream = open(CONFIG_FILE, "r")
    conf = yaml.load_all(stream).__next__()

    twilio_id = conf["twilio"]["account_sid"]
    twilio_secret = conf["twilio"]["auth_token"]

    target_phone = conf["phones"]["target_number"]
    source_phone = conf["phones"]["source_number"]

    send.send(twilio_id, twilio_secret, target_phone, source_phone, getip.get_ips())

if __name__ == '__main__':
    main()
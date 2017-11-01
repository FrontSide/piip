## Piip

Send the private IP address of a Raspberry PI 
(or any linux machine for that matter) per SMS to a phone.

You might want to chose to run `piip` at machine startup
so you know with which IP to connect to it.

## Requirements

- python3 on your raspberryPi
- A twilio account (free account is sufficient) with a phone number that can send outgoing messaged
- A target phone

## Install

```
sudo pip install git+https://github.com/frontside/piip.git
```

Then update `/etc/piipconf.yaml` with your twilio credentials and phone numbers

Alternatively:
- Clone this repository
- Run `make build`
- And then again update `/etc/piipconf.yaml`

## Usage

Run with `piip`

To get the script to run a startup edit `/etc/rc.local` and add the script execution command.


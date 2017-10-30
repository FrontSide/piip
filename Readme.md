## Piip

Send the private IP address of a Raspberry PI 
(or any linux machine for that matter) per SMS to a phone.

You might want to chose to run `send.py` at machine startup
so you know with which IP to connect to it.

## Install
- Clone this repository
- `make build`
- Update the variables in `send.py` with your twilio credentials and phone numbers

Run with `./send.py`

To get the script to run a startup edti `/etc/rc.local` and add the script execution command.

## Requirements 
- A twilio account (free account is sufficient) with a phone number that can send outgoing messaged.
- A target phone of course.




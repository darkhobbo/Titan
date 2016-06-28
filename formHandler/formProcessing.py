from flask import render_template
import os
import requests


def process_form(req):
    send_msg_test()
    if req.method == 'POST':
        return 'Processing Form'
    else:
        # Showing Form Template
        return render_template('simple_form.html')


def send_msg_test():
    r = requests.post(
        'https://api.mailgun.net/v3/gregpetersen.ca/messages',
        auth=('api', os.environ['APIKEY']),
        data={'from': 'gregpetersen <postmaster@gregpetersen.ca>',
              'to': os.environ['ADMIN'],
              'subject': 'TEST O PLZ email',
              'text': 'You just sent yourself an email.'})
    # print(r.text)
    # print(r.status_code)
    # Testing something
    return r

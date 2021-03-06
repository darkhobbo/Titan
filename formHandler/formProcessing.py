"""Form processing module. Has two functions: process_form and send_msg_test."""
from flask import render_template
import os
import requests


def process_form(req):
    """Based on request, send message or render template."""
    if req.method == 'POST':
        return send_msg_test(req)
    else:
        # Showing Form Template
        return render_template('simple_form.html')


def send_msg_test(new_req):
    """Handles request and sends email."""
    print(new_req)
    if new_req.form['_gotcha'] != "":
        return "Gotcha ye robit"
    else:
        subj = new_req.form['_subject'] if new_req.form['_subject'] != "" else "New message from website."

        new_data = {'from': new_req.form['_replyto'],
                    'to': os.environ['ADMIN'],
                    'subject': subj,
                    'text': new_req.form['_message']}

        if new_req.form['_cc'] != "":
            new_data['cc'] = new_req.form['_cc']

        r = requests.post(
            os.environ['APIURL'],
            auth=('api', os.environ['APIKEY']),
            data=new_data)

        print(r.text)
        print(r.status_code)
        return render_template('message_submitted.html')

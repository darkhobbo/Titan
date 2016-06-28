from flask import render_template
import requests


def process_form(req):
    #send_simple_message()
    if req.method == 'POST':
        return 'Processing Form'
    else:
        # Showing Form Template
        return render_template('simple_form.html')


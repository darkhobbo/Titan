"""Main python file. Accepts requests and routes them."""
from flask import Flask
from flask import request

import formHandler

process_form = formHandler.process_form

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    """Processes request sent to '/' route."""
    return process_form(request)

if __name__ == '__main__':
    app.run()


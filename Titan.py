from flask import Flask
from flask import request

import formProcessing
process_form = formProcessing.process_form

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    return process_form(request)

if __name__ == '__main__':
    app.run()

#!/usr/bin/python3
""" Basic flask hello world """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ The hello world thing """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbtn():
    """ different directory """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_str(text):
    """ text variable """
    parse = "C "
    parse = parse + text.replace("_", " ")
    return parse


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def hello_str2(text='is cool'):
    """ text variable """
    pars = "Python "
    pars = pars + text.replace("_", " ")
    return pars


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """ checks if n is number """
    if (type(n) is int):
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

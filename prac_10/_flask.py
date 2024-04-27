from flask import Flask

app = Flask(__name__)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5.0 + 32.0


@app.route('/')
def hello_world():
    """Return a 'Hello, World!' string as a webpage."""
    return '<h1>Hello, World:)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    """Greet the person using the name provided in the URL or just say 'Hello'."""
    return f'<h1>Hello {name if name else "World"}!</h1>'


@app.route('/convert/<float:celsius>')
def convert_temperature(celsius):
    """Convert a Celsius value from the URL to Fahrenheit and display both."""
    fahrenheit = celsius_to_fahrenheit(celsius)
    return f'<p>{celsius}°C is {fahrenheit}°F.</p>'


app.run(debug=True)

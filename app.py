from flask import Flask

from os import environ

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Web APP'


if __name__ == '__main__':
    port = environ.get('APP_PORT', '5000')
    port = int(port)
    app.run(debug=True, host='0.0.0.0', port=port)
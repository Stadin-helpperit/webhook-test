from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', '5002'))
    app.run(port=PORT)

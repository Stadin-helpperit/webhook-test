from flask import Flask, request
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    req = request.get_json(silent=True, force=True)

    fulfillmentText = 'Success'

    query_result = req.get('query_Result')

    userInput = query_result.get('parameters').get('telegram-command')

    print(userInput)

    return {
        "fulfillmentText": fulfillmentText

    }


if __name__ == '__main__':
    app.run(port='5002')

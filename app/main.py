from flask import Flask, request
import os
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/webhook', methods=['POST', 'GET'])
def webhook():
    req = request.get_json(force=True)

    print(req)

    fulfillmentText = 'Success'

    query_result = req.get('queryResult')

    userInput = query_result.get('parameters').get('telegram-command')

    print(userInput)

    return {
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [fulfillmentText]

                }
            }
        ]


    }


if __name__ == '__main__':
    app.run(port='5002')

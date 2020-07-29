from googlecloud_wrapper import GooglecloudWrapper
from threading import Thread
from flask import Flask
import requests

app = Flask("transrption_service")
decisionModuleUrl = "http://127.0.0.1:7000"

gcWrapper = GooglecloudWrapper()

@app.route('/', methods=['POST'])
def dataReceived(data):
    send(gcWrapper.recognize(data))

def send(response):
    r = requests.post(decisionModuleUrl, data=response)
    return r

if __name__ == '__main__':
    app.run(debug=True, port=6100, use_reloader=False)

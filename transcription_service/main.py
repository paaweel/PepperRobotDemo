from googlecloud_wrapper import GooglecloudWrapper
from threading import Thread
from flask import Flask
import requests

app = Flask("transrption_service")
decisionModuleUrl = "http://127.0.0.1:6200"
listeningServiceUrl = "http://127.0.0.1:6000/listen"

gcWrapper = GooglecloudWrapper()


@app.route('/run', methods=['POST'])
def run():
    r = requests.get(listeningServiceUrl, data="")
    return "DONE"

@app.route('/', methods=['POST'])
def dataReceived(data):
    send(gcWrapper.recognize(data))

def send(response):
    print(response)
    r = requests.post(decisionModuleUrl, data=response)
    return r

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)

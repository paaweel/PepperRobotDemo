import requests
from service_handler import ServiceHandler


class Communicator:
    def __init__(self, language='English'):
        self.language = language
        self.service_handler = ServiceHandler()
        self.say_url = self.service_handler.sayUrl
        self.listen_url = self.service_handler.listenUrl

    def say(self, text, verbose=True):
        response = requests.post(self.say_url, data=text).content
        if verbose:
            print(response)

    def listen(self, verbose=True):
        print("I am requesting from " + self.listen_url)
        response = requests.get(self.listen_url).content
        if verbose:
            print(response)
        return response

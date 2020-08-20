import json
import os

import requests


class Communicator:
    def __init__(self, path, language='English', test=True):
        self.language = language
        with open(os.path.join(path, 'config.json')) as f:
            config = json.load(f)
            if test:
                variables = config['development']
            else:
                variables = config['production']
        self.say_url = variables['say_url']
        self.listen_url = variables['listen_url']

    def say(self, text, verbose=True):
        response = requests.post(self.say_url, data=text).content
        if verbose:
            print(response)

    def listen(self, verbose=True):
        response = requests.get(self.listen_url).content
        if verbose:
            print(response)
        return response

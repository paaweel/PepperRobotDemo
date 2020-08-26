# import aiohttp
# import asynio
# from aiohttp import ClientSession
import requests


class Pepper():

    def __init__(self):
        self.port = 5000
        self.listenUrl = self._get_url("listening_service")
        self.transcriptionUrl = self._get_url("transcription_service")
        self.sayUrl = self._get_url("say_service")

    def _get_url(self, name):
        return "http://" + name + ":" + str(self.port)

    def get_transcription(self):
        return requests.get(self.listenUrl + "/")

    def say_something(self):
        print(self.sayUrl + "/")
        requests.post(url=self.sayUrl + "/", data="How you doin")

    def say(self, data):
        print(self.sayUrl + "/")
        requests.post(url=self.sayUrl + "/", data=data)

    def get_raw_audio(self):
        data = requests.get(url=self.listenUrl + "/listen")
        print (data)
        return data

# import aiohttp
# import asynio
# from aiohttp import ClientSession
import requests


class Pepper:
    def __init__(self):
        self.port = 5000
        self.listenUrl = self.__get_url("192.168.1.102")
        self.transcriptionUrl = self.__get_url("transcription_service")
        self.sayUrl = self.__get_url("say_service")
        self.emotionListenUrl = self.__get_url("emotion_listen_service")

    def __get_url(self, name):
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
        return data

    def get_audio_emotion(self, raw_audio):
        emotion = requests.post(url=self.emotionListenUrl + "/emotion", data=raw_audio)
        return emotion

    def save_audio_as_wav(self):
        raw_audio = self.get_raw_audio()
        self.get_audio_emotion(raw_audio)


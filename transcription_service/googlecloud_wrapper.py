from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

class GooglecloudWrapper():

    def __init__(self):
        self.client = speech_v1.SpeechClient()

        self.encoding = enums.RecognitionConfig.AudioEncoding.FLAC
        self.sample_rate_hertz = 44100
        self.language_code = 'en-US'

        self.config = {
            'encoding': self.encoding,
            'sample_rate_hertz': self.sample_rate_hertz,
            'language_code': self.language_code
        }

        # self.uri = 'gs://bucket_name/file_name.flac'
        # self.audio = {'uri': uri}

    def recognize(self, audio):
        return self.client.recognize(self.config, audio)

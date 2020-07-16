from googlecloud import GoogleCloud

class GooglecloudWrapper():

    def __init__(self):
        client = speech_v1.SpeechClient()

        self.encoding = enums.RecognitionConfig.AudioEncoding.FLAC
        self.sample_rate_hertz = 44100
        self.language_code = 'en-US'

        self.config = {
            'encoding': encoding,
            'sample_rate_hertz': sample_rate_hertz,
            'language_code': language_code
        }
        
        # self.uri = 'gs://bucket_name/file_name.flac'
        # self.audio = {'uri': uri}

    def recognize(audio):
        return self.client.recognize(self.config, audio)

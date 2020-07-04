import json
import os
import string
import time
import qi


class Pepper:
    def __init__(self, path, ip="192.168.1.123", port="9559", language='English'):
        # type: (str, str) -> object
        self.session = qi.Session()
        self.ip = ip
        self.port = port
        self.language = language
        with open(os.path.join(path, 'expected_vocabulary.json'))as f:
            expected_vocabulary = json.load(f)
        self.expected_vocabulary = expected_vocabulary[string.lower(language)]

    def connect(self):
        try:
            # Initialize qi framework.
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
            print ("Can't connect to Pepper at ip \"" + self.ip + "\" on port " + str(self.port) + ".\n"
                                                                                                   "Please check your "
                                                                                                   "script arguments. "
                                                                                                   "Run with -h "
                                                                                                   "option for help.")

    def say(self, text):
        tts = self.session.service("ALTextToSpeech")
        tts.say(text)

    def listen(self):
        asr = self.session.service(" ALSpeechRecognition")
        asr.setVocabulary(self.expected_vocabulary, False)

        # Start the speech recognition engine with user Test_ASR
        asr.subscribe("Test_ASR")
        print
        'Speech recognition engine started'
        time.sleep(20)
        asr.unsubscribe("Test_ASR")

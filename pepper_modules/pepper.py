import json
import os
import string
import qi


class Pepper:
    def __init__(self, path, ip="192.168.1.123", port="9559", language='English', test_mode=False):
        # type: (str, str, str, str) -> None
        self.session = qi.Session()
        self.ip = ip
        self.port = port
        self.language = language
        with open(os.path.join(path, 'expected_vocabulary.json'))as f:
            expected_vocabulary = json.load(f)
        self.expected_vocabulary = expected_vocabulary[string.lower(language)]
        if not test_mode:
            self.listen_session = self.session.service(" ALSpeechRecognition")
            self.listen_session.setVocabulary(self.expected_vocabulary, False)
        self.listen_buf = []

    def connect(self):
        try:
            # Initialize qi framework.
            self.session.connect("tcp://" + self.ip + ":" + str(self.port))
        except RuntimeError:
            print ("Can't connect to Pepper at ip \""
                + self.ip + "\" on port " + str(self.port) + ".\n"
                + "Please check your script arguments. "
                + "Run with -h option for help.")

    def say(self, text):
        tts = self.session.service("ALTextToSpeech")
        tts.say(text)

    def open_listen(self):
        # Start the speech recognition engine with user Test_ASR
        self.listen_session.subscribe("Test_ASR")
        print('Speech recognition engine started.')

    def close_listen(self):
        self.listen_session.unsubscribe("Test_ASR")
        print('Speech recognition engine stopped.')

    def open_watch(self):
        pass

    def close_watch(self):
        pass

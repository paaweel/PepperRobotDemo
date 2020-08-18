import string
import random

import qi
import sys

import numpy as np
import time
from audio_session_manager import AudioSessionManager


class PepperAudioProvider(object):
    RATE = 16000
    """
    Provides acsess to pepper's micropones. 
    """

    def __init__(self):
        """
        Initialise services and variables.
        """
        super(PepperAudioProvider, self).__init__()
        # Get the service ALAudioDevice.
        # self.audio_service.unsubscribe(self.module_name)

    def connect(self, ip="192.168.1.123", port="9559", language="English"):
        # type: (str, str, str) -> None
        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + ip + ":" + port)
            print("Robot connected to listening_module.")
        except RuntimeError:
            print("Can't connect to Pepper at ip \""
                  + ip + "\" on port " + port + ".\n"
                  + "Please check your script arguments. "
                  + "Run with -h option for help.")

    def listen(self, timeout=1):
        """
        Collect pepper's microphone output for timeout [s]
        """
        # audio = [chunk for chunk in self.getAudio(timeout)]

        return self.getAudio(timeout)

    def getAudio(self, timeout=1):
        with AudioSessionManager(self.session, timeout * 10) as stream:
            content = [content.tobytes() for content in stream.data()]
            return content


if __name__ == '__main__':
    session = qi.Session()
    ip = '192.168.1.123'
    port = '9559'
    try:
        session.connect("tcp://" + ip + ":" + port)
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + ip + "\" on port "
        + port + ".\n" + "Please check your script arguments. "
        + "Run with -h option for help.")
        sys.exit(1)

    provider = PepperAudioProvider()
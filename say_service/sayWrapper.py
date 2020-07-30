import qi


class SayWrapper:
    def __init__(self, testMode, ip="192.168.1.123", port="9559", language="English"):
        # type: (bool, str, str, str) -> None
        self.testMode = testMode
        if not self.testMode:
            self.session = qi.Session()
            try:
                self.session.connect("tcp://" + ip + ":" + port)
                self.say_service = self.session.service("ALTextToSpeech")
                self.say_service.setLanguage(language)
                print("Robot connected to SAY module.")
            except RuntimeError:
                print("Can't connect to Pepper at ip \""
                    + ip + "\" on port " + port + ".\n"
                    + "Please check your script arguments. "
                    + "Run with -h option for help.")
            self.client = None
        else:
            print("Robot in the SAY TEST mode.")


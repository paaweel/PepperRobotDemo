class ServiceHandler:
    def __init__(self):
        self.port = 5000
        self.listenUrl = self._get_url("listening_service") + "/listen"
        self.transcriptionUrl = self._get_url("transcription_service") + "/"
        self.sayUrl = self._get_url("say_service") + "/"

    def _get_url(self, name):
        return "http://" + name + ":" + str(self.port)
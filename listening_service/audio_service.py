from audio_providers.pepper_audio_provider import PepperAudioProvider


class AudioService:
    """docstring for AudioService."""

    def __init__(self):
        self.ap = PepperAudioProvider()

    def listen(self, timeout=0):
        return self.ap.listen(timeout)

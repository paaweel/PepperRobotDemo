# from injector import inject

from audio_providers.audio_provider import AudioProvider
from audio_providers.pepper_audio_provider import PepperAudioProvider

class AudioService:
    """docstring for AudioService."""
    # @inject
    # def __init__(self, ap: AudioProvider):
    #     self.ap = audioProvider

    def __init__(self):
        self.ap = PepperAudioProvider()

    def listen(self, timeout=1):
        return self.ap.listen(timeout)

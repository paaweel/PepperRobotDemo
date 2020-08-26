from injector import singleton
from audio_service import AudioService


def configure(binder):
    binder.bind(AudioService, to=AudioService, scope=singleton)
    return binder

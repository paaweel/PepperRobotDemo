# DO NOT USE
# py2 cannot into FlaskInjector 
from injector import singleton

# modules
from audio_providers.audio_provider import AudioProvider
from audio_providers.pepper_audio_provider import PepperAudioProvider
# service
from audio_service import AudioService

def configure(binder):
    binder.bind(AudioService, to=AudioService, scope=singleton)
    binder.bind(AudioProvider, to=PepperAudioProvider, scope=singleton)
    return binder

import io
import os
from pepper import Pepper
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from tests.Microphone import Microphone


def listen_google(session):
    print("listening fun started")
    file = io.open("test", 'w')
    language_code = 'pl-PL'
    RATE = 16000
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/ilona/Data/Dokumenty/Master_Studies/semestr_1/Pepper/" \
                                                   "YT Voice Control-69219517df9b.json"

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with Microphone(session) as stream:
        print("mic start")
        audio_generator = stream.generator()

        requests = (types.StreamingRecognizeRequest(audio_content=content.tobytes())
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        # self.listen_print_loop(responses, stream, file)


if __name__ == '__main__':
    test_path = os.getcwd()
    main_path = os.path.dirname(test_path)
    pepper = Pepper(main_path, "192.168.1.123", "9559", 'English', True)
    pepper.connect()
    listen_google(pepper.session)

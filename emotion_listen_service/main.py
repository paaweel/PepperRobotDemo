from flask import Flask, request

from emotion_service import EmotionService

app = Flask('emotion_listen_service')
emotion_service = EmotionService()


@app.route('/listen', methods=['POST'])
def listen():
    print("Providing audio from listen service.")
    # get data from request body
    emotion_service.add_audio_data(request.json)
    return "Audio data was received."


@app.route('/emotion', methods=['POST'])
def get_emotion():
    print("Get emotions from audio data using AI.")
    print(request.data)
    emotion_service.audio_file_service.response_to_wav(request.data)
    return "OK"


if __name__ == '__main__':
    """
    emotion_service.audio_file_service.wav_to_txt_bytes()
    emotion_service.audio_file_service.txt_bytes_to_wav()
    """
    # emotion_service.audio_file_service.response_to_wav()
    # keras + flask do not work (multithreading problem) unless keras is called from the main thread for the 1st time
    # print(emotion_service.predict())
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=False)

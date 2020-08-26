from flask import Flask
from audio_service import AudioService

app = Flask('listening_service')

service = AudioService()


@app.route('/listen', methods=['GET'])
def listen():
    print("Start listen")
    data = service.listen(2)
    print(str(data))
    return str(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000, use_reloader=False)

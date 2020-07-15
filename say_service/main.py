from flask import Flask, request
import qi

app = Flask('sayservice')
text = ""
ttsSession = None
session = None


def connect(ip="192.168.1.123", port="9559", language="English"):
    # type: (str, str, str) -> None
    global ttsSession, session
    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + port)
        ttsSession = session.service("ALTextToSpeech")
        ttsSession.setLanguage(language)
        ttsSession.say("don't say it") #czemu mowi to dwa razy? Tego wgl tutaj nie powinno byc
        print("Robot connected to SAY module.")
    except RuntimeError:
        print("Can't connect to Pepper at ip \""
              + ip + "\" on port " + port + ".\n"
              + "Please check your script arguments. "
              + "Run with -h option for help.")


@app.route('/', methods=['POST'])
def say_text():
    if ttsSession:
        global text, ttsSession
        text = request.get_data()
        ttsSession.say(text)
        return "SAY string was sent."
    return "Robot not connected."


@app.route('/test', methods=['POST'])
def say_text_test():
    global text
    text = request.get_data()
    print(text)
    return "SAY string was sent."


if __name__ == '__main__':
    test = False
    if not test:
        connect()
    app.run(debug=True, port=5000, use_reloader=False)

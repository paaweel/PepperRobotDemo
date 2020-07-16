import time

from flask import Flask, request
import qi

app = Flask('emotionservice')
emoSession = None
session = None


def connect(ip="192.168.1.123", port="9559", language="English"):
    # type: (str, str, str) -> None
    global session, emoSession
    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + port)
        emoSession = session.service("ALMood")
        print("Robot connected to EMOTION module.")
    except RuntimeError:
        print("Can't connect to Pepper at ip \""
              + ip + "\" on port " + port + ".\n"
              + "Please check your script arguments. "
              + "Run with -h option for help.")


@app.route('/reaction', methods=['GET'])
def get_reaction():
    global emoSession
    if emoSession:
        emoSession.subscribe("reactionMood", "Active")
        time.sleep(2)
        reaction = emoSession.getEmotionalReaction()
        emoSession.unsubscribe("reactionMood")
        return reaction
    return "Robot not connected."


@app.route('/state', methods=['GET'])
def get_state():
    global emoSession
    if emoSession:
        emoSession.subscribe("stateMood", "Active")
        time.sleep(3)
        state = emoSession.currentPersonState()
        emoSession.unsubscribe("stateMood")
        return state
    return "Robot not connected."


if __name__ == '__main__':
    test = False
    if not test:
        connect()
    app.run(debug=True, port=7000, use_reloader=False)

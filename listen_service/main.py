import time
from threading import Thread
from flask import Flask
import qi
from googlecloud import GoogleCloud

app = Flask('listenservice')
text = ""
gcSession = None


def connect(ip="192.168.1.123", port="9559", language="English"):
    # type: (str, str, str) -> None
    global gcSession
    session = qi.Session()
    try:
        session.connect("tcp://" + ip + ":" + port)
        gcSession = GoogleCloud(session)
        print("Robot connected to LISTEN module.")
    except RuntimeError:
        print("Can't connect to Pepper at ip \""
              + ip + "\" on port " + port + ".\n"
              + "Please check your script arguments. "
              + "Run with -h option for help.")


# TODO accumulate the answer and redirect from console into API response
@app.route('/', methods=['GET'])
def listen():
    if gcSession:
        global text, gcSession
        threadRecognition = Thread(target=gcSession.run,
                                   args=("test.txt",))
        threadRecognition.start()
        time.sleep(20)
        threadRecognition.do_run = False
        threadRecognition.join()
        return "LISTEN function is not ready yet."
    return "Google Cloud not connected."


@app.route('/test', methods=['GET'])
def listen_test():
    global text
    print("Tell me something, boy.")
    text = raw_input()
    return text


if __name__ == '__main__':
    test = True
    if not test:
        connect()
    app.run(debug=True, port=6000)

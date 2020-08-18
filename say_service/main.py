from flask import Flask, request
from sayWrapper import SayWrapper

app = Flask('say_service')

sayWrapper = SayWrapper(testMode=False)


@app.route('/', methods=['POST'])
def say_text():
    global sayWrapper
    if sayWrapper.say_service:
        text = request.get_data()
        sayWrapper.say_service.say(text)
        return "SAY string was sent."
    return "Robot not connected."


@app.route('/test', methods=['POST'])
def say_text_test():
    global sayWrapper
    text = request.get_data()
    print(text)
    return "SAY string was sent."

if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)

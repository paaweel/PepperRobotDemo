import qi
from multiprocessing import Process
from threading import Thread


class VideoWrapper:
    def __init__(self, ip="192.168.1.123", port="9559", language="English"):
        # type: (str, str, str) -> None
        self.session = qi.Session()
        try:
            self.session.connect("tcp://" + ip + ":" + port)
            self.video_service = self.session.service("ALVideoDevice")
            print("Robot connected to VIDEO module.")
        except RuntimeError:
            print("Can't connect to Pepper at ip \""
                  + ip + "\" on port " + port + ".\n"
                  + "Please check your script arguments. "
                  + "Run with -h option for help.")

        self.resolution = 2
        self.colorSpace = 11
        self.fps = 20
        self.captureFrames = False
        self.client = None
        self.process = Process(target=self.capture)
        self.thread = None

    def startThread(self):
        self.captureFrames = True
        self.thread = Thread(target=self.capture)
        self.thread.daemon = True
        self.thread.start()

    def stopThread(self):
        self.captureFrames = False
        self.thread.join()

    def capture(self):
        print 'getting images in remote'
        while self.captureFrames:
            # result = self.video_service.getImageRemote(self.client)
            print(self.captureFrames)

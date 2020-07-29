import numpy as np
from PIL import Image
import qi
from multiprocessing import Process
from threading import Thread
from collections import deque


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
        self.lastFrames = deque([], maxlen=10)

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
        self.client = self.video_service.subscribe(
            "python_client",
            self.resolution,
            self.colorSpace,
            self.fps)
        result = self.video_service.getImageRemote(self.client)
        if result is None:
            print 'cannot capture.'
            self.stopThread()
        elif result[6] is None:
            print 'no image data string.'
            self.stopThread()
        width = result[0]
        height = result[1]
        image = np.zeros((height, width, 3), np.uint8)
        im = Image.frombytes("RGB", (width, height), image)
        self.lastFrames.append(im)

        while self.captureFrames:
            result = self.video_service.getImageRemote(self.client)
            if result is None:
                print 'cannot capture.'
                self.stopThread()
            elif result[6] is None:
                print 'no image data string.'
                self.stopThread()
            else:
                image = str(bytearray(result[6]))
                im = Image.frombytes("RGB", (width, height), image)
                self.lastFrames.append(im)
        self.video_service.unsubscribe(self.client)

    def getLastFrames(self, n=10):
        # it's faster to index a list than a deque collection
        return list(self.lastFrames)[0:n]

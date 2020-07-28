
import time
from six.moves import queue
import random
import numpy as np

class AudioSessionManager(object):
    """docstring for AudioSessionManager."""
    RATE = 16000

    def __init__(self, session, nFrames):
        super(AudioSessionManager, self).__init__()
        self._buff = queue.Queue()
        self.isProcessingDone = True
        self.nbOfFramesToProcess = nFrames
        self.framesCount = 0
        self.micFront = []
        self.session = session
        self.audio_service = self.session.service("ALAudioDevice")
        self.module_name = "SoundProcessingModule" + str(random.randint(0, 10000))
        print("Service is registered")
        session.registerService(self.module_name, self)


    def __enter__(self):
        print("ENETRING")
        self.audio_service.setClientPreferences(self.module_name, AudioSessionManager.RATE, 3, 0)
        self.audio_service.subscribe(self.module_name)
        self.isProcessingDone = False
        return self


    def __exit__(self, type, value, traceback):
        print("EXITING")
        self.audio_service.unsubscribe(self.module_name)
        self.isProcessingDone = True
        self._buff.put(None)


    def processRemote(self, nbOfChannels, nbOfSamplesByChannel, timeStamp, inputBuffer):
        print("PROCESSS REMOTE" + str(self.framesCount))
        if (self.framesCount <= self.nbOfFramesToProcess):
            self.framesCount = self.framesCount + 1
            # convert inputBuffer to signed integer as it is interpreted as a string by python
            # self.micFront = self.convertStr2SignedInt(inputBuffer)
            # push input to the queue
            self._buff.put(inputBuffer)
        else :
            self.isProcessingDone=True

    def generator(self):
        print("GENERATOR")
        while not self.isProcessingDone:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return

            data = np.frombuffer(chunk, np.int16)
            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data = np.concatenate((data, np.frombuffer(chunk, np.int16)), axis=None)
                except queue.Empty:
                    break

            yield data
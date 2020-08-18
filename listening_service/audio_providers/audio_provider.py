from abc import ABCMeta, abstractmethod

class AudioProvider(ABCMeta):
    """Abstract audio provider"""

    def __init__(self):
        pass

    @abstractmethod
    def listen(self, timeout=1):
        pass

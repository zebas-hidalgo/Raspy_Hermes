from abc import ABC, abstractmethod

class BaseGateway(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

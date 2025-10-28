from abc import ABC, abstractmethod
class AbstractFilter(ABC):
    @abstractmethod
    def filtering(self, text: str):
        pass

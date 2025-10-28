from abc import ABC, abstractmethod

class Indexer(ABC):
    @abstractmethod
    def build(self, folder_path):
        pass

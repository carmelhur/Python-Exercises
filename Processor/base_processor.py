from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List

class BaseProcessor(ABC):
    @abstractmethod
    def run(self, path: str) -> Dict[str, List[str]]:
        raise NotImplementedError

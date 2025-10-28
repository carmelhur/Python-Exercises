from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Score(ABC):
    @abstractmethod
    def calculate(self, index: Dict[str, Dict[str, int]]) -> Dict[str, Dict[str, float]]:
        pass

from abc import ABC, abstractmethod

class Creature(ABC):
    def __init__(self) -> None:
        self.name: str
        self.type: str

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} Creature"
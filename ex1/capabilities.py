from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal() -> str:
        pass


class TransformCapability(ABC):

    @abstractmethod
    def transform() -> str:
        pass

    @abstractmethod
    def revert() -> str:
        pass

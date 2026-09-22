from ex0 import Creature, CreatureFactory
from .capabilities import HealCapability, TransformCapability
from .creatures_cap import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory, HealCapability):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()

class TransformCreatureFactory(Creature, TransformCapability):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()

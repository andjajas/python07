from ex0.creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon
from ex0.factories import CreatureFactory, FlameFactory, AquaFactory

def create_creature(fac_obj: CreatureFactory):
    if isinstance(fac_obj, FlameFactory):
        fac_obj.create_base()
        fac_obj.create_evolved()

if __name__ == "__main__":
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()

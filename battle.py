#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory


def factory(fac_obj: CreatureFactory) -> None:
    base_crea = fac_obj.create_base()
    evol_crea = fac_obj.create_evolved()
    print(base_crea.describe())
    print(base_crea.attack())
    print(evol_crea.describe())
    print(evol_crea.attack())


def battle(flame_fac: FlameFactory, aqua_fac: AquaFactory) -> None:
    base_flame = flame_fac.create_base()
    base_aqua = aqua_fac.create_base()
    print(base_flame.describe())
    print(" vs.")
    print(base_aqua.describe())
    print(" fight!")
    print(base_flame.attack())
    print(base_aqua.attack())


def main() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    print("Testing factory")
    factory(flame_fac)
    print("\nTesting factory")
    factory(aqua_fac)
    print("\nTesting battle")
    battle(flame_fac, aqua_fac)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(
            "You can still evade this exception,"
            " if you CTRL+C before this program runs")
    except Exception as e2:
        print(e2)

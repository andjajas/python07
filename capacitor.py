#!/usr/bin/env python3
from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability,
)


def main() -> None:
    healing_fac = HealingCreatureFactory()
    base_heal = healing_fac.create_base()
    evol_heal = healing_fac.create_evolved()
    print("Testing Creature with healing capability")
    print(" base:")
    print(base_heal.describe())
    print(base_heal.attack())
    if isinstance(base_heal, HealCapability):
        print(base_heal.heal())
    print(" evolved:")
    print(evol_heal.describe())
    print(evol_heal.attack())
    if isinstance(evol_heal, HealCapability):
        print(f"{evol_heal.heal()}\n")
    trans_fac = TransformCreatureFactory()
    base_trans = trans_fac.create_base()
    evol_trans = trans_fac.create_evolved()
    print("Testing Creature with transform capability")
    print(" base:")
    print(base_trans.describe())
    print(base_trans.attack())
    if isinstance(base_trans, TransformCapability):
        print(base_trans.transform())
    print(base_trans.attack())
    if isinstance(base_trans, TransformCapability):
        print(base_trans.revert())
    print(" evolved:")
    print(evol_trans.describe())
    print(evol_trans.attack())
    if isinstance(evol_trans, TransformCapability):
        print(evol_trans.transform())
    print(evol_trans.attack())
    if isinstance(evol_trans, TransformCapability):
        print(evol_trans.revert())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e1:
        print(e1)
    except Exception as e2:
        print(e2)

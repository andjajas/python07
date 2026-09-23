#!/usr/bin/env python3
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    InvalidStrategyError,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        factory, strategy = opponents[i]  # unpacks the tuple for creature1
        creature1 = (
            factory.create_base()
        )  # creatures shown in example are all base creatures
        for j in range(i + 1, len(opponents)):
            factory2, strategy2 = opponents[j]
            creature2 = factory2.create_base()
            print("\n* Battle *")
            print(f"{creature1.describe()}")
            print(" vs.")
            print(f"{creature2.describe()}")
            print(" now fight!")
            try:
                strategy.act(creature1)
                strategy2.act(creature2)
            except InvalidStrategyError as e:
                print(e)


def main() -> None:
    # Tournament 0
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    opponents = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    battle(opponents)
    # Tournament 1
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    battle(opponents)
    # Tournament 2
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    battle(opponents)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e1:
        print(e1)
    except Exception as e2:
        print(e2)

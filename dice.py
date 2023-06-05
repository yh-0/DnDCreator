import random
from typing import Tuple, List


class Dice:
    @staticmethod
    def roll(size: int, count: int = 1):
        rolls = [random.randint(1, size) for _ in range(count)]
        return sum(rolls), rolls

    @staticmethod
    def show_single(roll: Tuple[int, List[int]]):
        return f"{roll[0]} {roll[1]}"

    @classmethod
    def roll_stats(cls):
        rolls = [cls.roll(6, 4) for _ in range(6)]
        lowest_removed = [sorted(roll[1])[1:] for roll in rolls]
        return [(sum(roll), roll) for roll in lowest_removed]

    @staticmethod
    def show_rolls(rolls: List[Tuple[int, List[int]]]):
        return "\n".join([f"{roll[0]:<{7 - len(str(roll[0]))}} {roll[1]}" for roll in rolls])

import random


class Dice:
    @classmethod
    def roll(cls, size, count=1):
        rolls = [random.randint(1, size) for _ in range(count)]
        return sum(rolls), rolls

    @classmethod
    def show_single(cls, roll):
        return f"{roll[0]} {roll[1]}"

    @classmethod
    def roll_stats(cls):
        rolls = [cls.roll(6, 4) for _ in range(6)]
        lowest_removed = [sorted(roll[1])[1:] for roll in rolls]
        return [(sum(roll), roll) for roll in lowest_removed]

    @classmethod
    def show_rolls(cls, rolls):
        return "\n".join([f"{roll[0]:<{7 - len(str(roll[0]))}} {roll[1]}" for roll in rolls])

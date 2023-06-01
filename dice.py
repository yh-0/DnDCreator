import random

class Dice:

    @classmethod
    def roll(self, size, count=1):
        if count == 1:
            return random.randint(1, size)
        
        return [random.randint(1, size) for _ in range(count)]

    @classmethod
    def roll_stats(self):
        return [sorted(self.roll(6, 4))[1:] for _ in range(6)]

    @classmethod
    def show_rolls(self, rolls):
        return "\n".join([f'{sum(roll):<{7 - len(str(sum(roll)))}} {roll}' for roll in rolls])
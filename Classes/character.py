from typing import List, Dict, Tuple


class Character:
    def __init__(self) -> None:
        self.name: str = "John"
        self.attr: List[int] = [10, 10, 10, 10, 10, 10]
        self.attr_bonus: Dict[str, int] = {
            "STR": 0, 
            "DEX": 0, 
            "CON": 0, 
            "INT": 0, 
            "WIS": 0, 
            "CHA": 0
        }
        self.hp: int = 0
        self.ac: int = 10
        self.speed: int = 30

    def __repr__(self) -> str:
        return f"{self.name}\n{self.attr}\nHP: {self.hp}\nAC: {self.ac}\nSPEED: {self.speed}"

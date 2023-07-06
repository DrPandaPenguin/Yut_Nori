import random


class stick:
    def __init__(self) -> None:
        self.outcome = {1: "도", 2: "개", 3: "걸", 4: "윷", 5: "모"}

    @staticmethod
    def throw(self):
        distance = random.randint(1, 5)
        return self.outcome[distance]

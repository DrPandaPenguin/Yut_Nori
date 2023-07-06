import random


class Stick:
    outcome = {1: "도", 2: "개", 3: "걸", 4: "윷", 5: "모"}

    @staticmethod
    def throw():
        distance = random.randint(1, 5)
        return Stick.outcome[distance]

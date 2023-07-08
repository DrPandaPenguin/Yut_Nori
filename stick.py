import random


class Stick:
    outcome = {1: "do", 2: "ge", 3: "Gurl", 4: "yot", 5: "mo"}

    @staticmethod
    def throw():
        distance = random.randint(1, 5)
        return Stick.outcome[distance]

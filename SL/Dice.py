# Singleton Pattern for Dice
import random


class Dice:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Dice, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def roll():
        return random.randint(1, 6)


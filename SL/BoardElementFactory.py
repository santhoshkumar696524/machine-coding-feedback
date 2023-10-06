from Ladder import Ladder
from Snake import Snake


class BoardElementFactory:
    @staticmethod
    def create_snake(head, tail):
        return Snake(head, tail)

    @staticmethod
    def create_ladder(start, end):
        return Ladder(start, end)


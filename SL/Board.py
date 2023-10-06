from CellType import CellType
from Ladder import Ladder
from Snake import Snake


class Board:
    def __init__(self, size=100):
        self.size = size
        self.cells = {i: CellType.EMPTY for i in range(1, size + 1)}  # Initialize all cells as EMPTY
        self.snakes = []
        self.ladders = []

    def add_element(self, element):
        if isinstance(element, Snake):
            self.snakes.append(element)
        elif isinstance(element, Ladder):
            self.ladders.append(element)

    def is_cell_occupied(self, cell):
        return self.cells[cell] == CellType.PLAYER

    def move_player(self, player, dice_value):
        current_position = player.position
        new_position = current_position + dice_value

        # Check for snakes and ladders
        for snake in self.snakes:
            if new_position == snake.head:
                new_position = snake.tail
                break

        for ladder in self.ladders:
            if new_position == ladder.start:
                new_position = ladder.end
                break

        # Ensure the player does not go beyond the board size
        if new_position <= self.size:
            self.cells[current_position] = CellType.EMPTY  # Update the current cell
            self.cells[new_position] = CellType.PLAYER  # Update the new cell
            player.position = new_position


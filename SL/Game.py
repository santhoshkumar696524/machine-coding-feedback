from Board import Board
from BoardElementFactory import BoardElementFactory
from Dice import Dice
from Player import Player


class Game:
    def __init__(self):
        self.players = []
        self.board = None
        self.dice = Dice()
        self.observers = []

    def initialize_game(self):
        num_snakes = int(input())
        snakes = [tuple(map(int, input().split())) for _ in range(num_snakes)]

        num_ladders = int(input())
        ladders = [tuple(map(int, input().split())) for _ in range(num_ladders)]

        num_players = int(input())
        player_names = [input() for _ in range(num_players)]

        self.players = [Player(name) for name in player_names]

        self.board = Board()

        for snake in snakes:
            self.board.add_element(BoardElementFactory.create_snake(snake[0], snake[1]))

        for ladder in ladders:
            self.board.add_element(BoardElementFactory.create_ladder(ladder[0], ladder[1]))

        for player in self.players:
            self.board.cells[player.position] = player

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            if "player_won" in event:
                observer.player_won(event["player_won"])
            else:
                observer.player_moved(
                    event["player"],
                    event["dice_value"],
                    event["previous_position"],
                    event["new_position"]
                )

    def play_game(self):
        while True:
            for player in self.players:
                if player.position == self.board.size:
                    continue
                dice_value = self.dice.roll()
                previous_position = player.position
                player.move(dice_value)
                if player.position > self.board.size:
                    player.position = self.board.size - (player.position - self.board.size)
                event = {
                    "player": player,
                    "dice_value": dice_value,
                    "previous_position": previous_position,
                    "new_position": player.position
                }
                self.notify_observers(event)

                if player.position == self.board.size:
                    self.notify_observers({"player_won": player})
                    return

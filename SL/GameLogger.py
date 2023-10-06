from GameObserver import GameObserver


class GameLogger(GameObserver):
    def player_moved(self, player, dice_value, previous_position, new_position):
        print(f"{player.name} rolled a {dice_value} and moved from {previous_position} to {new_position}")

    def player_won(self, player):
        print(f"{player.name} wins the game!")

from Game import Game
from GameLogger import GameLogger

if __name__ == "__main__":
    snake_and_ladder_game = Game()
    snake_and_ladder_game.initialize_game()

    # Add the logger as an observer
    logger = GameLogger()
    snake_and_ladder_game.add_observer(logger)

    # Start the game
    snake_and_ladder_game.play_game()

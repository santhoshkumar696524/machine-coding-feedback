class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self, dice_value):
        self.position += dice_value

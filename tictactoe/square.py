class Square:
    def __init__(self):
        self.player = None

    def get_mark(self):
        if self.player is None:
            return " "
        else:
            return self.player.get_designation()
        
    def set_player(self, player):
        self.player = player

    def get_player(self):
        return self.player

    def occupied(self):
        return self.player is not None

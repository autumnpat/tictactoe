class Player:
    def __init__(self, designation):
        self.designation = designation

    def __repr__(self):
        return "Player: " + self.designation

    def get_designation(self):
        return self.designation
    
    def equal(self, player):
        return player.designation == self.designation
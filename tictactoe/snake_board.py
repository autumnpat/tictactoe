import variable_board
import logging

class SnakeBoard(variable_board.VariableBoard):
    """
    Allow non-straight connected chains, no branching
    """
    def __init__(self, xsize, ysize, goal, straight):
        super().__init__(xsize, ysize, goal)
        self.straight = straight

    def seek_goal(self, player, xcurrent, ycurrent, foundcount, xdir, ydir):
        if self.straight:
            return super().seek_goal(player, xcurrent, ycurrent, foundcount, xdir, ydir)
        
        #At this point I'm thinking I might want a full visitor or memoize pattern where
        #I have an object that knows how to traverse the board
        return self.seek_snake_goal(player, xcurrent, ycurrent, foundcount, [(xcurrent-xdir, ycurrent-ydir), (xcurrent,ycurrent)])

    def seek_snake_goal(self, player, xcurrent, ycurrent, foundcount, visited):
        logging.debug("seek_snake_goal (player: %s  xcurrent: %d  ycurrent: %d  foundcount: %d  visited: %s)", repr(player), xcurrent, ycurrent, foundcount, repr(visited))

        if foundcount == self.goal:
            logging.debug("found snake goal")
            return player
        
        for newx in range(xcurrent-1, xcurrent+2):
            for newy in range(ycurrent-1, ycurrent+2):
                if self.check_next_square_match(player, newx, newy) and (newx, newy) not in visited:
                    result = self.seek_snake_goal(player, newx, newy, foundcount+1, visited+[(newx,newy)])
                    if result is not None:
                        return result
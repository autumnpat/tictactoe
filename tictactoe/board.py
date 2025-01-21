import square
import logging

class IllegalMoveException(Exception):
    def __init__(self, reason):
        super(Exception, self).__init__("cannot move to proposed square: " + reason)

class Board:
    """
    Board enforces straight lines as goals and a 3x3 board
    """
    def __init__(self):
        self.do_initialization(3,3,3)

    def do_initialization(self, xsize, ysize, goal):
        """
        do_initialization allows for other board sizes and goal lengths
        """
        self.xsize = xsize
        self.ysize = ysize
        self.goal = goal
        self.board = []
        for x in range(self.xsize):
            r = []
            for y in range(self.ysize):
                r.append(square.Square())
            self.board.append(r)
        self.separator = "-+" * (self.xsize - 1) + "-"

    def __repr__(self):
        return self.board_state_string()

    def move(self, posx, posy, player):
        if not self.valid_position(posx, posy):
            raise IllegalMoveException("move off of board")
        if self.board[posx][posy].occupied():
            raise IllegalMoveException("occupied")
        self.board[posx][posy].set_player(player)

    def board_state_string(self):
        """
        board_state_string returns the current board state
        """
        result = []
        for x in self.board:
            result.append('|'.join([y.get_mark() for y in x ]))
            result.append(self.separator)
        result.pop()
        return '\n'.join(result)

    def winner(self):
        #Scan the board for occupied squares then do a constrained dfs
        for x in range(self.xsize):
            for y in range(self.ysize):
                square = self.board[x][y]
                if square.occupied():
                    result = self.start_scan_for_goal(square.get_player(), x, y, 1)
                    if result != None:
                        return result

    def valid_position(self, posx, posy):
        return posx < self.xsize and posx >= 0 and posy < self.ysize and posy >= 0
    
    def check_next_square_match(self, player, newx, newy):
        if self.valid_position(newy, newx):
            square = self.board[newx][newy]
            return square.occupied() and square.get_player().equal(player)
        return False

    def start_scan_for_goal(self, player, xcurrent, ycurrent, foundcount):
        logging.debug("start scan: (player: %s  xcurrent: %d  ycurrent: %d  foundcount: %d)", repr(player), xcurrent, ycurrent, foundcount)
        #Assumptions, we only need to look to down directions, since we are scanning down and right.
        #Sweep left to right below first
        newx = xcurrent+1
        for newy in range(ycurrent-1,ycurrent+2):
            if self.check_next_square_match(player, newx, newy):
                result = self.seek_goal(player, newx, newy, foundcount+1, 1, newy-ycurrent)
                if result is not None:
                    return result
        #Now handle across if ycurrent == starts far enough left (since we're only doing straight lines)
        if ycurrent <= self.ysize-self.goal:
            newy = ycurrent+1
            newx = xcurrent
            if self.check_next_square_match(player, newx, newy):
                result = self.seek_goal(player, newx, newy, foundcount+1, 0, newy-ycurrent)
                if result is not None:
                    return result
        return None

    def seek_goal(self, player, xcurrent, ycurrent, foundcount, xdir, ydir):
        logging.debug("seek_goal: (player: %s  xcurrent: %d  ycurrent: %d  foundcount: %d  xdir: %d  ydir: %d)", repr(player), xcurrent, ycurrent, foundcount, xdir, ydir)
        #This method now traverses in a straight line to find the result.
        if foundcount == self.goal:
            logging.debug("found goal")
            return player
        newx = xcurrent + xdir
        newy = ycurrent + ydir
        if self.check_next_square_match(player, newx, newy):
            return self.seek_goal(player, newx, newy, foundcount+1, xdir, ydir)
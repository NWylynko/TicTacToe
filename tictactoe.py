

class TicTacToe:
    def __init__(self):
        #setups the grid
        self._grid = [[None, None, None], [None, None, None], [None, None, None]]

    def getIndexOfPosition(self, position):
        #kinda returns an x and y position on the grid
        self.positions = {
                    0:(0, 0), 1:(0, 1), 2:(0, 2),
                    3:(1, 0), 4:(1, 1), 5:(1, 2),
                    6:(2, 0), 7:(2, 1), 8:(2, 2)}

        return(self.positions[position])

    def makeMove(self, position, player):
        #updates the position with either an X or an O
        self._grid[self.getIndexOfPosition(position)[0]][self.getIndexOfPosition(position)[1]] = player

    def printGrid(self):
        #prints out the grid
        for i in range(3):
            print(self._grid[i])

    def playGame(self):
        #runs the game
        self.Won = False
        self.currentPlayer = "X"

        while self.Won == False:
            #kepps running until someone wins or a draw
            self.printGrid()
            print("You must enter a number between 0 and 8!")
            self.move = 10
            #if they player enters a number above 8 they will just be told to enter another number
            while self.move > 8:
                self.move = int(input("Player "+ str(self.currentPlayer) +" Move: "))
            self.makeMove(self.move, self.currentPlayer)

            #swaps the currentPlayer after the currentPlayer has said what they want to do
            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"

game = TicTacToe()
game.playGame()

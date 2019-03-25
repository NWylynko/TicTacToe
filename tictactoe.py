

class TicTacToe:
    def __init__(self):
        self.grid = [[None, None, None], [None, None, None], [None, None, None]]

    def getIndexOfPosition(self, position):
        self.positions = {
                    0:(0, 0), 1:(0, 1), 2:(0, 2),
                    3:(1, 0), 4:(1, 1), 5:(1, 2),
                    6:(2, 0), 7:(2, 1), 8:(2, 2)}

        return(self.positions[position])

    def makeMove(self, position, player):
        self.grid[self.getIndexOfPosition(position)[0]][self.getIndexOfPosition(position)[1]] = player

    def printGrid(self):
        for i in range(3):
            print(self.grid[i])

    def playGame(self):

        self.Won = False
        self.currentPlayer = "X"

        while self.Won == False:
            self.printGrid()
            print("You must enter a number between 0 and 8!")
            self.move = int(input("Player "+ str(self.currentPlayer) +" Move: "))
            self.makeMove(self.move, self.currentPlayer)

            if self.currentPlayer == "X":
                self.currentPlayer = "O"
            else:
                self.currentPlayer = "X"

game = TicTacToe()
game.playGame()

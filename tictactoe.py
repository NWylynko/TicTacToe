

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
        if position > 8:
            return "position to high"
        elif self._grid[self.getIndexOfPosition(position)[0]][self.getIndexOfPosition(position)[1]] == None:
            self._grid[self.getIndexOfPosition(position)[0]][self.getIndexOfPosition(position)[1]] = player
            return "success"
        else:
            return "fail"

    def printGrid(self):
        #prints out the grid
        print("------------------")
        print("-----TicTacToe----")
        print("------------------")
        for i in range(3):
            print(self._grid[i])
        print("------------------")

    def checkWinner(self):
        #checks if a player has won

        for i in range(3):

            #checks horizontal (-)
            if self._grid[i][0] == "X" and self._grid[i][1] == "X" and self._grid[i][2] == "X":
                return "X"
            if self._grid[i][0] == "O" and self._grid[i][1] == "O" and self._grid[i][2] == "O":
                return "O"

            #checks virticle (|)
            if self._grid[0][i] == "X" and self._grid[1][i] == "X" and self._grid[2][i] == "X":
                return "X"
            if self._grid[0][i] == "O" and self._grid[1][i] == "O" and self._grid[2][i] == "O":
                return "O"

            #checks diagonals (/)
            if self._grid[0][0] == "X" and self._grid[1][1] == "X" and self._grid[2][2] == "X":
                return "X"
            if self._grid[0][0] == "O" and self._grid[1][1] == "O" and self._grid[2][2] == "O":
                return "O"

            #checks diagonals (\)
            if self._grid[2][0] == "X" and self._grid[1][1] == "X" and self._grid[1][2] == "X":
                return "X"
            if self._grid[2][0] == "O" and self._grid[1][1] == "O" and self._grid[1][2] == "O":
                return "O"

        draw = 0
        if self._grid[i][i] != None:
            draw += 1

        if draw == 8:
            return "draw"

        return "no winner"


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

                if self.makeMove(self.move, self.currentPlayer) == "success":
                    #checks to see if a player has Won
                    if self.checkWinner() == "X":
                        self.Won = "X"
                        self.printGrid()
                        print("-----")
                        print("X Won")
                        print("-----")
                    elif self.checkWinner() == "O":
                        self.Won = "O"
                        self.printGrid()
                        print("-----")
                        print("O Won")
                        print("-----")
                    elif self.checkWinner() == "draw":
                        self.Won = "X"
                        self.printGrid()
                        print("----")
                        print("Draw")
                        print("----")
                    #swaps the currentPlayer after the currentPlayer has said what they want to do
                    if self.currentPlayer == "X":
                        self.currentPlayer = "O"
                    else:
                        self.currentPlayer = "X"

                elif self.makeMove(self.move, self.currentPlayer) == "position to high":
                    print("You must enter a number between 0 and 9!")

                else:
                    print("That Place is taken")
game = TicTacToe()
game.playGame()

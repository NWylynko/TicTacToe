from tkinter import *
m = Tk()
m.title("TicTacToe")
class TicTacToe:
    def __init__(self):
        #remembers scores between games
        self.scores = {"playerXWins": 0, "playerOWins": 0, "draws": 0}
        self.setup()
        #buttons for all
        self.buttons = []
        #gets players names
        self.Label1 = Label(m, text='Player X')
        self.Label2 = Label(m, text='Player O')

        self.Label1.grid(row=0, column=0)
        self.Label2.grid(row=1, column=0)

        self.playerXLabel = Entry(m)
        self.playerOLabel = Entry(m)

        self.playerXLabel.grid(row=0, column=1)
        self.playerOLabel.grid(row=1, column=1)



        self.startButton = Button(m, text='Start', width=20, fg="black", command=self.playGame)
        self.startButton.grid(row=2, column=1)

        mainloop()
    def setup(self):
        #setups the grid
        self._grid = [[None, None, None], [None, None, None], [None, None, None]]

    def getCurrentPlayersName(self, player):
        #returns the names of the players
        if player == "X":
            return self.playerX
        elif player == "O":
            return self.playerO
        else:
            return "error"

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

    def updategrid(self, i):
        self.move = i
        print(i, self.move)
        for i in range(3):
            print(self._grid[i])

    def printGrid(self):
        #prints out the grid
        Label(m, text=self.getCurrentPlayersName(self.currentPlayer) + "'s turn").grid(row=0, column=1)
        Button(m, text="0", width=3, command= lambda: self.updategrid(0)).grid(row=1, column=0)
        Button(m, text="1", width=3, command= lambda: self.updategrid(1)).grid(row=1, column=1)
        Button(m, text="2", width=3, command= lambda: self.updategrid(2)).grid(row=1, column=2)
        Button(m, text="3", width=3, command= lambda: self.updategrid(3)).grid(row=2, column=0)
        Button(m, text="4", width=3, command= lambda: self.updategrid(4)).grid(row=2, column=1)
        Button(m, text="5", width=3, command= lambda: self.updategrid(5)).grid(row=2, column=2)
        Button(m, text="6", width=3, command= lambda: self.updategrid(6)).grid(row=3, column=0)
        Button(m, text="7", width=3, command= lambda: self.updategrid(7)).grid(row=3, column=1)
        Button(m, text="8", width=3, command= lambda: self.updategrid(8)).grid(row=3, column=2)

        mainloop()
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

            #checks diagonals (\)
            if self._grid[0][0] == "X" and self._grid[1][1] == "X" and self._grid[2][2] == "X":
                return "X"
            if self._grid[0][0] == "O" and self._grid[1][1] == "O" and self._grid[2][2] == "O":
                return "O"

            #checks diagonals (/)
            if self._grid[2][0] == "X" and self._grid[1][1] == "X" and self._grid[0][2] == "X":
                return "X"
            if self._grid[2][0] == "O" and self._grid[1][1] == "O" and self._grid[0][2] == "O":
                return "O"

        draw = 0
        if self._grid[i][i] != None:
            draw += 1

        if draw == 8:
            return "draw"

        return "no winner"


    def playGame(self):

        self.playerX = self.playerXLabel.get()
        self.playerO = self.playerOLabel.get()

        #remove widgets
        self.playerXLabel.grid_remove()
        self.Label1.grid_remove()
        self.playerOLabel.grid_remove()
        self.Label2.grid_remove()
        self.startButton.grid_remove()

        #runs the game
        self.Won = False
        self.currentPlayer = "X"

        while self.Won == False:
            #kepps running until someone wins or a draw
            self.printGrid()
            if self.makeMove(self.move, self.currentPlayer) == "success":
                #checks to see if a player has Won
                if self.checkWinner() == "X":
                    self.Won = "X"
                    self.printGrid()
                    self.scores["playerXWins"] += 1
                    print(self.playerX + " Won")
                    print(self.getCurrentPlayersName("X") + ": " + str(self.scores["playerXWins"]) + ", " + self.getCurrentPlayersName("O") + ": " + str(self.scores["playerOWins"]) + ", Draws: " + str(self.scores["draws"]))
                elif self.checkWinner() == "O":
                    self.Won = "O"
                    self.printGrid()
                    self.scores["playerOWins"] += 1
                    print(self.playerO + " Won")
                    print(self.getCurrentPlayersName("X") + ": " + str(self.scores["playerXWins"]) + ", " + self.getCurrentPlayersName("O") + ": " + str(self.scores["playerOWins"]) + ", Draws: " + str(self.scores["draws"]))
                elif self.checkWinner() == "draw":
                    self.Won = "X"
                    self.printGrid()
                    self.scores["draws"] += 1
                    print("Draw")
                    print(self.getCurrentPlayersName("X") + ": " + str(self.scores["playerXWins"]) + ", " + self.getCurrentPlayersName("O") + ": " + str(self.scores["playerOWins"]) + ", Draws: " + str(self.scores["draws"]))
                #swaps the currentPlayer after the currentPlayer has said what they want to do
                if self.currentPlayer == "X":
                    self.currentPlayer = "O"
                else:
                    self.currentPlayer = "X"
game = TicTacToe()

playAgain = True

while playAgain == True:
    askPlayAgain = input("Play Again? (sure/nah) ")
    if askPlayAgain == "sure":
        game.setup()
    else:
        playAgain = False

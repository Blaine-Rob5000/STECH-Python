"""
Student:  Robin G. Blaine
Date:     November 14, 2017
Class:   _Python Programming

Assignment (Module 3, Chapter 9, Project 10):
Write a GUI-based program that allows the user to play a game of tic-tac-toe
with the computer. The main window should display a 3 by 3 grid of empty
buttons. When the user presses an empty button, an X should appear.  The
computer should then respond by checking for a winner, then placing an O on
an empty button if there is no winner. The computer should then check for a
winner again. A RESET button shouuld reset the game and the window to their
initial state. Allow the computer to place it's mark on a randomly chosen
button.

v2.0: added checkbutton to turn on/off smart moves for the computer
"""

from tkinter import *
import random

class TicTacToe(Frame):
    """This class creates a GUI for a game of tic-tac-toe."""

    def __init__(self):
        """Initializes the variables and widgets."""

        Frame.__init__(self)
        self.master.title("Tic-Tac-Toe v2.0")
        self.master.resizable(False, False)
        self.grid(padx = 10, pady = 10)

        # variables to track the number of moves and the winner
        self._numMoves = 0
        self._winner = ""

        # player and computer tokens and an open space
        self._playerToken = "X"
        self._computerToken = "O"
        self._openSpace = ""

        # winner label
        self._winnerLabel = Label(self, text = self._winner, width = 15, relief = SUNKEN)
        self._winnerLabel.grid(row = 0, column = 0, columnspan = 3)

        # game buttons
        self._buttonMark = []
        self._gameButton = []
        for b in range(9):
            self._buttonMark.append(self._openSpace)
            self._gameButton.append(Button(self, text = self._buttonMark[b],
                command = lambda n = b: self._pressButton(n),
                width = 5))
            r = b // 3 + 1
            c = b % 3
            self._gameButton[b].grid(row = r, column = c)

        # Reset button
        self._resetButton = Button(self, text = "RESET",
            command = lambda: self._resetGame(),
            width = 5)
        self._resetButton.grid(row = 4, column = 0)

        # smart AI checkbox
        self._smartAI = BooleanVar()
        self._smartAICheck = Checkbutton(self, text = "Smart AI",
            variable = self._smartAI, onvalue = True, offvalue = False)
        self._smartAICheck.grid(row = 4, column = 1, columnspan = 2)


    def _pressButton(self, button):
        """The player places an X by pressing a button.
    button : integer from 0 to 9 indicating which button was pressed"""

        if self._winner == "" and self._buttonMark[button] == self._openSpace:
            self._buttonMark[button] = self._playerToken
            self._gameButton[button].configure(text = self._buttonMark[button])
            self._numMoves += 1
            if self._isWinner(self._playerToken):
                self._winner = "Player Wins!"
                self._winnerLabel.configure(text = self._winner)
            elif self._numMoves == 9:
                self._winner = "Tie!"
                self._winnerLabel.configure(text = self._winner)
            else:
                self._computerTurn()


    def _resetGame(self):
        """Resets the game."""

        self._winner = ""
        self._winnerLabel.configure(text = self._winner)
        self._numMoves = 0
        for b in range(9):
            self._buttonMark[b] = self._openSpace
            self._gameButton[b].configure(text = self._buttonMark[b])


    def _computerTurn(self):
        """The computer marks a random, unmarked button with an O."""

        if self._smartAI.get():
            computerMove = self._smartMove()
        else:
            computerMove = self._randomMove()
        self._buttonMark[computerMove] = self._computerToken
        self._gameButton[computerMove].configure(text = self._computerToken)
        self._numMoves += 1
        if self._isWinner(self._computerToken):
            self._winner = "Computer Wins!"
            self._winnerLabel.configure(text = self._winner)


    def _smartMove(self):
        """Returns a smart move for the computer."""

        # check for a winning move
        for move in range(9):
            if self._buttonMark[move] == self._openSpace:
                self._buttonMark[move] = self._computerToken
                if self._isWinner(self._computerToken):
                    return move
                else:
                    self._buttonMark[move] = self._openSpace

        # block a winning move by the player
        for move in range(9):
            if self._buttonMark[move] == self._openSpace:
                self._buttonMark[move] = self._playerToken
                if self._isWinner(self._playerToken):
                    return move
                else:
                    self._buttonMark[move] = self._openSpace

        # check to see if the center is a good move
        if self._isGoodMove(4):
            return 4

        possibleMoves = []

        # return a random selection from good corner moves (if any)
        for move in (0, 2, 6, 8):
            if self._isGoodMove(move):
                possibleMoves.append(move)
        if len(possibleMoves) > 0:
            move = random.choice(possibleMoves)
            return move

        # return a random selection from the remaining squares (if any)
        for move in (1, 3, 5, 7):
            if self._isGoodMove(move):
                possibleMoves.append(move)
        if len(possibleMoves) > 0:
            move = random.choice(possibleMoves)
            return move

        # if center is open, return that move
        if self._buttonMark[4] == self._openSpace:
            return 4

        # if any corners are open, return a random one
        for move in (1, 3, 5, 7):
            if self._buttonMark[4] == self._openSpace:
                possibleMoves.append(move)
            if len(possibleMoves) > 0:
                move = random.choice(possibleMoves)
                return move

        # return a random move
        return self._randomMove()


    def _isGoodMove(self, move):
        """Returns True if a move is open and gives 2 in a row with the 3rd space open;
returns False otherwise.
    move: integer from 0 to 9 representing one of the buttons"""

        # if the space is already used, return False
        if self._buttonMark[move] != self._openSpace:
            return False

        isGood = (self._openSpace, self._computerToken)

        # check rows
        r = move // 3
        if self._buttonMark[r] in isGood and \
           self._buttonMark[r + 1] in isGood and \
           self._buttonMark[r + 2] in isGood:
            return True

        # check columns
        c = move % 3
        if self._buttonMark[c] in isGood and \
           self._buttonMark[c + 3] in isGood and \
           self._buttonMark[c + 6] in isGood:
            return True

        # check upper-left to lower-right diagonal (if applicable)
        if move in (0, 4, 8):
            if self._buttonMark[0] in isGood and \
               self._buttonMark[4] in isGood and \
               self._buttonMark[8] in isGood:
                return True

        # check upper-right to lower-left diagonal (if applicable)
        if move in (2, 4, 6):
            if self._buttonMark[2] in isGood and \
               self._buttonMark[4] in isGood and \
               self._buttonMark[6] in isGood:
                return True

        # otherwise, return False
        return False


    def _randomMove(self):
        """Returns a random move for the computer."""

        openButtons = []
        for b in range(9):
            if self._buttonMark[b] == self._openSpace:
                openButtons.append(b)
        move = random.choice(openButtons)
        return move


    def _isWinner(self, token):
        """Returns True if the player with the submitted token has won, False otherwise
    token : a character ('X' for the player or 'O' for the computer)"""

        # check rows
        for r in range(3):
            if self._buttonMark[r * 3]     == token and \
               self._buttonMark[r * 3 + 1] == token and \
               self._buttonMark[r * 3 + 2] == token:
                return True

        # check columns
        for c in range(3):
            if self._buttonMark[c]     == token and \
               self._buttonMark[c + 3] == token and \
               self._buttonMark[c + 6] == token:
                return True

        # check top-left to bottom right diagonal
        if self._buttonMark[0] == token and \
           self._buttonMark[4] == token and \
           self._buttonMark[8] == token:
            return True

        # check top-right to bottom-left diagonal
        if self._buttonMark[2] == token and \
           self._buttonMark[4] == token and \
           self._buttonMark[6] == token:
            return True

        # return False if no win is found
        return False


def main():
    """The main function."""

    game = TicTacToe()
    game.mainloop()


main()

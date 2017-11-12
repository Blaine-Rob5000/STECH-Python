"""
Version 1.0

GUI program to roll dice for the Seventh Scion tabletop roleplaying game.

Written by: Robin G. Blaine on October 9, 2017
"""

import random
from tkinter import *

# Constant for legal sized dice
LEGAL = (12, 10, 8, 6, 4, 20)

# Constants for die positions
D12 = 0
D10 = 1
D8  = 2
D6  = 3
D4  = 4

class DiceRoller(Frame):
    """GUI dice roller main class."""
    def __init__(self):
        """Sets up the variables, window, and widgets."""
        Frame.__init__(self)
        self.master.title("Dice Roller")
        self.master.resizable(False, False)
        self.grid(padx = 10, pady = 10)

        # include d20 in roll?
        self._d20 = True
        self._d20CheckValue = BooleanVar()

        # set number of each die to 0
        self._d12 = 0
        self._d10 = 0
        self._d8  = 0
        self._d6  = 0
        self._d4  = 0

        # Advantage and Disadvantage degrees
        self._advantage = 0
        self._disadvantage = 0

        # do dice explode?
        self._exploding = True
        self._explodingCheckValue = BooleanVar()

        # Labels and +/- Buttons for each die
        self._d12Label = Label(self, text = "0d12", width = 18, relief = SUNKEN)
        self._d12Label.grid(row = 1, column = 0)
        self._d12PlusButton = Button(self, text = " + ",
                                     command = self._d12Plus)
        self._d12PlusButton.grid(row = 1, column = 1)
        self._d12MinusButton = Button(self, text = " - ",
                                      command = self._d12Minus)
        self._d12MinusButton.grid(row = 1, column = 2)

        self._d10Label = Label(self, text = "0d10", width = 18, relief = SUNKEN)
        self._d10Label.grid(row = 2, column = 0)
        self._d10PlusButton = Button(self, text = " + ",
                                     command = self._d10Plus)
        self._d10PlusButton.grid(row = 2, column = 1)
        self._d10MinusButton = Button(self, text = " - ",
                                      command = self._d10Minus)
        self._d10MinusButton.grid(row = 2, column = 2)

        self._d8Label = Label(self, text = "0d8", width = 18, relief = SUNKEN)
        self._d8Label.grid(row = 3, column = 0)
        self._d8PlusButton = Button(self, text = " + ",
                                    command = self._d8Plus)
        self._d8PlusButton.grid(row = 3, column = 1)
        self._d8MinusButton = Button(self, text = " - ",
                                     command = self._d8Minus)
        self._d8MinusButton.grid(row = 3, column = 2)

        self._d6Label = Label(self, text = "0d6", width = 18, relief = SUNKEN)
        self._d6Label.grid(row = 4, column = 0)
        self._d6PlusButton = Button(self, text = " + ",
                                    command = self._d6Plus)
        self._d6PlusButton.grid(row = 4, column = 1)
        self._d6MinusButton = Button(self, text = " - ",
                                     command = self._d6Minus)
        self._d6MinusButton.grid(row = 4, column = 2)

        self._d4Label = Label(self, text = "0d4", width = 18, relief = SUNKEN)
        self._d4Label.grid(row = 5, column = 0)
        self._d4PlusButton = Button(self, text = " + ",
                                    command = self._d4Plus)
        self._d4PlusButton.grid(row = 5, column = 1)
        self._d4MinusButton = Button(self, text = " - ",
                                     command = self._d4Minus)
        self._d4MinusButton.grid(row = 5, column = 2)

        # Advantage and Disadvantage degree Labels and +/- Buttons
        self._advantageLabel = Label(self, text = "Advantage: 0",
                                     width = 18, relief = SUNKEN)
        self._advantageLabel.grid(row = 6, column = 0)
        self._advantagePlusButton = Button(self, text = " + ",
                                           command = self._advantagePlus)
        self._advantagePlusButton.grid(row = 6, column = 1)
        self._advantageMinusButton = Button(self, text = " - ",
                                            command = self._advantageMinus)
        self._advantageMinusButton.grid(row = 6, column = 2)

        self._disadvantageLabel = Label(self, text = "Disadvantage: 0",
                                        width = 18, relief = SUNKEN)
        self._disadvantageLabel.grid(row = 7, column = 0)
        self._disadvantagePlusButton = Button(self, text = " + ",
                                              command = self._disadvantagePlus)
        self._disadvantagePlusButton.grid(row = 7, column = 1)
        self._disadvantageMinusButton = Button(self, text = " - ",
                                               command = self._disadvantageMinus)
        self._disadvantageMinusButton.grid(row = 7, column = 2)

        # Labels describing dice roll and for roll results; Roll and Reset buttons
        self._rollStringLabel = Label(self, text = "Rolling: d20", width = 60,
                                      anchor = W, relief = SUNKEN)
        self._rollStringLabel.grid(row = 9, column = 0, columnspan = 8)
        Label(self, text = "Result", width = 7).grid(row = 8, column =8, columnspan = 2)
        self._rollResultLabel = Label(self, text = "0", width = 7, relief = SUNKEN)
        self._rollResultLabel.grid(row = 9, column = 8, columnspan = 2)
        self._rollButton = Button(self, text = "Roll",
                                  command = self._roll, width = 7)
        self._rollButton.grid(row = 9, column = 10)
        self._resetButton = Button(self, text = "Reset",
                                  command = self._reset, width = 7)
        self._resetButton.grid(row = 9, column = 11)

        # blank label in column 3 for spacing
        self._spacerLabel = Label(self, text = "", width = 5)
        self._spacerLabel.grid(row = 0, column = 3)

        # d20 Checkbutton
        self._d20Check = Checkbutton(self, text = "Include d20",
                                     variable = self._d20CheckValue,
                                     onvalue = True, offvalue = False,
                                     command = lambda: self._refreshLabels())
        self._d20Check.grid(row = 0, column = 0, columnspan = 3)
        self._d20Check.select()

        # Exploding dice checkbutton
        self._explodingCheck = Checkbutton(self, text = "Exploding Dice",
                                           variable = self._explodingCheckValue,
                                           onvalue = True, offvalue = False,
                                           command = lambda: self._refreshLabels())
        self._explodingCheck.grid(row = 8, column = 0, columnspan = 3)
        self._explodingCheck.select()

        # rank selection buttons for automatic roll setup
        rank = 0
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        self._rank0Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(0))
        self._rank0Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank0Label = Label(self, text = "-", width = 10)
        self._rank0Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank0Label.configure(anchor = W)

        # rank 1
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank1Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(1))
        self._rank1Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank1Label = Label(self, text = rankText, width = 10)
        self._rank1Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank1Label.configure(anchor = W)

        # rank 2
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank2Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(2))
        self._rank2Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank2Label = Label(self, text = rankText, width = 10)
        self._rank2Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank2Label.configure(anchor = W)

        # rank 3
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank3Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(3))
        self._rank3Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank3Label = Label(self, text = rankText, width = 10)
        self._rank3Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank3Label.configure(anchor = W)

        # rank 4
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank4Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(4))
        self._rank4Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank4Label = Label(self, text = rankText, width = 10)
        self._rank4Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank4Label.configure(anchor = W)

        # rank 5
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank5Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(5))
        self._rank5Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank5Label = Label(self, text = rankText, width = 10)
        self._rank5Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank5Label.configure(anchor = W)

        # rank 6
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank6Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(6))
        self._rank6Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank6Label = Label(self, text = rankText, width = 10)
        self._rank6Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank6Label.configure(anchor = W)

        # rank 7
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank7Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(7))
        self._rank7Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank7Label = Label(self, text = rankText, width = 10)
        self._rank7Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank7Label.configure(anchor = W)

        # rank 8
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank8Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(8))
        self._rank8Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank8Label = Label(self, text = rankText, width = 10)
        self._rank8Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank8Label.configure(anchor = W)

        # rank 9
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank9Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(9))
        self._rank9Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank9Label = Label(self, text = rankText, width = 10)
        self._rank9Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank9Label.configure(anchor = W)

        # rank 10
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank10Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(10))
        self._rank10Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank10Label = Label(self, text = rankText, width = 10)
        self._rank10Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank10Label.configure(anchor = W)

        # rank 11
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank11Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(11))
        self._rank11Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank11Label = Label(self, text = rankText, width = 10)
        self._rank11Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank11Label.configure(anchor = W)

        # rank 12
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank12Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(12))
        self._rank12Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank12Label = Label(self, text = rankText, width = 10)
        self._rank12Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank12Label.configure(anchor = W)

        # rank 13
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank13Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(13))
        self._rank13Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank13Label = Label(self, text = rankText, width = 10)
        self._rank13Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank13Label.configure(anchor = W)

        # rank 14
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank14Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(14))
        self._rank14Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank14Label = Label(self, text = rankText, width = 10)
        self._rank14Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank14Label.configure(anchor = W)

        # rank 15
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank15Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(15))
        self._rank15Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank15Label = Label(self, text = rankText, width = 10)
        self._rank15Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank15Label.configure(anchor = W)

        # rank 16
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank16Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(16))
        self._rank16Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank16Label = Label(self, text = rankText, width = 10)
        self._rank16Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank16Label.configure(anchor = W)

        # rank 17
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank17Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(17))
        self._rank17Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank17Label = Label(self, text = rankText, width = 10)
        self._rank17Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank17Label.configure(anchor = W)

        # rank 18
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank18Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(18))
        self._rank18Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank18Label = Label(self, text = rankText, width = 10)
        self._rank18Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank18Label.configure(anchor = W)

        # rank 19
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank19Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(19))
        self._rank19Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank19Label = Label(self, text = rankText, width = 10)
        self._rank19Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank19Label.configure(anchor = W)

        # rank 20
        rank += 1
        gridRow = self._getRow(rank)
        gridCol = self._getCol(rank)
        rankText = diceString(False, dCode(rank), 0)
        self._rank20Button = Button(self, text = "Rank " + str(rank), width = 9,
                                   command = lambda: self._setDice(20))
        self._rank20Button.grid(row = gridRow, column = gridCol)
        gridCol += 1
        self._rank20Label = Label(self, text = rankText, width = 10)
        self._rank20Label.grid(row = gridRow, column = gridCol, sticky = W)
        self._rank20Label.configure(anchor = W)

    def _getRow(self, rank):
        return rank % 7 + 1

    def _getCol(self, rank):
        return rank // 7 * 3 + 4

    def _d12Plus(self):
        """Increments number of d12 to roll."""
        self._d12 += 1
        self._refreshLabels()

    def _d12Minus(self):
        """Decrements number of d12 to roll."""
        if self._d12 > 0:
            self._d12 -= 1
            self._refreshLabels()

    def _d10Plus(self):
        """Increments number of d10 to roll."""
        self._d10 += 1
        self._refreshLabels()

    def _d10Minus(self):
        """Decrements number of d10 to roll."""
        if self._d10 > 0:
            self._d10 -= 1
            self._refreshLabels()

    def _d8Plus(self):
        """Increments number of d8 to roll."""
        self._d8 += 1
        self._refreshLabels()

    def _d8Minus(self):
        """Decrements number of d8 to roll."""
        if self._d8 > 0:
            self._d8 -= 1
            self._refreshLabels()

    def _d6Plus(self):
        """Increments number of d6 to roll."""
        self._d6 += 1
        self._refreshLabels()

    def _d6Minus(self):
        """Decrements number of d6 to roll."""
        if self._d6 > 0:
            self._d6 -= 1
            self._refreshLabels()

    def _d4Plus(self):
        """Increments number of d4 to roll."""
        self._d4 += 1
        self._refreshLabels()

    def _d4Minus(self):
        """Decrements number of d4 to roll."""
        if self._d4 > 0:
            self._d4 -= 1
            self._refreshLabels()

    def _advantagePlus(self):
        """Increments the degree of Advantage."""
        self._advantage += 1
        self._refreshLabels()

    def _advantageMinus(self):
        """Decrements the degree of Advantage."""
        if self._advantage > 0:
            self._advantage -= 1
            self._refreshLabels()

    def _disadvantagePlus(self):
        """Increments the degree of Disadvantage."""
        self._disadvantage += 1
        self._refreshLabels()

    def _disadvantageMinus(self):
        """Decrements number of d4 to roll."""
        if self._disadvantage > 0:
            self._disadvantage -= 1
            self._refreshLabels()

    def _roll(self):
        """Displays the results of the selected roll."""
        dice = (self._d12, self._d10, self._d8, self._d6, self._d4)
        degree = self._advantage - self._disadvantage
        rollResult = rollDice(self._d20, dice, degree, self._exploding)
        self._rollResultLabel.configure(text = str(rollResult))

    def _reset(self):
        """Resets all fields except d20 and explode."""
        self._d12 = 0
        self._d10 = 0
        self._d8  = 0
        self._d6  = 0
        self._d4  = 0
        self._advantage = 0
        self._disadvantage = 0
        self._refreshLabels()
        self._rollResultLabel.configure(text = "0")

    def _setDice(self, rank):
        """Sets the d12, d10, d8, d6, and d4 fields to the submitted rank."""
        diceCode = dCode(rank)
        self._d12 = diceCode[0]
        self._d10 = diceCode[1]
        self._d8 = diceCode[2]
        self._d6 = diceCode[3]
        self._d4 = diceCode[4]
        self._refreshLabels()

    def _refreshLabels(self):
        """Refreshes the values in dice and Advantage/Disadvantage labels."""
        self._d20 = self._d20CheckValue.get()
        self._exploding = self._explodingCheckValue.get()
        self._d12Label.configure(text = str(self._d12)+"d12")
        self._d10Label.configure(text = str(self._d10)+"d10")
        self._d8Label.configure(text = str(self._d8)+"d8")
        self._d6Label.configure(text = str(self._d6)+"d6")
        self._d4Label.configure(text = str(self._d4)+"d4")
        self._advantageLabel.configure(text = "Advantage: " +
                                       str(self._advantage))
        self._disadvantageLabel.configure(text = "Disadvantage: " +
                                          str(self._disadvantage))
        dice = (self._d12, self._d10, self._d8, self._d6, self._d4)
        degree = self._advantage - self._disadvantage
        rollString = "Rolling: " + diceString(self._d20, dice, degree)
        self._rollStringLabel.configure(text = rollString)

# end DiceRoller class

def dCode(rank):
    """Returns the dice code for the submitted rank value.
        rank : non-negative integer"""
    if rank < 0:
        print("\nError: Rank cannot be less than zero.")
        return dCode(0)
    if rank == 0:
        return (0, 0, 0, 0, 0)
    if rank == 1:
        return (0, 0, 0, 0, 1)
    if rank == 2:
        return (0, 0, 0, 1, 0)
    if rank == 3:
        return (0, 0, 1, 0, 0)
    if rank == 4:
        return (0, 1, 0, 0, 0)
    d12 = (rank + 2) // 7
    d10 = 0
    d8  = 0
    d6  = 0
    d4  = 0
    remainder = (rank + 2) % 7
    if remainder in range(1, 6):
        d12 -= 1
    if remainder == 1:
        d6 = 2
    elif remainder == 2:
        d8 = 1
        d6 = 1
    elif remainder == 3:
        d8 = 2
    elif remainder == 4:
        d10 = 1
        d8 = 1
    elif remainder == 5:
        d10 = 2
    elif remainder == 6:
        d10 = 1
    return tuple((d12, d10, d8, d6, d4))

def diceString(d20, dice, degree):
    """Returns the string for the submitted dice.
        d20    : boolean
        dice   : die code (tuple of 5 non-negative integers)
        degree : integer; + for Advantage / - for Disadvantage"""
    result = ""
    sides = LEGAL[:-1]
    if len(dice) != len(sides):
        print("\nError: Invalid dice code.")
        return result
    dieStr = []
    for die in sides:
        dieStr.append("d" + str(die) + "+")
    if d20:
        result += "d20+"
    for n in range(5):
        if dice[n] == 1:
            result += "d" + str(sides[n]) + "+"
        elif dice[n] > 1:
            result += str(dice[n]) + "d" + str(sides[n]) + "+"
    result = result[:-1]
    if degree > 0:
        result += " w/Advantage " + str(degree)
    if degree < 0:
        result += " w/Disadvantage " + str(abs(degree))
    return result

def rollDice(d20, dice, degree, exploding):
    """Returns the results of the submitted roll.
        d20       : boolean
        dice      : die code (tuple of 5 non-negative integers)
        degree    : integer; + for Advantage / - for Disadvantage
        exploding : boolean"""
    total = 0
    sides = LEGAL[:-1]
    if len(dice) != len(sides):
        print("\nError: Invalid dice code.")
        return total
    for die in range(5):
        if dice[die] > 0:
            total += rollAdvantage(dice[die], sides[die], degree, exploding)
            degree = 0
    if d20:
        total += rollAdvantage(1, 20, degree, exploding)
    print("Final Roll:", total, "\n") # trace
    return total

def rollAdvantage(number, die, degree, exploding):
    """Returns the submitted roll with Advantage or Disadvantage.
        number    : non-negative integer
        die       : integer from LEGAL
        degree    : integer; + for Advantage / - for Disadvantage
        exploding : boolean"""
    dieResults = []
    total = 0
    if die not in LEGAL:
        print("\nError: d" + str(die) + " is not a legal die.")
        return total
    if die == 20 and degree != 0:
        degree = degree // abs(degree) # d20 Adv/Dis is max 1 degree
    for roll in range(0, int(number + abs(degree))):
        dieResults.append(random.randint(1, die))
    dieResults.sort()
    print(str(number) + "d%-2s" % str(die) + " Adv " + str(degree), "->",
          dieResults, end = " -> ") # trace
    if degree > 0:
        dieResults = dieResults[degree:]
        print(dieResults, end = " -> ") # trace
    elif degree < 0:
        dieResults = dieResults[:degree]
        print(dieResults, end = " -> ") # trace
    for roll in range(number):
        total += dieResults[roll]
        if dieResults[roll] == die and exploding:
            total += explode(die)
    print(total) # trace
    return total

def explode(die):
    """Returns the explosion for the submitted die.
        die : integer from LEGAL"""
    total = 0
    if die not in LEGAL:
        print("\nError: d" + str(die) + " is not a legal die.")
        return total
    roll = random.randint(1, die)
    total += roll
    if roll == die:
        total += explode(die)
    return total


def main():
    """Gets the dice rolling."""
    DiceRoller().mainloop()

main()

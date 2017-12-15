"""
Class:  	_Python Programming (ITEC 3001)
Assignment:	Final Project


GUI program to perform all sorts of dice rolls using dice of any size and exotic mechanics.

Written by: Robin G. Blaine on December ??, 2017


Notes:
http://python-gtk-3-tutorial.readthedocs.io/en/latest/Combobox.html
https://stackoverflow.com/questions/17757451/simple-ttk-combobox-demo
https://www.packtpub.com/mapt/book/application_development/9781785283758/1/ch01lvl1sec15/combo-box-widgets
http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-Combobox.html
http://www.tkdocs.com/tutorial/widgets.html
 - can be used for checkbuttons and entry fields as well!
"""

import random
from tkinter import *
from tkinter import ttk


class UltimateDiceRoller(Frame):
    """GUI dice roller main class."""
    def __init__(self):
        """Sets up the variables, window, and widgets."""
        Frame.__init__(self)
        self.master.title("Ultimate Dice Roller")
        self.grid(padx = 5, ipadx = 5, pady = 5, ipady = 5)
        
        # Initialize list variables for each row
        # Add to/Subtract from total (1 = add / -1 = subtract / 0 = does not factor into total)
        self._addSubtract = []
        
        # Number of Dice (non-negative integer)
        self._numberOfDice = []
        
        # Number of Sides (positive integer)
        self._numberOfSides = []
        
        # Explosion/Implosion
        self._explosionDepth = [] #  non-negative integer / 0 = none 
        self._explodeInfiniteChkVal = []
                
        self._implosionDepth = [] #  non-negative integer / 0 = none
        self._implodeInfiniteChkVal = []

        # Advantage and Disadvantage degrees (+ = adv / - = dis / 0 = none)
        self._advantageDegree = []
        
        # Dice-Pool/Success
        self._dicePoolChkVal = []
        self._successThreshold = [] # integer, default = average die roll
        self._succeedOverUnder = [] # + = over / - = under
        
        # Constant roll modifier
        self._modifier = [] # integer, adds to / subtracts from final roll
        
        # Custom content
        self._customOutputChkVal = []
        self._customOutputMinMax = [] # lowest and highest values for roll
        self._customOutputString = [] # each item is a list of strings
        
        # Individual Row Output
        self._rowOutput = []
        
        # Set up variables for each row (0 to 9)
        for row in range(10):
            # Add to/Subtract from total (1 = add / -1 = subtract / 0 = does not factor into total)
            self._addSubtract.append(1) # default is to add to overall total
        
            # Number of Dice (non-negative integer)
            self._numberOfDice.append(StringVar())
            self._numberOfDice[row].set("1")
            
            # Number of Sides (positive integer)
            self._numberOfSides.append(StringVar())
            self._numberOfSides[row].set("6")
            
            # Explosion/Implosion
            self._explosionDepth.append(StringVar()) #  non-negative integer / 0 = none 
            self._explodeInfiniteChkVal.append(BooleanVar())
            
            self._implosionDepth.append(StringVar()) #  non-negative integer / 0 = none
            self._implodeInfiniteChkVal.append(BooleanVar())
            
            # Advantage and Disadvantage degrees (+ = adv / - = dis / 0 = none)
            self._advantageDegree.append(StringVar())
            
            # Dice-Pool/Success
            self._dicePoolChkVal.append(BooleanVar())
            self._successThreshold.append(StringVar()) # integer, default = average die roll
            self._succeedOverUnder.append("+") # + = over / - = under
            
            # Constant roll modifier
            self._modifier.append(StringVar()) # integer, adds to/subtracts from final roll
            self._modifier[row].set("0")
            
            # Custom content
            self._customOutputChkVal.append(BooleanVar())
            self._customOutputMinMax.append([0, 0]) # lowest and highest values for roll
            self._customOutputString.append([]) # each item is a list of strings
            
            # Individual Row Output
            self._rowOutput.append("") # displays as a string
            
        # Combobox MAIN MENU (save, load, reset, show options)
        self._mainMenuSelection = StringVar()
        self._mainMenu = Menubutton(self, text = "Main Menu", relief = RAISED)
        self._mainMenu.menu = Menu(self._mainMenu, tearoff = 0)
        self._mainMenu["menu"] = self._mainMenu.menu
        
        self._mainMenu.menu.add_command(label = "Save Configuration") # command = 
        self._mainMenu.menu.add_command(label = "Load Configuration")
        self._mainMenu.menu.add_command(label = "Reset All Fields")
        
        self._showExplosionChkVal = BooleanVar()
        self._showImplosionChkVal = BooleanVar()
        self._showAdvantageChkVal = BooleanVar()
        self._showDicePoolChkVal = BooleanVar()
        self._showModifierChkVal = BooleanVar()
        self._showCustomOutputChkVal = BooleanVar()

        self._mainMenu.menu.add_checkbutton(label = "Show Explosion",     variable = self._showExplosionChkVal,    onvalue = True, offvalue = False)
        self._mainMenu.menu.add_checkbutton(label = "Show Implosion",     variable = self._showImplosionChkVal,    onvalue = True, offvalue = False)
        self._mainMenu.menu.add_checkbutton(label = "Show Advantage",     variable = self._showAdvantageChkVal,    onvalue = True, offvalue = False)
        self._mainMenu.menu.add_checkbutton(label = "Show Dice Pool",     variable = self._showDicePoolChkVal,     onvalue = True, offvalue = False)
        self._mainMenu.menu.add_checkbutton(label = "Show Modifier",      variable = self._showModifierChkVal,     onvalue = True, offvalue = False)
        self._mainMenu.menu.add_checkbutton(label = "Show Custom Output", variable = self._showCustomOutputChkVal, onvalue = True, offvalue = False)
        
        self._mainMenu.grid(row = 0, column = 0, columnspan = 4)
                        
        # Labels
        self._addSubtractLabel = Label(self, text = "+/-", width = 5)
        self._addSubtractLabel.grid(row = 2, column = 0)
        
        self._numberOfDiceLabel = Label(self, text = "# Dice", width = 10)
        self._numberOfDiceLabel.grid(row = 2, column = 1)
        
        self._numberOfSidesLabel = Label(self, text = "# Sides", width = 10)
        self._numberOfSidesLabel.grid(row = 2, column = 3)
        
        self._explosionLabel = Label(self, text = "Explosions", width = 15)
        self._explosionLabel.grid(row = 1, column = 4, columnspan = 2)
        self._explosionDepthLabel = Label(self, text = "Depth", width = 10)
        self._explosionDepthLabel.grid(row = 2, column = 4)
        
        self._explodeInfiniteLabel = Label(self, text = "Inf?", width = 5)
        self._explodeInfiniteLabel.grid(row = 2, column = 5)
        
        self._implosionLabel = Label(self, text = "Implosions", width = 15)
        self._implosionLabel.grid(row = 1, column = 6, columnspan = 2)
        self._implosionDepthLabel = Label(self, text = "Depth", width = 10)
        self._implosionDepthLabel.grid(row = 2, column = 6)
        
        self._implodeInfiniteLabel = Label(self, text = "Inf?", width = 5)
        self._implodeInfiniteLabel.grid(row = 2, column = 7)
        
        self._advantageDegreeLabel = Label(self, text = "Advantage", width = 10)
        self._advantageDegreeLabel.grid(row = 2, column = 8)
        
        self._dicePoolLabel = Label(self, text = "Dice Pool", width = 25)
        self._dicePoolLabel.grid(row = 1, column = 9, columnspan = 3)
        
        self._dicePoolOnLabel = Label(self, text = "On?", width = 5)
        self._dicePoolOnLabel.grid(row = 2, column = 9)
        
        self._successThresholdLabel = Label(self, text = "Threshold", width = 10)
        self._successThresholdLabel.grid(row = 2, column = 10)
        
        self._succeedOverUnderLabel = Label(self, text = "Over/Under", width = 10)
        self._succeedOverUnderLabel.grid(row = 2, column = 11)
        
        self._modifierLabel = Label(self, text = "Modifier", width = 10)
        self._modifierLabel.grid(row = 2, column = 12)
        
        self._customOutputLabel = Label(self, text = "Custom Output", width = 25)
        self._customOutputLabel.grid(row = 1, column = 13, columnspan = 2)
        
        self._customOutputOnLabel = Label(self, text = "On?", width = 5)
        self._customOutputOnLabel.grid(row = 2, column = 13)
        
        self._customOutputEditLabel = Label(self, text = "Edit", width = 15)
        self._customOutputEditLabel.grid(row = 2, column = 14)
        
        self._rowResultLabel = Label(self, text = "Individual Results", width = 20)
        self._rowResultLabel.grid(row = 2, column = 15)
        
        self._rowRollLabel = Label(self, text = "Roll", width = 10)
        self._rowRollLabel.grid(row = 2, column = 16)
        
        # Initialize widget lists
        self._addSubtractButton = [] # toggles between + / - / <blank>
        self._numberOfDiceEntry = [] # takes a non-negative integer
        self._numberOfSidesEntry = [] # takes a positive integer
        
        self._explosionDepthEntry = [] # non-negative integer
        self._explodeInfiniteCheckbutton = []
        self._explodeCombinedCheckbutton = []
        
        self._implosionDepthEntry = [] # takes a non-negative integer
        self._implodeInfiniteCheckbutton = []
        self._implodeCombinedCheckbutton = []
        
        self._advantageDegreeEntry = [] # takes a integer (+ = adv / - = dis / 0 = neither)
        
        self._dicePoolCheckbutton = []
        self._successThresholdEntry = [] # takes an integer in the die range
        self._succeedOverUnderButton = []
        
        self._modifierEntry = [] # takes an integer, adds to/subtracts from final roll
        
        self._customOutputCheckbutton = []
        self._customOutputEditCombobox = [] 
        
        self._rowOutputLabel = [] # non-editable label that shows results as a string
        
        self._rowRollButton = [] # rolls just that row
        
        # set up each row of widgets
        gridRow = 0
        for i in range(0, 10):
            gridRow = i + 3
            self._addSubtractButton.append(Button(self, text = "+", width = 2, command = lambda row = i : self.cycleAddSubtract(row)))
            self._addSubtractButton[i].grid(row = gridRow, column = 0)
            
            self._numberOfDiceEntry.append(Entry(self, textvariable = self._numberOfDice[i], width = 8, justify = CENTER))
            self._numberOfDiceEntry[i].grid(row = gridRow, column = 1)

            Label(self, text = "d").grid(row = gridRow, column = 2)
            
            self._numberOfSidesEntry.append(Entry(self, textvariable = self._numberOfSides[i], width = 8, justify = CENTER))
            self._numberOfSidesEntry[i].grid(row = gridRow, column = 3)
            
            self._explosionDepthEntry.append(Entry(self, textvariable = self._explosionDepth[i], width = 8, justify = CENTER))
            self._explosionDepthEntry[i].grid(row = gridRow, column = 4)
            
            self._explodeInfiniteCheckbutton.append(Checkbutton(self))
            self._explodeInfiniteCheckbutton[i].grid(row = gridRow, column = 5)
            
            self._implosionDepthEntry.append(Entry(self, textvariable = self._implosionDepth[i], width = 8, justify = CENTER))
            self._implosionDepthEntry[i].grid(row = gridRow, column = 6)
            
            self._implodeInfiniteCheckbutton.append(Checkbutton(self))
            self._implodeInfiniteCheckbutton[i].grid(row = gridRow, column = 7)
            
            self._advantageDegreeEntry.append(Entry(self, textvariable = self._advantageDegree[i], width = 8, justify = CENTER))
            self._advantageDegreeEntry[i].grid(row = gridRow, column = 8)
            
            self._dicePoolCheckbutton.append(Checkbutton(self))
            self._dicePoolCheckbutton[i].grid(row = gridRow, column = 9)
            
            self._successThresholdEntry.append(Entry(self, textvariable = self._successThreshold[i], width = 8, justify = CENTER))
            self._successThresholdEntry[i].grid(row = gridRow, column = 10)
            
            self._succeedOverUnderButton.append(Button(self, text = "+"))
            self._succeedOverUnderButton[i].grid(row = gridRow, column = 11)
            
            self._modifierEntry.append(Entry(self, textvariable = self._modifier[i], width = 8, justify = CENTER))
            self._modifierEntry[i].grid(row = gridRow, column = 12)
            
            self._customOutputCheckbutton.append(Checkbutton(self))
            self._customOutputCheckbutton[i].grid(row = gridRow, column = 13)
            
            self._customOutputEditCombobox.append(ttk.Combobox(self, width = 20))
            self._customOutputEditCombobox[i].grid(row = gridRow, column = 14)
            
            self._rowOutputLabel.append(Label(self, width = 16, relief = SUNKEN))
            self._rowOutputLabel[i].grid(row = gridRow, column = 15)
            
            self._rowRollButton.append(Button(self, text = "<- Roll", command = lambda row = i : self._rollRow(row)))
            self._rowRollButton[i].grid(row = gridRow, column = 16)
        
        self._combinedTotal = 0
        Label(self, text = "Combined Total", width = 20).grid(row = 13, column = 15)
        self._combinedTotalLabel = Label(self, width = 20, relief = SUNKEN)
        self._combinedTotalLabel.grid(row = 14, column = 15)
        self._combinedRollButton = Button(self, text = "Roll All", width = 16, command = lambda : self._rollAll())
        self._combinedRollButton.grid(row = 14, column = 14)
        
        self._average = [0, 0]
        Label(self, text = "Average Result", width = 20).grid(row = 15, column = 15)
        self._averageLabel = Label(self, width = 20, relief = SUNKEN)
        self._averageLabel.grid(row = 16, column = 15)
        self._clearAverageButton = Button(self, text = "Clear Average", width = 16)
        self._clearAverageButton.grid(row = 16, column = 14)

    def cycleAddSubtract(self, row):
        """Cycles the Add/Subtract button and variable for the given row."""
        if self._addSubtract[row] == 1:
            self._addSubtract[row] = -1
            self._addSubtractButton[row].configure(text = "-")
        elif self._addSubtract[row] == -1:
            self._addSubtract[row] = 0
            self._addSubtractButton[row].configure(text = "")
        else:
            self._addSubtract[row] = 1
            self._addSubtractButton[row].configure(text = "+")
            
    def _rollRow(self, row):
        """Rolls the dice for a single row."""
        num = int(self._numberOfDice[row].get())
        die = int(self._numberOfSides[row].get())
        mod = int(self._modifier[row].get())
        result = 0
        for roll in range(num):
            result += random.randint(1, die)
        result += mod
        self._rowOutput[row] = str(result)
        self._rowOutputLabel[row].configure(text = self._rowOutput[row])
        return result * self._addSubtract[row]
    
    def _rollAll(self):
        """Rolls and totals the dice for all rows."""
        result = 0
        for row in range(10):
            result += self._rollRow(row)
        self._combinedTotal = result
        self._combinedTotalLabel.configure(text = str(result))

def main():
            """Gets the dice rolling."""
            UltimateDiceRoller().mainloop()

main()

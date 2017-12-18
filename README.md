# Final Project for _Python Programming

By Robin G. Blaine

## Synopsis

This is a GUI program for rolling any number of dice with any number of sides with the option to include exotic dice-rolling mechanics such as explosions, implosions, advantage, dice pools, and custom output.

*Code Example*

The following is a sample of the code for rolling the die (or dice) on a single row:

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

*Motivation*

My motivations for this project go beyond merely completing a course assignment. I am an avid RPG gamer and many games use unusual dice (beyond the standard six polyhedrals: d4, d6, d8, d10, d12, and d20) and/or exotic mechanics that can makes rolls more complicated and time-consuming.  This program is intended to make a wide variety of dice rolls as quick and simple as a few clicks of the mouse.

*Installation*

Installation of the program only requires that the user run the UltimateDiceRoller.py file.

*API Reference*

<img src=”gui.png”/>

The program was more time-consuming than the alloted time for my project allowed for and, as such, is incomplete.  The GUI elements are all displayed but many are not yet functional.  

The main menu element is a drop-down list that has several (as-yet non-functional) options.  These include the option to save the current configuration of the dice roller and the option to load a saved configuration, as well as the option to reset all fields to their default values.

The main menu also contains (non-functional) checkbuttons to individually hide the GUI controls for the various exotic dice mechanics so that unused mechanics do not clutter the display or confuse the user.  After implementation, these options will allow the user to check or uncheck the option to display or hide the various mechanics.

The two rows below the main menu contain labels for the different GUI elements of the program.

The next ten rows contain the GUI elements that allow the user to set up rolls.  The first column is a button that cycles between "+" (the default), "-", and an empty string.  When the button displays the "+" symbol, that row will be added to the final total when the "Roll All" button is clicked.  When it displays "-", that row's results will be subtracted from the final total.  When the button is blank, that row's results will not be factored into the final total.

The second and fourth column all the user to enter the number of dice to roll for that row and the number of sides for those dice.  Between the two Entry fields is the letter "d", which is the standard notation for "die" in common gaming parlance.  (For example, "2d4" means "roll 2 4-sided dice and add them together.")

The next two columns allow the user to adjust the "exploding dice" options.  "Exploding" means that when a die rolls maximum, it is rolled again and added to the total.  "Explosion Depth" refers to the maximum number of extra rolls that may be scored.  If the "Inf?" Checkbutton is checked, then the die will be rolled and added until some result other than the maximum value is rolled.  A depth of 0 indicates that explosions will not be applied.
[This option is not yet implemented.]


The next two columns allow the user adjust the "imploding dice" options.  This is similar to "exploding dice," except that when the MINIMUM is rolled on the die, another die is rolled and subtracted.  If the new roll scores its maximum result, then another die is rolled and subtracted from the total until either the die rolls some number other than maximum or the maximum implosion depth is reached.

The next column contains an Entry field that allows the user to set the degree of Advantage or Disadvantage.  A positive value indicates the degree of Advantage, while a negative value indicates the degree of Disadvantage.  A value of 0 indicates that neither Advantage nor Disadvantage will be applied.  Advantage X (also called "best of") indicates that X number of extra dice (of the same type) will be rolled and the X number of dice that score the lowest will be discarded.  Disadvantage (or "worst of") is the opposite:  X extra dice are rolled and the X number that score the HIGHEST will be discarded.
[This option is not yet implemented.]
 
 
The next three columns control the "Dice Pool" options.  When rolling a Dice Pool, each die has a certain threshold which, if rolled causes the die to count as a single "success" added to the total.  For example, if rolling 3d10 with a success threshold of 7, each die that scores 7 or better counts as a single success.  A roll of 4, 5, and 8 would equal 1 success.  The first of these three columns is a Checkbutton to turn this option on or off.  The next is an Entry field that allows the user to input the threshold for a success.  The third column contains a button that toggles between "+" and "-".  If the button is set to "+", it indicates that a die must score equal to or greater than the threshold to count as a success.  If it is set to "-", then a die must score equal to or less than the threshold to count as a success.
[This option is not yet implemented.]
 
The next column is an Entry field that allows the user to define a constant modifier (a positive integer, a negative integer, or zero) that is added to the final roll on that row.
 
The next two columns allow the user to set each die for custom output.  The first column is a Checkbutton to turn on or off this option.  The next is a Combobox of Entry fields to assign a text value to each die result.
[This option is not yet implemented.]


The next column is a Label that displays the results of the dice rolled on that row.

The last column contains a button (labeled "<- Roll") that rolls the dice on that row only.

Below these rows, is a Label that displays the total roll for all of the dice rows and a button to roll and total all of the rows.

Finally, at the bottom of the GUI display, is a label to display the average of all previous rolls and a button to reset this value.
[This option is not yet implemented.]


*Tests*

The number, sides, and modifer for each row may be entered (click on the Entry widget and type in an appropriate integer) and the option to add, subtract, or ignore that row when calculating the final total all function.  After setting these options, the "<- Roll" buttons may be used to roll individual rows and the "Roll All" button may be used to roll all rows together and display the total.  The program still requires a great deal of work to complete, but, sadly, it falls beyond the scope of the time allowed for this project.  It is my intention to complete it on my own time at a later date.

*Contributors*

Individuals who wish to contribute to the project are free to do so. The program is incomplete and requires a great deal of work.  None of the main menu options are functioning as yet, and none of the exotic mechanics nor the averaging system have been implemented.

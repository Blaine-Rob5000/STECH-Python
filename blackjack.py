"""
Student:  Robin G. Blaine
Date:     November 8, 2017
Class:   _Python Programming

Assignment (Module 3, Chapter 9, Project 4):
  Write a GUI program that plays blackjack with the user.
  <Card and Deck classes are taken from student data files.>
"""

from tkinter import *
from cards import Card, Deck

class Blackjack(Frame):

    def __init__(self):
        
        Frame.__init__(self)
        
        self.master.title("Blackjack")
        self.grid()
        self._deck = Deck()
        self._backImage = PhotoImage(file = Card.BACK_NAME)
        self._blankImage = PhotoImage(file = "DECK\\blank.gif")

        self._dealerLabel = Label(self, text = "Dealer")
        self._dealerLabel.grid(row = 0, column = 0, columnspan = 2)

        self._dealerCardImage = []
        for x in range(10):
            self._dealerCardImage.append(Label(self, image = self._blankImage))
            self._dealerCardImage[x].grid(row = 1, column = x)

        self._statusLabel = Label(self, text = "Click NEW GAME to begin.")
        self._statusLabel.grid(row = 2, column = 0, columnspan = 2)

        self._playerCardImage = []
        for x in range(10):
            self._playerCardImage.append(Label(self, image = self._blankImage))
            self._playerCardImage[x].grid(row = 3, column = x)

        self._playerLabel = Label(self, text = "Player")
        self._playerLabel.grid(row = 4, column = 0, columnspan = 2)

        self._hitButton = Button(self, text = "Hit",
                                 command = self._hit)
        self._hitButton.config(width = 9)
        self._hitButton.grid(row = 4, column = 7)

        self._standButton = Button(self, text = "Stand",
                                   command = self._stand)
        self._standButton.config(width = 9)
        self._standButton.grid(row = 4, column = 8)

        self._newGameButton = Button(self, text = "New Game",
                                     command = self._newGame)
        self._newGameButton.config(width = 9)
        self._newGameButton.grid(row = 4, column = 9)

        self._playersTurn = False


    def _hit(self):
        if self._playersTurn:
            card = self._deck.deal()
            self._player.hit(card)
            n = len(self._player.getCards())
            self._playerCardImage[n].config(image = card.fileName)
            if self._player.getPoints == 21:
                self._stand()
            elif self._player.getPoints() > 21:
                self._playersTurn = False
                self._statusLabel.config(text = "You bust and lose.")


    def _stand(self):
        if self._playersTurn:
            self._playersTurn = False
            self._dealer.hit(self._deck)
            n = 0
            for card in self._dealer.getCards():
                self._dealerCardImage[n].configure(image = card.fileName)
                n += 1
            dealerPoints = self._dealer.getPoints()
            playerPoints = self._player.getPoints()
            if dealerPoints > 21:
                self._statusLabel.config(text = "Dealer busts.  You win.")
            elif dealerPoints < playerPoints and playerPoints <=21:
                self._statusLabel.config(text = "You win.")
            elif dealerPoints == playerPoints:
                if self._player.hasBlackjack() and not self._dealer.hasBlackjack():
                    self._statusLabel.config(text = "You win.")
                elif not self._player.hasBlackjack() and self._dealer.hasBlackJack():
                    self._statusLabel.config(text = "Dealer wins.")
                else:
                    self._statusLabel.config(text = "There is a tie.")

                    
    def _newGame(self):
        # initialize new game
        self._playersTurn = True
        self._statusLabel.config(text = "")
        self._deck = Deck()
        self._deck.shuffle()
        self._player = Player([self._deck.deal(), self._deck.deal()])
        self._dealer = Dealer([self._deck.deal(), self._deck.deal()])
        print(self._player) # trace
        print(self._dealer) # trace
        # clear card images
        for n in range(10):
            self._playerCardImage[n].config(image = self._blankImage)
            self._dealerCardImage[n].config(image = self._blankImage)
        # display player's cards
        n = 0
        for card in self._player.getCards():
            self._playerCardImage[n].config(image = card.fileName)
            n += 1
        # display dealer's face-up card and back of hole card
        card = self._dealer.getCards()[0]
        self._dealerCardImage[0].config(image = card.fileName)
        self._dealerCardImage[1].config(image = self._backImage)
        if self._player.hasBlackjack():
            self._dealer.hit()


class Player(object):
    """This class represents a player in a game of blackjack."""

    def __init__(self, cards):
        self._cards = cards

    def __str__(self):
        result = ", ".join(map(str, self._cards))
        result += "\n " + str(self.getPoints()) + " points"
        return result

    def hit(self, card):
        self._cards.append(card)

    def getPoints(self):
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        for card in self._cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def getCards(self):
        return self._cards

    def hasBlackjack(self):
        return len(self._cards) == 2 and self.getPoints() == 21


def Dealer(Player):
    """This class represents the dealer in a game of blackjack."""

    def __init__(self, cards):
        Player.__init__(self, cards)
        self._showOneCard = True

    def __str__(self):
        if self._showOneCard:
            return str(self._cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        self._showOneCard = False
        while self.getPoints() < 17:
            self._cards.append(deck.deal())


def main():
    game = Blackjack()
    game.mainloop()

main()

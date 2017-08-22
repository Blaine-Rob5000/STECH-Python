//STECH Java programming class
//Exercise 2-24
//Created by Robin G. Blaine on 8/22/2017
//display a random card value and suit from a 52 card deck

class Exercise_2_24 {
	public static void main(String[] args) {
		//generate a random card value
		int value = (int)(Math.random() * 13) + 1;
		
		//generate a random suit
		int suit = (int)(Math.random() * 4) + 1;

/*
begin debug

System.out.println(value);
System.out.println(suit);
System.out.println("");

end debug
*/
		
		//display the card value and suit
		System.out.print("Your card is the ");
		if (value == 1)
			System.out.print("Ace of ");
		else if (value == 2)
			System.out.print("Two of ");
		else if (value == 3)
			System.out.print("Three of ");
		else if (value == 4)
			System.out.print("Four of ");
		else if (value == 5)
			System.out.print("Five of ");
		else if (value == 6)
			System.out.print("Six of ");
		else if (value == 7)
			System.out.print("Seven of ");
		else if (value == 8)
			System.out.print("Eight of ");
		else if (value == 9)
			System.out.print("Nine of ");
		else if (value == 10)
			System.out.print("Ten of ");
		else if (value == 11)
			System.out.print("Jack of ");
		else if (value == 12)
			System.out.print("Queen of ");
		else if (value == 13)
			System.out.print("King of ");
		else
			System.out.print("Value Error! ");
		
		if (suit == 1)
			System.out.print("Clubs!");
		else if (suit == 2)
			System.out.print("Spades!");
		else if (suit == 3)
			System.out.print("Diamonds!");
		else if (suit == 4)
			System.out.print("Hearts!");
		else
			System.out.print("Suit Error!");
	}
}
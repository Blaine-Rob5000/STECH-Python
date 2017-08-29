//STECH Java programming class
//Exercise 8-11
//created by Robin G. Blaine on 8/29/2017
//input  - an integer from 0 to 511
//output - the corresponding setup of a 3x3 grid of coins from the Game: nine heads and tails


//imports
import java.util.Scanner;


public class Exercise_8_11 {
	public static void main(String[] args) {
		
		//create Scanner
		Scanner input = new Scanner(System.in);
		
		//declare array
		int[][][] gameState = new int[512][3][3];
		
		//define variables
		String stateString;
		
		//define values for each game state (0 = heads, 1 = tails)
		for (int state = 0; state < 512; state++) {
			for (int row = 0; row < 3; row++) {
				for (int column = 0; column < 3; column++) {
					stateString = convertToBinary(state);
					gameState[state][row][column] = (int)stateString.charAt(row * 3 + column) - 48;
				}	//end for (column)
			}	//end for (row)
		}	//end for (state)
		
		//choose a game state number and display the corresponding matrix
		System.out.print("Enter the game state to view (an integer number from 0 to 511): ");
		int stateNumber = input.nextInt();
		System.out.println("");
		
		//verify integer value is between 0 and 511
		if ((stateNumber < 0) || (stateNumber > 511)) {
			System.out.println("Error!  State number must be in the range of 0 to 511...");
			System.exit(0);
		}
		
		//display the chosen game state
		for (int row = 0; row < 3; row++) {
			for (int column = 0; column < 3; column++) {
				if (gameState[stateNumber][row][column] == 0)
					System.out.print("H ");
				else
					System.out.print("T ");
					//end if
			}	//end for (column)
			System.out.println("");
		}	//end for (row)
		
	}	//end main
	
	
	public static String convertToBinary(int number){
		
		String binaryString = Integer.toBinaryString(number);
		
		while (binaryString.length() < 9) {
			binaryString = "0" + binaryString;
			}	//end while
		
		return binaryString;
				
	}	//end convertToBinary
	
	
}	//end Exercise_8_11
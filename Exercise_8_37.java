//STECH Java programming class
//Exercise 8-37
//created by Robin G. Blaine on 8/29/2017
//input  - prompt the user to guess the capital of a state (not case-sensitive)
//output - the total number of correct guesses


//imports
import java.util.Scanner;


public class Exercise_8_37 {
	public static void main(String[] args) {
		
		//create Scanner
		Scanner input = new Scanner(System.in);
		
		//declare arrays
		String[][] stateAndCapital = new String[][] {
			{"Alabama",     "Montgomery"},
			{"Alaska",      "Juneau"},
			{"Arizona",     "Phoenix"},
			{"Arkansas",    "Little Rock"},
			{"California",  "Sacramento"},
			{"Colorado",    "Denver"},
			{"Connecticut", "Hartford"},
			{"Delaware",    "Dover"},
			{"Florida",     "Tallahassee"},
			{"Georgia",     "Atlanta"}
		};
		
		String[][] answer = new String[10][2];
		
		int numberOfCorrectAnswers = 0;		
		
				
		//cycle through the 10 states, prompt user to guess the capital, keep track of correct answers
		for (int stateNumber = 0; stateNumber < 10; stateNumber++) {
			System.out.print("Enter the capital of " + stateAndCapital[stateNumber][0] + ": ");
			answer[stateNumber][0] = input.nextLine();
			if (answer[stateNumber][0].toLowerCase().compareTo(stateAndCapital[stateNumber][1].toLowerCase()) == 0) {
				answer[stateNumber][1] = "Right    ";
				numberOfCorrectAnswers += 1;
			}
			else
				answer[stateNumber][1] = "Wrong    ";
				//end if
			
		}	//end for (stateNumber)
		
		//display the correct answers and number of correct guesses
		System.out.println("");
		
		for (int stateNumber = 0; stateNumber < 10; stateNumber++) {
			System.out.print(answer[stateNumber][1] + "State: ");
			System.out.printf("%-12s", stateAndCapital[stateNumber][0]);
			System.out.print("    Capital: ");
			System.out.printf("%-11s", stateAndCapital[stateNumber][1]);
			System.out.println("    Your answer: " + answer[stateNumber][0]);
		}	//end for (stateNumber)
		
		System.out.println("");
		
		System.out.println("Total correct answers: " + numberOfCorrectAnswers);
		
	}	//end main
		
}	//end Exercise_8_37
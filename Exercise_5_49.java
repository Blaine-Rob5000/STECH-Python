//STECH Java programming class
//Exercise 5-49
//created by Robin G. Blaine on 8/24/2017
//input  - user enters a string
//output - the number of consonants and vowells in the string


//imports
import java.util.Scanner;

public class Exercise_5_49 {
	public static void main(String[] args) {
	
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	
	//input string to anaylyze
	System.out.print("Enter a string to analyze: ");
	String userString = input.nextLine();
	userString = userString.toUpperCase();		//convert to uppercase
	int stringLength = userString.length();		//determine the string's length
	
	System.out.println("");
	System.out.println("");
	
	//count the vowels and consonants
	char character = ' '; 
	int numConsonants = 0;
	int numVowells = 0;
	
	for (int count = 0; count < stringLength; count++) {
		character = userString.charAt(count);
		if (((int) character >= 65) && ((int) character <= 90)) {
			switch(character) {
				case 'A': numVowells += 1; break;
				case 'E': numVowells += 1; break;
				case 'I': numVowells += 1; break;
				case 'O': numVowells += 1; break;
				case 'U': numVowells += 1; break;
				default:  numConsonants += 1;
				}	//end switch
			}	//end iff
		}	//end for loop
	
	//display the consonant and vowell counts
	System.out.println("Number of consonants: " + numConsonants);
	System.out.println("Number of vowells:    " + numVowells);
	}
}
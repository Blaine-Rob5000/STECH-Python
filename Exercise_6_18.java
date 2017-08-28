//STECH Java programming class
//Exercise 6-18
//created by Robin G. Blaine on 8/28/2017
//input  - user enters a password
//output - "Valid password" or "Invalid password"
//valid password must be at least 8 characters, must consist of only letters and digits, must contain at least 2 digits


//imports
import java.util.Scanner;

public class Exercise_6_18 {
	public static void main(String[] args) {
	
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	
	//input password to anaylyze
	System.out.println("Password rules: ");
	System.out.println("  1) Password must have at least eight characters.");
	System.out.println("  2) Password must consist only of letters and digits.");
	System.out.println("  3) Password must contain at least two digits.");
	System.out.println("");
	System.out.print("Enter password: ");
	String password = input.nextLine();
	System.out.println("");
	System.out.println("");
	
	
	//determine the password's length; generate error and end program if less than 8
	int pwLength = password.length();
	
	if (pwLength < 8) {
		System.out.println("Invalid password!  Must be at least 8 characters...");
		System.exit(0);
	}	//end if
	
		
	//count the letters and digits 
	int numLetters = 0;
	int numDigits  = 0;
	char character;
	
	
	for (int count = 0; count < pwLength; count++) {
		character = password.charAt(count);
		if (Character.isLetter(character))
			numLetters += 1;
		else if (Character.isDigit(character))
			numDigits += 1;
		else {
			System.out.println("Invalid password!  Can only contain letters and digits...");
			System.exit(0);
			}	//end if
		}	//end for loop

	
	//display valid or invalid password based on number of digits
	if (numDigits < 2)
		System.out.println("Invalid password!  Must contain at least two digits...");
	else
		System.out.println("Valid password.");
	}	//end main
}	//end Exercise_6_18
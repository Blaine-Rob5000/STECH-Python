//STECH Java programming class
//Exercise 3-26
//created by Robin G. Blaine on 8/22/2017
//input an integer and determine if it is divisible by:
//	5 and 6
//	5 or  6
//	5 xor 6

//imports
import java.util.Scanner;

public class Exercise_3_26 {
	public static void main(String[] args) {
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	//input an integer
	System.out.print("Enter an integer: ");
	
	int integer = input.nextInt();
	
	//determine if the integer is divisible by 5 and 6
	boolean fiveAnd   = ((integer / 5.0) == (int)(integer / 5.0));
	boolean sixAnd    = ((integer / 6.0) == (int)(integer / 6.0));
	boolean answerAnd = ((fiveAnd == true) && (sixAnd == true));
		
	//determine if the integer is divisible by 5 or 6
	boolean fiveOr   = ((integer / 5.0) == (int)(integer / 5.0));
	boolean sixOr    = ((integer / 6.0) == (int)(integer / 6.0));
	boolean answerOr = ((fiveOr == true) || (sixOr == true));
	
	//determine if the integer is divisible by 5 xor 6
	boolean fiveXor   = ((integer / 5.0) == (int)(integer / 5.0));
	boolean sixXor    = ((integer / 6.0) == (int)(integer / 6.0));
	boolean answerXor = ((fiveXor == true) ^ (sixXor == true));
	
	//display the results
	System.out.println("");
	System.out.println("  Is " + integer + " divisible by 5 and 6?                " + answerAnd);
	System.out.println("  Is " + integer + " divisible by 5 or 6?                 " + answerOr);
	System.out.println("  Is " + integer + " divisible by 5 or 6, but not both?   " + answerXor);
	}
}
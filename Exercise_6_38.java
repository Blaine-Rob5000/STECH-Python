//STECH Java programming class
//Exercise 6-38
//created by Robin G. Blaine on 8/28/2017
//input  - none
//output - 10 x 10 grid of uppercase characters, 10 x 10 grid of single digits
public class Exercise_6_38 {
	public static void main(String[] args) {
		
		char character;
		
		//print 10x10 grid of uppercase characters
		for (int row = 0; row < 10; row++) {
			for (int col = 0; col < 10; col++) {
				character = character('A', 'Z');
				System.out.print(character + " ");
			}	//end for (col)
			System.out.println("");
		}	//end for (row)
		System.out.println("");
		
		//print 10x10 grid of digits
		for (int row = 0; row < 10; row++) {
			for (int col = 0; col < 10; col++) {
				character = character('0', '9');
				System.out.print(character + " ");
			}	//end for (col)
			System.out.println("");
		}	//end for (row)
		
	}	//end main
	
	public static char character(char lowChar, char highChar) {
		return (char)(lowChar + Math.random() * (highChar - lowChar + 1));
	}	//end character
	
	
	
}	//end Exercise_6_38
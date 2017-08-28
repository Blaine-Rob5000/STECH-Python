//STECH Java programming class
//Exercise 7-15
//created by Robin G. Blaine on 8/28/2017
//input  - 10 numbers (stored to an array)
//output - index and value of smallest element in the array


//imports
import java.util.Scanner;


public class Exercise_7_15 {
	public static void main(String[] args) {
		//create Scanner
		Scanner input = new Scanner(System.in);
		
		//declare array
		int[] arrayOfNumbers = new int[10];
		
		//have the user input 10 numbers into the array
		System.out.println("Enter 10 integers:");
		for (int count = 0; count < 10; count++) {
			System.out.printf("% 5d", (count + 1));
			System.out.print(": ");
			arrayOfNumbers[count] = input.nextInt();
		}	//end for loop
		System.out.println("");
		
		//display the new array after elimiminating duplicates
		eliminateDuplicates(arrayOfNumbers);
		
	}	//end main
	
	
	public static void eliminateDuplicates(int[] oldArray){
		
		//declare array
		int[] newArray = new int[10];
		
		//declare variables
		boolean match = false;
		int newIndexMax = 0;
		
		//eliminate duplicates
		newArray[0] = oldArray[0];
		
		for (int index = 1; index < 10; index++) {
			for (int checkIndex = 0; checkIndex < index; checkIndex++) {
				if (oldArray[index] == newArray[checkIndex]) {
					match = true;
				}	//end if
				
			}	//end for
			if (!match) {
				newIndexMax += 1;
				newArray[newIndexMax] = oldArray[index];
			}	//end if
			
			match = false;
		}
		
		//display the new array
		System.out.print("The new array of numbers is:");
		for (int index = 0; index <= newIndexMax; index++) {
			System.out.print(" " + newArray[index]);
		}	//end for
		System.out.println("");
		
	}	//end eliminateDuplicates
	
	
}	//end Exercise_7_15
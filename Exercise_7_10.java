//STECH Java programming class
//Exercise 7-10
//created by Robin G. Blaine on 8/28/2017
//input  - 10 numbers (stored to an array)
//output - index and value of smallest element in the array


//imports
import java.util.Scanner;


public class Exercise_7_10 {
	public static void main(String[] args) {
		//create Scanner
		Scanner input = new Scanner(System.in);
		
		//declare array
		double[] arrayOfNumbers = new double[10];
		
		//have the user input 10 numbers into the array
		System.out.println("Enter 10 numbers:");
		for (int count = 0; count < 10; count++) {
			System.out.print("  Index " + count + ") ");
			arrayOfNumbers[count] = input.nextDouble();
		}	//end for loop
		System.out.println("");
		
		//display the smallest element's index and value
		int index = indexOfSmallestElement(arrayOfNumbers);
		System.out.println("The smallest element's index is: " + index);
		System.out.println("               And its value is: " + arrayOfNumbers[index]);
		
	}	//end main
	
	
	public static int indexOfSmallestElement(double[] array){
		
		//declare variables
		int smallestIndex = 0;
		
		//search for smallest
		for (int count = 0; count < 10; count++) {
			if (array[count] < array[smallestIndex])
				smallestIndex = count;
				//end if
		}	//end for
		
		return smallestIndex;
	}	//end indexOfSmallestElement
	
	
}	//end Exercise_7_10
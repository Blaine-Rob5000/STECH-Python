//STECH Java programming class
//Exercise 3-18
//Created by Robin G. Blaine on 8/22/2017
//input package weight and output cost to ship (or error if over 20 lbs)
//  0  < w <= 1    3.5
//  1  < w <= 3    5.5
//  3  < w <= 10   8.5
//  10 < w <= 20  10.5
//       w >  20  cannot ship

//import Scanner utility
import java.util.Scanner;

class Exercise_3_18 {
	public static void main(String[] args) {
		//create a Scanner object
		Scanner input = new Scanner(System.in);
		
		//prompt the user to enter distance, miles per gallon, and price per gallon
		System.out.println("Enter the package weight: ");
		double weight = input.nextDouble();
		System.out.println("");
		
		//output cost to ship the package
		if (weight < 0)
			System.out.println("Invalid weight. Please enter a value of 0 or greater...");
		
		else if (weight <= 1)
			System.out.println("The cost to ship is: $3.50");
		
		else if (weight <= 3)
			System.out.println("The cost to ship is: $5.50");
		
		else if (weight <= 10)
			System.out.println("The cost to ship is: $8.50");
		
		else if (weight <= 20)
			System.out.println("The cost to ship is: $10.50");
		
		else
			System.out.println("Too Heavy! The package cannot be shipped...");
	}
}
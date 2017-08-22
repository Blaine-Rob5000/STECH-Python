//STECH Java programming class
//Exercise 2-4
//Created by Robin G. Blaine on 8/22/2017
//input a number of pounds, convert to kilograms and display the result
//1 lb = .454 kg

//import Scanner utility
import java.util.Scanner;

class Exercise_2_4 {
	public static void main(String[] args) {
		//create a Scanner object
		Scanner input = new Scanner(System.in);
		
		//prompt the user to enter the number of pounds to convert to kilograms
		System.out.println("Enter the number of pounds to convert to kilograms: ");
		double numPounds = input.nextDouble();
		
		System.out.println("");
		System.out.println("That equals " + numPounds * .454 + " kilograms.");
	}
}
//STECH Java programming class
//Exercise 2-23
//Created by Robin G. Blaine on 8/22/2017
//input driving distance, miles per gallon, and price per gallon, output cost of trip

//import Scanner utility
import java.util.Scanner;

class Exercise_2_23 {
	public static void main(String[] args) {
		//create a Scanner object
		Scanner input = new Scanner(System.in);
		
		//prompt the user to enter distance, miles per gallon, and price per gallon
		System.out.println("Enter the distance driven: ");
		double distance = input.nextDouble();
		System.out.println("");
		
		System.out.println("Enter the number of miles per gallon: ");
		double efficiency = input.nextDouble();
		System.out.println("");
		
		System.out.println("Enter the price per gallon: ");
		double price = input.nextDouble();
		System.out.println("");
			
		//calculate and output cost of the trip
		double totalCost = (distance / efficiency * price);
		totalCost = Math.round(totalCost * 100.0) / 100.0;
		System.out.println("That total fuel cost is: $" + totalCost);
	}
}
//STECH Java programming class
//Exercise 2-13
//Created by Robin G. Blaine on 8/22/2017
//input an amount to deposit to savings each month into a savings account that earns 5% annual interest
//display the amount of money in the account after 6 months

//import Scanner utility
import java.util.Scanner;

class Exercise_3_18 {
	public static void main(String[] args) {
		//create a Scanner object
		Scanner input = new Scanner(System.in);
		
		//prompt the user to enter the amount to depost each month
		System.out.println("Enter the monthly deposit amount: ");
		double deposit = input.nextDouble();
		System.out.println("");
		
		//calculate the amount after 6 months at 5% interest
		double balance = 0.0;
		final double rate = 1.00417;
		
		balance = (balance + deposit) * rate;	//1 month
		balance = (balance + deposit) * rate;	//2 months
		balance = (balance + deposit) * rate;	//3 months
		balance = (balance + deposit) * rate;	//4 months
		balance = (balance + deposit) * rate;	//5 months
		balance = (balance + deposit) * rate;	//6 months
		
		//round and display balance
		balance = Math.round(balance * 100.0) / 100.0;
		System.out.println("Your total after 6 months is: $" + balance);

	}
}
//STECH Java programming class
//Exercise 5-30
//created by Robin G. Blaine on 8/24/2017
//input  - amount to be deposited each month to a savings account, the interest rate, and the number of months of saving
//output - account total after the specified number of months


//imports
import java.util.Scanner;

public class Exercise_5_30 {
	public static void main(String[] args) {
	
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	
	//input information
	System.out.print("Enter the amount to be deposited each month:    $");
	double depositAmount = input.nextDouble();
	
	System.out.print("Enter the yearly interest rate as a percentage: %");
	double yearlyInterestRate = input.nextDouble();
	yearlyInterestRate = yearlyInterestRate / 100.0;	//convert rate from percentage to a decimal
	
	System.out.print("Enter the number of months to calculate:         ");
	double numMonths = input.nextDouble();
	
	System.out.println("");
	System.out.println("");
	
	//calculate savings information
	double totalDeposit = depositAmount * numMonths;
	double monthlyInterestRate = yearlyInterestRate / 12.0;
	
	double accountBalance = 0;
	for (int count = 0; count < numMonths; count++) {
		accountBalance = accountBalance + depositAmount;
		accountBalance = Math.rint(accountBalance * (1.0 + monthlyInterestRate) * 100.0) / 100.0;
	
		System.out.println("Month " + (count + 1) + " ending balance: $" + accountBalance);
	
		}	//end for loop

	System.out.println("");
	
	double totalInterest = Math.rint((accountBalance - totalDeposit) *100.0) / 100.0;
	
	//display savings information
	System.out.println("Ending Balance:         $" + accountBalance);
	System.out.println("Total Interest Earned:  $" + totalInterest);
	}
}
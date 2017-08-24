//STECH Java programming class
//Exercise 4-23
//created by Robin G. Blaine on 8/24/2017
//input payroll information: employee name, hours worked in a week, hourly pay, federal tax rate, state tax rate
//output payroll statement: employee name, hours worked, pay rate, gross pay, deductions, net pay

//imports
import java.util.Scanner;

public class Exercise_4_23 {
	public static void main(String[] args) {
	
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	
	//input information
	System.out.print("Enter employee's name: ");
	String employee = input.nextLine();
	
	System.out.print("Enter the number of hours worked in the week: ");
	double hours = input.nextDouble();
	
	System.out.print("Enter the hourly pay rate: $");
	double payRate = input.nextDouble();
	
	System.out.print("Enter Federal tax withholding rate as a percentage: %");
	double fedRate = input.nextDouble();
	
	System.out.print("Enter State tax withholding rate as a percentage: %");
	double stateRate = input.nextDouble();
	
	System.out.println("");
	System.out.println("");
	
	//calculate payroll information
	double grossPay       = hours * payRate;
	double fedDeduction   = Math.round(grossPay * fedRate) / 100.0;
	double stateDeduction = Math.round(grossPay * stateRate) / 100.0;
	double totalDeduction = fedDeduction + stateDeduction;
	double netPay         = grossPay - totalDeduction;
	
	//display payroll information
	System.out.println("Employee Name: " + employee);
	System.out.println("Hours Worked: " + hours);
	System.out.println("Pay Rate:     $" + payRate);
	System.out.println("Gross Pay:    $" + grossPay);
	System.out.println("Deductions");
	System.out.println("  Federal Withholdings: $" + fedDeduction);
	System.out.println("  State Witholdings:    $" + stateDeduction);
	System.out.println("  Total Deductions:     $" + totalDeduction);
	System.out.println("");
	System.out.println("Net Pay: $" + netPay);
	}
}

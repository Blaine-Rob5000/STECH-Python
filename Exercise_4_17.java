//STECH Java programming class
//Exercise 4-17
//created by Robin G. Blaine on 8/24/2017
//input a year and the first letters of a month then display the number of days in that month

//imports
import java.util.Scanner;

public class Exercise_4_17 {
	public static void main(String[] args) {

	// declare array
	int[] monthDays;
	
	monthDays = new int[12];
	 
	monthDays[0] = 31;
	monthDays[1] = 28;
	monthDays[2] = 31;
	monthDays[3] = 30;
	monthDays[4] = 31;
	monthDays[5] = 30;
	monthDays[6] = 31;
	monthDays[7] = 31;
	monthDays[8] = 30;
	monthDays[9] = 31;
	monthDays[10] = 30;
	monthDays[11] = 31;
	
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	//input year and month
	System.out.print("Enter a year: ");
	int year = input.nextInt();
	
	System.out.println("");
	
	System.out.print("Enter the first three letters of a month: ");
	input.nextLine();	//consume leftover newline character
	String monthString = input.nextLine();
	
	//convert monthString to uppercase
	monthString = monthString.toUpperCase();
	
	//assign monthNumber a value based on monthString
	int monthNumber = 0;
	
	switch(monthString) {
		case "JAN": monthNumber = 0; monthString = "January"; break;
		case "FEB": monthNumber = 1; monthString = "February"; break;
		case "MAR": monthNumber = 2; monthString = "March"; break; 
		case "APR": monthNumber = 3; monthString = "April"; break;
		case "MAY": monthNumber = 4; monthString = "May"; break;
		case "JUN": monthNumber = 5; monthString = "June"; break;
		case "JUL": monthNumber = 6; monthString = "July"; break;
		case "AUG": monthNumber = 7; monthString = "August"; break;
		case "SEP": monthNumber = 8; monthString = "September"; break;
		case "OCT": monthNumber = 9; monthString = "October"; break;
		case "NOV": monthNumber = 10; monthString = "November"; break;
		case "DEC": monthNumber = 11; monthString = "December"; break;
		default: System.out.println("Error! Invalid month entry: " + monthString); System.exit(1);
		}	//end switch
	
	//assign the number of days
	int days = monthDays[monthNumber];
	
	//if month is February, check for leap year and add 1 day if true	
	if (monthNumber == 1) {
		if (year % 4 == 0)
			days = 29;								//add a day for leap year
		if ((year % 100 == 0) && (year % 400 != 0))
			days = 28;								//unless the year is divisible by 100 and not by 400		
		}
	
	//display the results
	System.out.println("");
	System.out.println("");
	System.out.println("The number of days in " + monthString + " of " + year + " is " + days);
	}
}

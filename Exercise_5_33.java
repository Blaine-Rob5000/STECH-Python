import javax.xml.parsers.*;

//STECH Java programming class
//Exercise 5-33
//created by Robin G. Blaine on 8/24/2017
//output - all perfect numbers below 10,000
//a perfect number is equal to the sum of all its divisors (excluding itself)


public class Exercise_5_33 {
	public static void main(String[] args) {
	
	//declare variables
	int total;
	
	//find the perfect numbers less than 10,000
	for (int number = 1; number < 10000; number++) {
		total = 0;
		int maxFactor = (int)(number / 2);
		for (int factor = 1; factor < (maxFactor + 1); factor++) {
			if (number % factor == 0)
				total = total + factor;
			}	//
		if (total == number)
			System.out.println(number + " is a perfect number.");
		}	//end outer for loop
	
	}
}
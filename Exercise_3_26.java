//STECH Java programming class
//Exercise 4-4
//created by Robin G. Blaine on 8/24/2017
//input the length of the side of a hexagon then calculate and display that hexagon's area

//imports
import java.util.Scanner;

public class Exercise_3_26 {
	public static void main(String[] args) {
	//create a Scanner
	Scanner input = new Scanner(System.in);
	
	//input an integer
	System.out.print("Enter the length of the hexagon's sides: ");
	
	double side = input.nextDouble();
	
	//calculate the area of the hexagon
	double area = 0;
	area = ((6.0 * Math.pow(side, 2.0) / (4.0 * Math.tan(Math.PI/6.0))));
	
	//display the results
	System.out.println("");
	System.out.println("The area of the hexagon is " + area);
	}
}

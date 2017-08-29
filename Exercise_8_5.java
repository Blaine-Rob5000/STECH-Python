//STECH Java programming class
//Exercise 8-5
//created by Robin G. Blaine on 8/29/2017
//


public class Exercise_8_5 {
	public static void main(String[] args) {
		
		//declare arrays
		double[][] matrix1 = {
			{1.0, 2.0, 3.0},
			{4.0, 5.0, 6.0},
			{7.0, 8.0, 9.0}
		};
		
		double[][] matrix2 = {
			{0.0, 2.0, 4.0},
			{1.0, 4.5, 2.2},
			{1.1, 4.3, 5.2}
		};
		
		double[][] matrixSum = new double[3][3];
		
		//add matrices
		matrixSum = addMatrix(matrix1, matrix2);
	
		//display the problem
		
		System.out.println("    Matrix 1      +     Matrix 2      =     Matrix 3");
		System.out.println(" -------------------------------------------------------");
		
		for (int row = 0; row < 3; row++) {
			for (int column = 0; column < 3; column++)
				System.out.printf("%, 5.1f", matrix1[row][column]);
				//end for (column)
			
			if (row == 1)
				System.out.print("   + ");
			else
				System.out.print("     ");
			
			
			for (int column = 0; column < 3; column++)
				System.out.printf("%, 5.1f", matrix2[row][column]);
				//end for (column)
			
			if (row == 1)
				System.out.print("   = ");
			else
				System.out.print("     ");
			
			for (int column = 0; column < 3; column++)
				System.out.printf("%, 5.1f", matrixSum[row][column]);
				//end for (column)
			
			System.out.println("");
			
		}	//end for (row)
		
	}	//end main
	
	
	public static double[][] addMatrix(double[][] a, double[][] b) {
		
		//check that matrices are the same size
		if ((a[0].length != b[0].length) || (a[1].length != b[1].length)) {
			System.out.println("Error!  Matrices are not the same size!");
			System.exit(0);
		}
		
		//declare sum array
		double[][] sumArray = new double[a[0].length][a[1].length];
		
		for (int row = 0; row < a[0].length; row++) {
			for (int column = 0; column < a[1].length; column++){
				sumArray[row][column] = a[row][column] + b[row][column];
			}	//end for (column)
		}	//end for (row)
		
		return sumArray;
		
	}	//end addMatrix
	
	
}	//end Exercise_8_5
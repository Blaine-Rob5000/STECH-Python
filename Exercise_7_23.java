//STECH Java programming class
//Exercise 7-23
//created by Robin G. Blaine on 8/28/2017
//locker puzzle
//100 students, 100 lockers
//all lockers begin closed (boolean false)
//student 1 (s1) starts at locker[1] and opens (boolean true) them all
//student 2 (s2) starts at locker[2] and closes every 2nd locker
//student 3 (s3) starts at locker[3] and changes every 3rd locker (close it if open, open it if closed)
//student 4 (s4) starts at locker[4] and changes every 4th locker
//etc...
//output - display the final state of all 100 lockers after all 100 students have passed through


public class Exercise_7_23 {
	public static void main(String[] args) {
		//declare array
		boolean[] lockerState  = new boolean[100];
		
		//assign false (closed) to all lockers
		for (int locker = 0; locker < 100; locker++) {
			lockerState[locker] = false;
		}	//end for
		
		for (int student = 0; student < 100; student++) {
			for (int locker = student; locker < 100; locker += (student + 1)) {
				lockerState[locker] = !lockerState[locker];
			}	//end for
		}	//end for
		
		//display all locker states
		for (int locker = 0; locker < 100; locker++) {
			System.out.print("Locker number: ");
			System.out.printf("% 4d", (locker + 1));
			System.out.print(" is ");
			if (lockerState[locker])
				System.out.println("open");
			else
				System.out.println("closed");
		}
	}	//end main
}	//end Exercise_7_23
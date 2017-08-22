//STECH Java programming class
//Exercise 1-4
//created by Robin G. Blaine on 8/22/2017
//show the average speed of a runner in kph, given distance (in miles) and time (in hours, minutes, and seconds)

class Exercise_1_12 {
	public static void main(String[] args) {
		System.out.println("Average speed in kilometers for a runner that runs 24 miles in 1 hour, 40 minutes, and 35 seconds is:");
		System.out.println("");
		System.out.println("    " + (24 * 1.6) / (1 + 40/60 + 35/(60*60)) + " kilometers per hour");
	}
}
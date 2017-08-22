class Exercise_1_12 {
	public static void main(String[] args) {
		System.out.println("Average speed in kilometers for a runner that runs 24 miles in 1 hour, 40 minutes, and 35 seconds is:");
		System.out.println("");
		System.out.println("    " + (24 * 1.6) / (1 + 40/60 + 35/(60*60)) + " kilometers per hour");
	}
}
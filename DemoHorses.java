//STECH Java programming class
//Exercise 11-Racehorse
//application DemoHorses.java
//created by Robin G. Blaine on 9/8/2017

/*
Write an application that demonstrates using objects of each of the following classes:

class Horse(name: String, color: String, birthYear: int)
	getName(): String
	getColor(): String
	getBirthYear(): int
	setName(name: String)
	setColor(color: String)
	setBirthYear(birthYear: int)
	
subclass RaceHorse(numberRacesCompeted: int)
	getNumberRacesCompeted(): int
	setNumberRacesCompeted(numberRacesCompeted: int)

Save the files as Horse.java, RaceHorse.java, and DemoHorses.java.
*/

public class DemoHorses {
		
	public static void main(String[] args) {		
		
		//demo Horse object
		Horse horse1 = new Horse("Charles", "Paint", 2010);
		System.out.println(" * * * * * horse1 information * * * * *");
		System.out.println("        Name: " + horse1.getName());
		System.out.println("       Color: " + horse1.getColor());
		System.out.println("  Birth Year: " + horse1.getBirthYear());
		System.out.println("");
		
		//demo RaceHorse object
		RaceHorse horse2 = new RaceHorse("Victoria", "Palamino", 2009, 13);
		System.out.println(" * * * * * horse2 information * * * * *");
		System.out.println("        Name: " + horse2.getName());
		System.out.println("       Color: " + horse2.getColor());
		System.out.println("  Birth Year: " + horse2.getBirthYear());
		System.out.println("  Number of Races Competed in: " + horse2.getNumberRacesCompeted());
		System.out.println("");
		
	}	//end main
		
}	//end application DemoHorses


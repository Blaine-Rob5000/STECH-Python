//STECH Java programming class
//Exercise 11-Racehorse
//subclass: RaceHorse
//created by Robin G. Blaine on 9/8/2017

/*
Create a subclass of Horse named RaceHorse, which contains an additional field that holds the number of races in which the horse has competed and additional methods to get and set the new field.

subclass RaceHorse(numberRacesCompeted: int)
	getNumberRacesCompeted(): int
	setNumberRacesCompeted(numberRacesCompeted: int)
*/

public class RaceHorse
	extends Horse {
	
	//variables
	private int numberRacesCompeted;
	
	//default constructor
	public RaceHorse() {
		
	}	//end default constructor
	
	//specified constructor (numberRacesCompeted)
	public RaceHorse(int numberRacesCompeted) {
		this.numberRacesCompeted = numberRacesCompeted;
	}	//end specified constructor (numberRacesCompeted)
	
	//specified constructor (name, color, birthYear, numberRacesCompeted)
	public RaceHorse (String name, String color, int birthYear, int numberRacesCompeted) {
		this.numberRacesCompeted = numberRacesCompeted;
		setName(name);
		setColor(color);
		setBirthYear(birthYear);
	}	//end specified constructor (name, color, birthYear, numberRacesCompeted)
	
	//get numberRacesCompeted
	public int getNumberRacesCompeted() {
		return numberRacesCompeted;
	}	//end getNumberRacesCompeted
	
}	//end subclass RaceHorse


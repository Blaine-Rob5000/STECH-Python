//STECH Java programming class
//Exercise 11-Racehorse
//class: Horse
//created by Robin G. Blaine on 9/8/2017

/*
Create a class named Horse that contains data fields for the name, color, and birthYear. Include get and set methods for these fields.

class Horse(name: String, color: String, birthYear: int)
	getName(): String
	getColor(): String
	getBirthYear(): int
	setName(name: String)
	setColor(color: String)
	setBirthYear(birthYear: int)

*/

public class Horse {
	
	//variables
	private String name;
	private String color;
	private int birthYear;
	
	//default constructor
	public Horse() {
		this.name = "";
		this.color = "";
		this.birthYear = 0;
	}	//end default constructor
	
	//specified constructor (name: String, color: String, birthYear: int)
	public Horse(String name, String color, int birthYear) {
		this.name = name;
		this.color = color;
		this.birthYear = birthYear;
	}	//end specified constructor (name: String, color: String, birthYear: int)
		
	//getter for name
	public String getName() {
		return this.name;
	}	//end getName
	
	//getter for color
	public String getColor() {
		return this.color;
	}	//end getColor
	
	//getter for birthYear
	public int getBirthYear() {
		return this.birthYear;
	}	//end getBirthYear
	
	//setter for name
	public void setName(String name) {
		this.name = name;
	}	//end setName
	
	//setter for color
	public void setColor(String color) {
		this.color = color;
	}	//end setCame
	
	//setter for birthYear
	public void setBirthYear(int birthYear) {
		this.birthYear = birthYear;
	}	//end setBirthYear
	
}	//end class Horse


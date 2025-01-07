import java.util.List;
import java.util.Arrays;
import java.util.Collections;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

import java.util.HashMap;
import java.util.Map;

import java.util.Comparator;



public class classExample {
	public static void main(String[] args) {
		Dog dog = new Dog();
		Cat cat = new Cat();
		Animal animal = new Animal();
		Animal polyDog = new Dog();
		Animal polyCat = new Cat();
		cat.setName("liang liang");
		dog.setName("snoopy");
		System.out.println("Animal name " + animal.getName());
		System.out.println("cat name " + cat.getName());
		System.out.println("Dog name " + dog.getName());
		System.out.println("Dog Type " + dog.getType());
		cat.setType("unknow");
		System.out.println("Dog Type " + dog.getType());
		cat.getDetails();
		System.out.println("toString: " + dog.toString());
		System.out.println("getClass: " + dog.getClass());
		// check if class can share a parameter like python
		// how to convert json to string and string to json in java
		// 
	}
}


class Animal{
	public String name = null;
	public static String type = "mammal";
	
	public void getDetails() {
		System.out.println("Details of animal");
	}
	
	public final int getDNA(){
		return 666666;
	}
	
	public String getName(){
		if (this.name != null) {
			return this.name;
		}
		else {
			return "Animal";
		}
	}
	
	public String getType(){
		return this.type;
	}
	
	public void setType(String type){
		this.type = type;
	}
	
	public void setName(String name){
		this.name = name;
	}
}


class Cat extends Animal {
	@Override
	public void getDetails(){
		System.out.printf("Details of %s", this.getClass().getName());
	}
}


class Dog extends Animal {
	
	@Override
	public void getDetails(){
		System.out.println("Detail of Dog");
	}

}




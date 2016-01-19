package com.exemplo.beersong;

public class BeerSong {

	public static void main(String[] args) {
		int beerNumber = 99;
		String word = "bootles";
		

		
		while (beerNumber > 0){
			
			
			if (beerNumber == 1){ 
				word ="bottle";
			}
				System.out.println(beerNumber + " " + word + " of beer on the wall");
				System.out.println(beerNumber + " " + word + " of beer");
				System.out.println("take on down");
				System.out.println("pass it around");
				
				beerNumber = beerNumber - 1;
				
				if (beerNumber > 0) {
					System.out.println(beerNumber + " " + word + " of beer on the wall");
				} else {
					System.out.println("nome more bootles of beer on the wall");
				}


			}
		}

}



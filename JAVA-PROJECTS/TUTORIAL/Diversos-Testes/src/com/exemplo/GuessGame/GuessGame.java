package com.exemplo.GuessGame;

public class GuessGame {

	Player p1;
	Player p2;
	Player p3;
	
	public void startGame(){
		p1 = new Player();
		p2 = new Player();
		p3 = new Player();
		
		int guessp1 = 0;
		int guessp2 = 0;
		int guessp3 = 0;
		
		boolean p1IsRight = false;
		boolean p2IsRight = false;
		boolean p3IsRight = false;
		
		int targetNumber = (int) (Math.random() * 10);
		System.out.println("estou pensando em um nº entre 0 e 9... ");
		
		while (true){
			System.out.println("O número a adinhar é " + targetNumber);
			
			p1.guess();
			p2.guess();
			p3.guess();
			
			guessp1 = p1.number;
			System.out.println("O jogador um forneceu o palipte " + guessp1);
			
			guessp2 = p2.number;
			System.out.println("O jogador dois forneceu o palipte " + guessp2);
			
			guessp3 = p3.number;
			System.out.println("O jogador três forneceu o palipte " + guessp3);
			
			
			if (guessp1 == targetNumber) {
				p1IsRight = true;
				
			}
			if (guessp2 == targetNumber) {
				p2IsRight = true;
				
			}
			if (guessp3 == targetNumber) {
				p3IsRight = true;
				
			}
			
			if (p1IsRight || p2IsRight || p3IsRight ) {
				System.out.println("Temos um vencedor");
				System.out.println("O jogador um acertou? " + p1IsRight);
				System.out.println("O jogador dois acertou? " + p2IsRight);
				System.out.println("O jogador três acertou? " + p3IsRight);
				System.out.println("Fim do jogo");
				break;
			} else {
				System.out.println("os jogadores terão que tentar novamente");
				
			}
		}
	}
}

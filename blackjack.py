import random
from random import shuffle
from typing import Dict, Type, List, Tuple, Generator

# Kartendeck erzeugen 
nr = "11 10 10 10 10 9 8 7 6 5 4 3 2".split()
card_types = "Pik Herz Kreuz Karo".split()
card_deck = [(num, farbe) for num in nr for farbe in card_types]


# Karten Stapel erzeugen
class card_stack:
    def __init__(self, card_deck: List[Tuple]) :
        self.card_deck  = card_deck
        self.card_generator: Generator[Tuple, None, None] = self.shuffle_deck()

    def shuffle_deck(self) -> None :
        shuffle(self.card_deck)
        for i in self.card_deck:
            yield i


# Class Spieler
class spieler:
    def __init__(self ):
        self.cards = []

    def draw_card(self, card_generator: Generator[Tuple, None, None], n: int ) -> None :
        for _ in range (n):
            self.cards.append(next(card_generator))

    def continue_turn(self) -> bool :
        answer = int(input("continue_turn type 1 else any number "))
        if answer == 1:
            return True
        else:
            return False
      

# Class Spiel
class Spiel:
    def __init__(self, dealer: Type[spieler], player: Type[spieler], card_stack: Type[card_stack]  = card_stack(card_deck)):
        self.dealer = dealer
        self.player = player
        self.card_generator: Generator[Tuple] = card_stack.card_generator

    def print_cards(self) -> None :
        return print(f"Dealer: {self.dealer.cards} , Player: {self.player.cards} ")

    def get_players_points(self,player) -> int:
        return sum(int(i) for i,j in player.cards)

    def print_results(self) -> None :
        if self.get_players_points(self.dealer) == 21:
            return ("Der  Dealer hat gewonnen")
        elif self.get_players_points(self.player) == 21:
            return ("Der Spieler  hat player")
        elif self.get_players_points(self.dealer) > 21:
            return ("Abbruch Dealer  ist über 21")
        elif self.get_players_points(self.player) > 21:
            return ("Abbruch Spieler  ist über 21")
        elif self.get_players_points(self.dealer) > self.get_players_points(self.player):
            return ("Der Dieler  hat gewonnen")
        elif self.get_players_points(self.dealer)  < self.get_players_points(self.player) :
            return ("Der Spieler  hat gewonnen")
        else:
            pass

    def game_ends(self) -> bool:
        if self.get_players_points(self.player) < 21 and  self.get_players_points(self.dealer)  <21:
            return False
        else:
            return True

    def players_turn(self) -> None:
        self.player.draw_card(self.card_generator, 1)
        self.print_cards()
        while   self.player.continue_turn() == True:
            self.player.draw_card(self.card_generator, 1)
            self.print_cards()
            if self.game_ends() == True :
                break

    def dealer_turn(self) -> None:
        self.dealer.draw_card(self.card_generator, 1)                 
        while   self.get_players_points(self.dealer)  <16 and self.game_ends() == False :
            self.dealer.draw_card(self.card_generator, 1)
    
    def main(self) -> None:   
        self.dealer.draw_card(self.card_generator, 1)      
        self.players_turn()
        if self.game_ends() == True :
            return print(self.print_results())   
        
        self.dealer_turn()   
        self.print_cards()
        print(self.print_results())   
        

x = Spiel(spieler(), spieler() )
x.main()
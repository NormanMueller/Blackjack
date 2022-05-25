import copy
from src.src.Blackjack_Game.Blackjack _Game.src.Blackjack_Game.Blackjack  import *
import pytest 
import unittest
from unittest.mock import Mock, patch,MagicMock
from unittest import mock
import builtins



class test_card_stack(unittest.TestCase):
    def setUp(self):
        self.card_stack  = card_stack(card_deck_init)


    def test_shuffle_deck_create_generator(self) -> None :
        #given 
        # #prints nur wenn der test nicht failed ;)
        init = copy.copy(card_deck_init)

        #when
        draw_card_from_generator = [next(self.card_stack.card_generator) for _ in range(len(init)) ]

        #then
        assert draw_card_from_generator != init
        assert len(draw_card_from_generator) == len(init)
        print(draw_card_from_generator[0:4], init[0:4])


class test_spieler(unittest.TestCase):

    def setUp(self):
        self.spieler  = spieler()
        self.spieler_2  = spieler()


    def test_draw_card(self) -> None:
        #given
        init = copy.copy(card_deck_init)
        generator = MagicMock()
        generator.__next__.side_effect  =  [(11, 'Herz'),(10, 'Herz'), (8, 'Kreuz') ]
        
        #when
        self.spieler.draw_card(generator,1)  
        self.spieler_2.draw_card(generator,1) 

       #then
        assert self.spieler.cards == [(11, 'Herz')]
        assert self.spieler_2.cards == [(10, 'Herz')]
        self.assertEqual(generator.__next__.call_count, 2)


    def test_continue(self) -> None:
        #with
        with mock.patch.object(builtins, 'input', lambda _: '1'):
        #thrn
            assert self.spieler.continue_turn() == True
    

    def test_no_continue(self) -> None:
        #with
        with mock.patch.object(builtins, 'input', lambda _: '0'):
        
        #thrn
            assert self.spieler.continue_turn() == False


class test_game(unittest.TestCase):
    def setUp(self):
        self.game = Game(spieler(), spieler())
        self.player = spieler()
    

    def test_get_players_points(self):
        #given
        self.player.cards =  [(11, 'Herz'),(10, 'Herz'), (8, 'Kreuz') ]

        #when
        points = self.game.get_players_points(self.player)

        #then
        assert  points == 29


    def test_game_ends_dealer(self):
        #given
        self.game.dealer.cards =  [(11, 'Herz'),(10, 'Herz'), (3, 'Kreuz') ]

        #when
        game_ends = self.game.game_ends()

        #then
        assert  game_ends == True


    def test_game_ends_player(self):
        #given
        self.game.player.cards =  [(11, 'Herz'),(8, 'Herz'), (3, 'Kreuz') ]

        #when
        game_ends = self.game.game_ends()

        #then
        assert  game_ends == True


    def test_game_continue(self):
        #given
        self.game.player.cards =  [(3, 'Herz'),(8, 'Herz'), (3, 'Kreuz') ]

        #when
        game_ends = self.game.game_ends()

        #then
        assert  game_ends == False


    def test_player_turn_continue(self):
        #given
         with patch('src.Blackjack_Game.Blackjack.spieler.draw_card') as mock_card, \
            patch('src.Blackjack_Game.Blackjack.spieler.continue_turn') as mock_continue:

            mock_continue.side_effect  =  [True,False ]

        #when
            self.game.players_turn()
        
        #then
            self.assertEqual(mock_card.call_count, 2)


    def test_player_turn_no_continuation(self):
        #given
         with patch('src.Blackjack_Game.Blackjack.spieler.draw_card') as mock_card, \
            patch('src.Blackjack_Game.Blackjack.spieler.continue_turn') as mock_continue:

            mock_continue.side_effect  =  [False ]

        #when
            self.game.players_turn()
        
        #then
            self.assertEqual(mock_card.call_count, 1)


    def test_player_turn_assert_card_1(self):
        #given
        with patch('src.Blackjack_Game.Blackjack.spieler.continue_turn') as mock_continue:

        #when
            mock_continue.side_effect  =  [False ]
            generator_mock = MagicMock()
            generator_mock.__next__.side_effect  =  [(11, 'Herz'),(10, 'Herz'), (8, 'Kreuz') ]
            self.game.card_generator = generator_mock

            self.game.players_turn()
        
        #then
            assert self.game.player.cards == [(11, 'Herz')]


    def test_player_turn_assert_card2(self):
        #given
        with patch('src.Blackjack_Game.Blackjack.spieler.continue_turn') as mock_continue:

        #when
            mock_continue.side_effect  =  [True ]
            generator_mock = MagicMock()
            generator_mock.__next__.side_effect  =  [(11, 'Herz'),(10, 'Herz'), (8, 'Kreuz') ]
            self.game.card_generator = generator_mock

            self.game.players_turn()
        
        #then
            assert self.game.player.cards == [(11, 'Herz'),(10, 'Herz')]

  
from blackjack import *
import pytest 



def test_mischen():
    kartendeck = ["11 Pik", "10 Pik", "9 Pik", "8 Pik"]
    karten = karten_stapel()
    karten.mischen(kartendeck)
    assert karten.kartendeck == kartendeck


import pytest
from project import Game

game = Game()
def test_get_words():
    assert game.get_words() != False

def test_choose_lang():
    assert game.choose_lang("ja") == True
    assert game.choose_lang("pjvs") == False

def test_tranlsate():
    assert game.translate_word("cat") == "猫"
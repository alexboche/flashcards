
import functools
import pathlib
import json


class Card:
    def __init__(self, front, back=None, side=None):
        self.front = front
        self.back = back
        self.side = side


    def __repr__(self):
        return f'Card(front={self.front}, back={self.back}, side={self.side})'

    def __str__(self):
        return ("front: %s\nback: %s\nside: %s" % (self.front, self.back, self.side))
    def __eq__(self, other):
        return self.as_dict() == other.as_dict()

    def as_dict(self):
        return {"front": self.front, "back": self.back, 
        "side": self.side}


def prep_dict_of_decks_for_json(dict_of_decks):
    dict_of_decks = dict_of_decks.copy()
    for deck_name, deck in dict_of_decks.items():
        deck = [card.as_dict() for card in deck] 
        dict_of_decks[deck_name] = deck
    return dict_of_decks

def unprep_dict_of_decks_for_json(dict_of_decks):
    for deck_name, deck in dict_of_decks.items():
        deck = [Card(**json_card) for json_card in deck]
        dict_of_decks[deck_name] = deck
    return dict_of_decks

def add_card_to_deck(card, deck, position_in_deck=None):
    deck = deck.copy()
    if position_in_deck == None:
        position_in_deck = len(deck)
    deck.insert(position_in_deck, card)
    return deck 

    
def add_deck_to_dict_of_decks(dict_of_decks, deck_name, deck):
    dict_of_decks = dict_of_decks.copy()
    dict_of_decks[deck_name] = deck
    return dict_of_decks

def save(dict_of_decks, filename):
    dict_of_decks = prep_dict_of_decks_for_json(dict_of_decks)
    with open(filename, "w") as f:
        json.dump(dict_of_decks, f)



def load(filename):
    with open(filename) as f:
        dict_of_decks = json.load(f)
        return unprep_dict_of_decks_for_json(dict_of_decks)

    
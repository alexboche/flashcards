
import functools
import pathlib
import json
import os

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

def build_card_and_add_to_deck(filename, deck_name, position, front, back, side):
        # load
        dict_of_decks = load(filename)
    
        # add
        card = Card(front, back, side)
        deck = dict_of_decks[deck_name]
        deck = add_card_to_deck(card, deck, position)
        dict_of_decks[deck_name] = deck
    
            # front = input("Front of card: ")  
            # back = input(Back of card)
        # Save
        save(dict_of_decks, filename)
    
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
    # basepath, _ = os.path.split(filename)
    basepath = os.path.dirname(filename)
    if not os.path.exists(basepath):
        os.makedirs(basepath)
    with open(filename, "w") as f:
        json.dump(dict_of_decks, f, indent=4)



def load(filename):
    try:
        with open(filename, 'r') as f:
            dict_of_decks = json.load(f)
    except FileNotFoundError:
        dict_of_decks = {}
    return unprep_dict_of_decks_for_json(dict_of_decks)
    
def view_card(deck, front_back_side):
    if deck == []:
        print("the deck called %s is empty" %deck)
        return
    if front_back_side == None:
        front_back_side = "front"
    dict_of_decks = load(filename)
    first_card = dict_of_decks[deck][0]
    if front_back_side == "front":
        print(f"front: {first_card.front}")
    if front_back_side == "back":
        print(f"back: {first_card.back}")
    if front_back_side == "side":
        print(f"side: {first_card.side}")

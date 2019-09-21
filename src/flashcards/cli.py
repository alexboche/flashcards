import click 
import os
from flashcards import flashcards_core
# with io.open(os.path.expanduser('~/debugout'), 'wb') as f:

# Approach using expanduser
data_dir = "flashcards_data"
filepath = os.path.expanduser(os.path.join("~", data_dir))
print(filepath)
f =   "flashcards.json"
filename = os.path.join(filepath, f)
print(filename)
print(os.path.expanduser("~"))

""" Approach relative to cli.py file location
abspath = os.path.abspath(__file__)
base = os.path.dirname(abspath)
print(base)
filepath = os.path.join(base, data_dir)
print(filepath)
filename = os.path.join(filepath, f)
print(filename)"""
# filepath, filename = os.path.split(filename)

# filename =   r"C:\Users\alex\programing\flashcards_project\src\flashcards\flashcards.json"
@click.group('flashcards')
def cli():
    'Command-line flashcards.'

@cli.command("add")
@click.option("--position", type=int, default=None)
@click.argument("deck_name")
@click.argument("front", required=False)
@click.argument("back", required=False)
@click.argument("side", required=False)
@click.option("--filename", default=filename)
def cli_add(filename, deck_name, position, front, back, side):
    if front == None:
        front = input("front: ")
    if back == None:
        back = input("back: ")
    flashcards_core.build_card_and_add_to_deck(filename, deck_name, position, front, back, side)


@cli.command("view")
@click.argument("deck")
@click.argument("front_back_side", required=False)
# @click.option("--filename", default=filename)
def cli_view_card(deck, front_back_side):
    flashcards_core.view_card(deck, front_back_side, filename)

    
@cli.command("create_deck")
@click.argument("deck")
def cli_create_deck(deck):
    dict_of_decks = flashcards_core.load(filename)
    
    if deck in dict_of_decks.keys():
        print("that deck already exists")
        return
    dict_of_decks[deck]=[]
    flashcards_core.save(dict_of_decks, filename)
    


@cli.command("move_current_card")
@click.argument("current_deck")
@click.option("--destination_deck", required=False)
@click.argument("position", type=int, required=False)
@click.option("--filename", required=False, default=filename)
def cli_move_current_card(current_deck, destination_deck, position, filename):  
    if destination_deck == None:
        destination_deck = current_deck
    if position == None:
        position = len(destination_deck)
    dict_of_decks = flashcards_core.load(filename)
    card = dict_of_decks[current_deck].pop(0)
    dict_of_decks[destination_deck].insert(position, card)
    flashcards_core.save(dict_of_decks, filename)



@cli.command('prompt')
def cli_prompt():
    """Prompt for input."""
    current_deck = input("What deck do you want to look at? \n ")
    while current_deck not in flashcards_core.load(filename) and current_deck != "":
        print(f"there is no deck named {current_deck}")
        current_deck = input("What deck do you want to look at? \n ")
    if current_deck == "":
        current_deck = "math"
    while True:
        action = input("What would you like to do? \n ")
        if action == "view":
            fbs = input("front, back or side? \n")
            flashcards_core.view_card(current_deck, fbs, filename)
        elif action == "move":
            pass
        elif action == "create card":
            front = input("front: ")
            back = input("back: ")
            card = flashcards_core.Card(front, back)
            # side
            # position = -1
            # position = input("position: ")
            flashcards_core.add_card_to_deck(card, current_deck)
            
        elif action == "exit":
            break
        # elif action == "change deck":
        #     current_deck = input("What deck do you want to look at?")




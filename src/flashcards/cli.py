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
@click.option("--position", type=int)
@click.argument("deck_name")
@click.argument("front")
@click.argument("back")
@click.argument("side", required=False)
@click.option("--filename", default=filename)
def cli_add(filename, deck_name, position, front, back, side):
    # load
    dict_of_decks = flashcards_core.load(filename)

    # add
    card = flashcards_core.Card(front, back, side)
    deck = dict_of_decks[deck_name]
    deck = flashcards_core.add_card_to_deck(card, deck, position)
    dict_of_decks[deck_name] = deck

        # front = input("Front of card: ")  
        # back = input(Back of card)
    # Save
    flashcards_core.save(dict_of_decks, filename)

@cli.command("view")
@click.argument("deck")
@click.argument("front_back_side", required=False)
# there has got to be a better way to do this. 
# You shouldn't need to reload the entire dict_of_decks 
# just to see the back of the card once you've seen the front
def cli_view_front(deck, front_back_side):
    if front_back_side == None:
        front_back_side = "front"
    dict_of_decks = flashcards_core.load(filename)
    first_card = dict_of_decks[deck][0]
    if front_back_side == "front":
        click.echo(f"front: {first_card.front}")
    if front_back_side == "back":
        click.echo(f"front: {first_card.back}")
    if front_back_side == "side":
        click.echo(f"front: {first_card.side}")
    


@cli.command("create_deck")
@click.argument("deck")
def cli_create_deck(deck):
    dict_of_decks = flashcards_core.load(filename)
    # TODO: handle the case where the deck already exists
    dict_of_decks[deck]=[]
    flashcards_core.save(dict_of_decks, filename)


@cli.command("move_current_card")
@click.argument("current_deck")
@click.option("--destination_deck", required=False)
@click.argument("position", type=int)
@click.option("--filename", required=False, default=filename)
def cli_move_current_card(current_deck, destination_deck, position, filename):  
    if destination_deck == None:
        destination_deck = current_deck
    dict_of_decks = flashcards_core.load(filename)
    card = dict_of_decks[current_deck].pop(0)
    dict_of_decks[destination_deck].insert(position, card)
    flashcards_core.save(dict_of_decks, filename)







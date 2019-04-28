import click 
from flashcards import flashcards_core

filename = r"C:\Users\Alex\flashcards.json"
@click.group('flashcards')
def cli():
    'Command-line flashcards.'

@cli.command("add")
@click.argument("position", type=int)
@click.argument("deck")
# @click.argument("filename")
# front back and side how to do this in a better way?
@click.argument("card_contents", nargs=3 ) # should I make nargs=-1
def cli_add(filename, deck, position, card_contents):
    # load
    dict_of_decks = flashcards_core.load(filename)

    # add
    card = dict_of_decks.Card(*card_contents)
    dict_of_decks = flashcards_core.add_card_to_deck (card, deck, position)

        # front = input("Front of card: ")  
        # back = input(Back of card)
    # Save
    dict_of_decks.save(dict_of_decks, filename)


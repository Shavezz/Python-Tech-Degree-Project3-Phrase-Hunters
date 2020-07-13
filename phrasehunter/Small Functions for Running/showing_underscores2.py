import random

PHRASES =[
'A Piece of Cake',
'An Arm and a Leg',
'Back to Square One',
'Beating Around the Bush',
'Cut To The Chase',
'Sharing is caring'
]

phrase = random.choice(PHRASES)

def start_game():
    #while Phrase.was_guessed_phrase == False:
        show_underscores()
        guess = input(print('Guess a letter: '))


def show_underscores():
    underscores = '_' * len(phrase)
    print (underscores)

    #for spaces in phrase:
       #phrase.replace(' ', ' ')

        
start_game()

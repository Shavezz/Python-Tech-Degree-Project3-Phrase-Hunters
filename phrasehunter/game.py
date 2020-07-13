from character import Character
from phrase import Phrase
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

#Character = Character()
Phrase = Phrase(phrase)


phrase = random.choice(PHRASES)
#Phrase.phrase = phrase

class Game:
    def __init__(self, PHRASES):
        self.PHRASES = PHRASES


    def start_game():
        #while Phrase.was_guessed_phrase == False:
            #show_underscores()
            guess = input(print('Guess a letter: '))
            
        

    #def show_win_screen():

    #def show_lose_screen():


    def getting_players_input():
        #pass this info to Phrase.py
        if was_guessed_phrase.check_if_guessed.Phrase == True:
            show_win_screen()

        else:
            show_lose_screen()


    def show_underscores():
        underscores = '_' * len(phrase)
        print (underscores)

        #for spaces in phrase:
            #phrase.replace(' ', ' ')
    
    start_game()

      

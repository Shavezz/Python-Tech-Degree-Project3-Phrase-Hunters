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
Phrase = Phrase(phrase)


class Game:
    def __init__(self, PHRASES):
        self.PHRASES = PHRASES


    def start_game(self):
        while Phrase.was_guessed_phrase == False:
            self.show_underscores()
            guess = input(print('Guess a letter: '))
            Character = Character(guess) #here I am making the 'guess' that user will input equal to the original_char in the Character class
            if guess == Character.original_char:
                Phrase.was_guessed_phrase == True
                
            
        

    #def show_win_screen(self):

    #def show_lose_screen(self):


    def getting_players_input(self):
        #pass this info to Phrase.py
        if was_guessed_phrase.check_if_guessed.Phrase == True:
            show_win_screen()

        else:
            show_lose_screen()


    def show_underscores(self):
        spacing = ''
        for spaces in phrase:
            if spaces != ' ':
                spacing += '_'
            else:
                spacing += ' '
        print(spacing)


        #for char in phrase:
            #print('_', end=" ")

        #underscores = '_' * len(phrase)
        #print (underscores)

        #for spaces in phrase:
            #phrase.replace(' ', ' ')



Game = Game(Phrase)    
Game.start_game()

      

from character import Character

#Character = Character(char)
 
class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase
        self.was_guessed_phrase = False

        for char in phrase:
            char = Character(char)


    def check_if_guessed(self, guessed_phrase):
        if self.guessed_phrase == phrase:
            self.was_guessed_phrase = True

    def show_phrase(self):
        if self.was_guessed_phrase == True:
            print (phrase)
            

  

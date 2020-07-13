class Character:
    def __init__(self, char1):
        self.original_char = char1
        was_guessed_character = False

    def update(self, guess):
        if guess == original_char:
            was_guessed_character == True
        


    def show_character():
        if was_guessed_character == True and len(original_char) == 1 and original_char.isalpha():
            print(original_char)
        else:
            print("_")



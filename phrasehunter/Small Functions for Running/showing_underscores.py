from phrasehunter.Phrase import Phrase

#Phrase = Phrase(PHRASES)

PHRASES ={
'A Piece of Cake'
'An Arm and a Leg'
'Back to Square One'
'Beating Around the Bush'
'Cut To The Chase'
'Sharing is caring'
}


phrase = random.choice(PHRASES)
Phrase.phrase = phrase



def showing_underscores():
    underscores = '_' * len(phrase)
    print(underscores)



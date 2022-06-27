from spellchecker import SpellChecker

class SearchFood:
    def __init__(self):
        pass
        
    def correction(self, misspelled_words):
        spell = SpellChecker(distance=1)

        # find those words that may be misspelled
        misspelled = spell.unknown(misspelled_words)
        
        for word in misspelled:
            
            # Get the one most likely answer
            print(spell.correction(word))

            # # Get a list of likely options
            print(spell.candidates(word))


search = SearchFood()
search.correction(['something', 'is', 'hapenning', 'here', 'chickeen','Shrimpe','Cockktail' ])
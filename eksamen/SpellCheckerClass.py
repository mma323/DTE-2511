class SpellChecker:
    def __init__(self, wordDictionary, fileToCheck):
        self.wordDictionary = wordDictionary
        self.fileToCheck = fileToCheck
        try:
            self.readDictionary()
            self.checkFile()
        except FileNotFoundError:
            print("File not found, enter valid file")
            quit()

    def readDictionary(self):
        self.valid = set( word.strip() for word in open(self.wordDictionary) )


    def checkFile(self):
        self.misspelled = dict()
        words = open(self.fileToCheck, "r")
        words = words.read()
        words = words.split()
        self.words = words
        for word in words:
            if word not in self.valid:
                if word in self.misspelled:
                    self.misspelled[word] += 1
                else:
                    self.misspelled[word] = 1
        self._checkPlural()

    
    def _checkPlural(self):
        pluralEnding = []
        for word in self.valid:
            plural = word + "r" if word[-1]=="e" else word + "er"
            pluralEnding.append(plural)
            plural = word + "ne" if word[-1] =="e" else word + "ene"
            pluralEnding.append(plural)

        for word in pluralEnding:
            if word in self.misspelled:
                del self.misspelled[word]
    
    def __str__(self):
        string = "Feilstavede ord: " + "\n"
        for key in self.misspelled:
            string += str(key) + "   -   " + str( self.misspelled[key] ) + "\n"
        return string

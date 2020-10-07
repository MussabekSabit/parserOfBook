from PyDictionary import PyDictionary
dictionary=PyDictionary()

class Meaning():
    def __init__(self, list):
        self.list = list

    def dict_with_meaning(self):
        dict_of_meaning = {}

        for item in self.list:
            dict_of_meaning[item] = dictionary.meaning(item, disable_errors=True)
        return dict_of_meaning

import re
import ebooklib
import enchant
from bs4 import BeautifulSoup
from ebooklib import epub
from nltk.stem import WordNetLemmatizer

import nltk
nltk.download('wordnet')
wnl = WordNetLemmatizer()

d = enchant.Dict("en_US")

class ContentOfEpub:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_list(self):
        file_path = self.file_path[1:]
        book = epub.read_epub(file_path)
        list_of_words=[]
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(item.get_content(), "html5lib")
            [list_of_words.extend(re.sub(r'[^\w]', ' ', text.lower()).split()) for text in soup.stripped_strings]

        list_of_words = [item for item in list_of_words if not item.isdigit() and item.isalpha() and d.check(item)]
        list_of_words = [wnl.lemmatize(item) for item in list_of_words]
        list_of_words = list(dict.fromkeys(list_of_words))
        return sorted(list_of_words)
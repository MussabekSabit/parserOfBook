import json
import os
from meaning_of_words import Meaning
file_path = "‪C:/Users/mussa/Desktop/byte-of-python.epub"



list_of_data = []
if os.path.isfile('./data.json'):
    with open('data.json', 'r') as f:
        list_of_data = json.loads(f.read())
else:
    with open('data.json', 'w', encoding='utf-8') as f:
        from words_from_epub import ContentOfEpub
        file_obj = ContentOfEpub(file_path)
        json.dump(file_obj.get_list(), f, ensure_ascii=False, indent=4)

dict_of_data_meaning ={}
if os.path.isfile('./data_meaning.json'):
    with open('data_meaning.json', 'r') as f:
        dict_of_data_meaning = json.loads(f.read())
else:
    with open('data_meaning.json', 'w', encoding='utf-8') as f:
        meaning_dict_obj = Meaning(list_of_data)
        json.dump(meaning_dict_obj.dict_with_meaning(), f, ensure_ascii=False, indent=4)

print(len(list_of_data))
print(list_of_data)

print(dict_of_data_meaning)

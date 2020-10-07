from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.ru',
      'translate.google.kz',
    ])
list_of_translated_words = []
list_of_translated_words= [translator.translate(item,dest='ru', src='en').text.lower() for item in list_of_words ]

dictionary = { list_of_words:list_of_translated_words}
print(dictionary)
rus_en = {"а": 'a', "б": 'b', "в": 'v', "г": 'g', "д": 'd', "е": 'e', "ё": 'e',
          "ж": 'zh', "з": 'z', "и": 'i', "й": 'y', "к": 'k', "л": 'l', "м": 'm',
          "н": 'n', "о": 'o', "п": 'p', "р": 'r', "с": 's', "т": 't', "у": 'u',
          "ф": 'f', "х": 'kh', "ц": 'ts', "ч": 'ch', "ш": 'sh', "щ": 'shch',
          "ы": 'y', "э": 'e', "ю": 'yu', "я": 'ya'}
en_rus = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', 'e': 'э', 'zh': 'ж',
          'z': 'з', 'i': 'и', 'y': 'ы', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
          'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'f': 'ф',
          'kh': 'х', 'ts': 'ц', 'ch': 'ч', 'sh': 'ш', 'shch': 'щ', 'yu': 'ю',
          'ya': 'я'}

def rus(sentence):
    words = [word.lower() for word in sentence.split()]
    ling = rus_en.copy()
    if 'е' in word:
        ind = word.find('е')
    result = [ling.get(i, '') for i in word]
    print(''.join(result))


def en(sentence):
    words = [word.lower() for word in sentence.split()]


sentence = input('Введите слово, которое нужно транслитерировать\n')
if sentence[0] in rus_en.keys():
    rus(sentence)
else:
    en(sentence)
        

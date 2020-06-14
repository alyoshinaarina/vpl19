s_word, path = input('Введите через пробел нужное слово и полный путь до файла: ').split(' ', 1)
txt = []
s_word = s_word.lower()
with open(path, 'r') as f:
    txt = f.readlines()

words = []
for line in txt:
    for word in line.split():
        word = word.lower()
        words.append(word)

indexes = [i for i, word in enumerate(words) if word == s_word]
dct = dict()
for i in indexes:
    if i > 0:
        if not dct.get(words[i - 1]):
            dct.update({words[i - 1]: 1})
        else:
            dct[words[i - 1]] += 1
    if i < len(words) - 1:
        if not dct.get(words[i + 1]):
            dct.update({words[i + 1]: 1})
        else:
            dct[words[i + 1]] += 1

res = sorted(dct.items(), key=lambda item: (-item[1], item[0]))
if len(res) == 0:
    print('Коллокатов не нашлось :(')
else:
    print('Словарь: ')
    for word, cnt in res:
        print(word, cnt)

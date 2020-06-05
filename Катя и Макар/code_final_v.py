import re
import pandas as pd
#чистим текст
st_file = input('Введите путь к файлу: ')
with open(st_file, encoding='utf-8') as f:
    text = f.read()
clean_text = re.findall(r'[А-Яа-яЁё]+-?[А-Яа-яЁё]*',text)
clean_text = ' '.join(clean_text)
clean_text = clean_text.lower()
clean_text = clean_text.split(' ')
#ищем коллокаты
wrd = input('Введитие слово для поиска: ')
wrd = wrd.lower()
spisok = []
if wrd in clean_text:
    for i in clean_text:
        if i == wrd:
            spisok.append(clean_text[clean_text.index(i) - 1])
            spisok.append(clean_text[clean_text.index(i) + 1])
            clean_text.remove(i)
    d = {word: spisok.count(word) for word in spisok}
    spisok_values = []
    spisok_index = []
    spisok_range_values = []
    spisok_keys = []
    spisok_range_keys = []
    for v in d.values():
        spisok_values.append(v)
    maximum = max(spisok_values)
    for v in range(0, maximum):
        for v in spisok_values:
            if v == maximum:
                spisok_range_values.append(v)
                spisok_index.append(spisok_values.index(v))
                spisok_values[spisok_values.index(v)] = maximum + 1
        maximum -= 1
    for k in d:
        spisok_keys.append(k)
    for index in spisok_index:
        spisok_range_keys.append(spisok_keys[index])
    general_slovar = {x: y for x, y in zip(spisok_range_keys, spisok_range_values)}
    print('Вот ранжированный список коллокатов, которые нам удалось найти для слова', '"' + wrd + '":')
    print('(результаты также сохранены в формате csv-файла)')
    for k, v in general_slovar.items():
        print(k, ' - ', v)
    #сохраняем результат поиска в файл
    new_dict = {'Коллокаты': list(general_slovar.keys()), 'Частота': list(general_slovar.values())}
    df = pd.DataFrame(new_dict)
    print(df)
    df.to_csv('Collocates.csv')
else:
    print('В тексте нет заданного слова...')

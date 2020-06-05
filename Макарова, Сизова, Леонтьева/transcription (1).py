#capitalletters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#letters = "абвгдгеёжзийклмнопрстуфхцчшщъыьэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
ImVowels = "АЕЁИОУЫЭЮЯ"
vowels = "аеёиоуыэюя"
#special = 'ъь'
SoftConSounds = ["б'","в'","г'","д'",' ',"з'","j'","к'","л'","м'","н'","п'","р'","с'","т'","ф'","х'","ч'",' ',"щ'"]
SolidConSounds = ["б","в","г","д","ж","з",' ', "к","л","м","н","п","р","с","т","ф","х","ц",' ',"ш"]
Vsounds = ["а",' ',' ',"и","о","у","ы","э","ь","ъ" ]

ifsoft = 'ьяюеёичщйЯЮЕЁИ'

word = input("Введите слово, выделив ударный гласный заглавной буквой: ")
newword = ''

length = len(word)

for i in range(length):
    if (vowels.find(word[i]) != -1): #проверка, является ли буква гласной безударной
        newword = newword + Vsounds[vowels.find(word[i])]       #vowels.find(word[i])- номер первого вхождения буквы с индексом i во введенном слове в строке vowels
    elif (ImVowels.find(word[i]) != -1):    #проверка, является ли буква гласной ударной
        newword = newword + Vsounds[ImVowels.find(word[i])]     #ImVowels.find(word[i])- номер первого вхождения буквы с индексом i во введенном слове в строке ImVowels
    else:       #если предыдущие условия не выполнились, то остался один вариант - буква является согласной
        if (ifsoft.find(word[i]) != -1):      #проверка на мягкость согласного (если следующая буква одна из тех, что есть в строке ifsoft, то звук - мягкий)
            newword = newword + SoftConSounds[consonants.find(word[i])]
            #consonants.find(word[i])- номер первого вхождения буквы с индексом i во введенном слове в строке consonants
        else:
            newword = newword + SolidConSounds[consonants.find(word[i])]

print('transcription:  ',newword)

#capitalletters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#letters = "абвгдгеёжзийклмнопрстуфхцчшщъыьэюя"
consonants = "бвгджзйклмнпрстфхцчшщ"
ImVowels = "АЕЁИОУЫЭЮЯ"
vowels = "аеёиоуыэюя"
special = 'ъь'
SoftConSounds = ["б'","в'","г'","д'",' ',"з'","j'","к'","л'","м'","н'","п'","р'","с'","т'","ф'","х'"," ","ч'",' ',"щ'"]
SolidConSounds = ["б","в","г","д","ж","з",' ', "к","л","м","н","п","р","с","т","ф","х","ц",' ',"ш"]
Vsounds = ["а","э","о","и","о","у","ы","э","у","а","ь","ъ","/\ "]

SoftSounds =''

ifsoft = 'ьяюеёичщйЯЮЕЁИ'
vow = 'еёюяЕЁЮЯ'

word = input("Введите слово, выделив ударный гласный заглавной буквой: ")
newword = ''

length = len(word)

for i in range(length):
    if (special.find(word[i]) != -1):
        continue
    
    elif (vowels.find(word[i]) != -1): #проверка, является ли буква гласной безударной
        newword = newword + Vsounds[vowels.find(word[i])]       #vowels.find(word[i])- номер первого вхождения буквы с индексом i во введенном слове в строке vowels
        if  (i!=0) and (vow.find(word[i]) != -1):             
            if (vowels.find(word[i-1])!=-1) or (special.find(word[i-1]) != -1): #если предыдущая буква - гласная, или ъ, или ь
                    newword = newword + SoftConSounds[6]+ Vsounds[vowels.find(word[i])]       

        
    elif (ImVowels.find(word[i]) != -1):    #проверка, является ли буква гласной ударной
        if (vow.find(word[i]) != -1):
            if  (i==0):             #если одна из этих букв стоит в начале слова
                newword = newword + SoftConSounds[6] + Vsounds[ImVowels.find(word[i])]             
            else:
                if (vowels.find(word[i-1])!=-1) or (special.find(word[i-1]) != -1): #если предыдущая буква - гласная, или ъ, или ь
                    newword = newword + SoftConSounds[6]+ Vsounds[ImVowels.find(word[i])]       
                elif ((SoftSounds.join(SoftConSounds)).find(newword[i-1])!=-1): #если предыдущая буква - мягкий согласный(объединяем список в строку, чтобы можно было методом find проверить условие)
                    newword = newword + Vsounds[ImVowels.find(word[i])]
        else:
            newword = newword + Vsounds[ImVowels.find(word[i])]     #ImVowels.find(word[i])- номер первого вхождения буквы с индексом i во введенном слове в строке ImVowels
                
                         
    else:       #если предыдущие условия не выполнились, то остался один вариант - буква является согласной
        if (word[i]=="ш")or(word[i]=="ж")or(word[i]=="ц"):
                    newword = newword + SolidConSounds[consonants.find(word[i])]
        elif (word[i]=="ч")or(word[i]=="щ")or(word[i]=="й"):     #проверка на всегда мягкие согласные
                newword = newword + SoftConSounds[consonants.find(word[i])]
        elif (i!=length-1):       #проверка, является ли согласный последней буквой (чтоб индекс не выходил за рамки допустимого диапазона)
            if (ifsoft.find(word[i+1]) != -1):     #проверка на мягкость согласного (если следующая буква одна из тех, что есть в строке ifsoft, то звук - мягкий)
                newword = newword + SoftConSounds[consonants.find(word[i])]
            else:
                newword = newword + SolidConSounds[consonants.find(word[i])]
        elif (i==length-1):     #если последняя буква- согласная
            newword = newword + SolidConSounds[consonants.find(word[i])]

print('transcription:  ',newword)

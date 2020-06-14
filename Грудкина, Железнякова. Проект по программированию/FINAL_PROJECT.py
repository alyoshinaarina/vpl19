print ('Введите, пожалуйста, прилагательное в именительном падеже. Степень прилагательного может быть любая. Прилагательное не должно быть качественным. Эта программа выведет простую и сложную форму сравнительной степени, если это возможно :3')
word = input()
only_complex = ['кровный', 'ручной', 'больной', 'ранний', 'лишний', 'зыбкий', 'дерзкий', 'ломкий', 'липкий', 'топкий', 'робкий', 'падкий', 'цепкий', 'зябкий', 'золотой', 'серебряный']
endings_of_adj = ['ый', 'ий', 'ая', 'яя', 'ое', 'ее', 'ые', 'ие']
first_adj = ''
if 'ейш' in word or 'айш' in word:
    if 'ейш' in word:
        index = word.find('е')
        new_word = word[:index]+ 'ый'
    elif 'айш' in word:
        index = word.find('а')
        new_word = word[:index]+ 'ий'
    word = new_word
first_adj = ''
if word in only_complex:
    print ('К сожалению, это прилагательное не имеет простой формы сравнительной степени')
elif 'ск' in word[-4:] or 'ов' in word[-4:] or 'ев' in word[-4:] or word[-3] == 'л':
    print ('К сожалению, это прилагательное не имеет простой формы сравнительной степени')    
else:
    first_adj = ''
    if word[-2:] in endings_of_adj:
        first_adj = ''
        if word == 'хороший':
            first_adj = 'лучше'
        elif word == 'плохой':
            first_adj = 'хуже'
        elif word == 'маленький' or word == 'малый':
            first_adj = 'меньше'
        elif word == 'молодой':
            first_adj = 'младше'
        elif word == 'старый':
            first_adj = 'старше'
        elif word == 'высокий':
            first_adj = 'выше'
        elif word == 'сладкий':
            first_adj = 'слаще'
        elif word[-3] == 'г' and word[-4] != 'л' or word[-3] == 'д':
            first_adj = word[:-3] + 'же'
        elif 'зк' in word:
            index = word.find('з')
            first_adj = word[:index]+ 'же'
        elif 'ст' in word:
            index = word.find('с')
            first_adj = word[:index]+ 'ще'
        elif word[-4] == 'н' and word[-3] == 'к' or word[-4] == 'н' and word[-3] == 'н':
            first_adj = word[:-3] + 'ьше'
        elif word[-3] == 'к' and word[-4] == 'г' or word[-4] == 'т' and word[-3] == 'к':
            first_adj = word[:-4] + 'че'  
        elif word[-3] == 'х' :
            first_adj = word[:-3] + 'ше'
        elif word[-3] == 'т':
            first_adj = word[:-3] + 'че'
        elif word[2] == 'л' or word[2] == 'л' and word[3] == 'г'  :
            first_adj = word[:3] + 'ьше'
        else:
            first_adj = word[:-2] + 'ее'
print ('Простая форма сравнительной степени этого прилагательного:', first_adj)
print ('Сложная форма сравнительной степени этого прилагательного: более/менее', word)
print ('Спасибо, что воспользовались нашей программой! Мы очень старались, когда делали ее!')
 


    


k = input('Приветствуем! Мы рады вместе с Вами генерировать степени сравнения прилагательных :)')
l = input ('Если Вы хотите ввести прилагательное в положительной степени, вызовите adjective(). Если в сравнительной - comparative(). Если в превосходной - superlative(). Если в превосходной со словом "самый" - verylative().')
def adjective():
    slovo = input ('Напишите прилагательное в м.р. ед. ч.: ')
    okonchanye = slovo[-2:]

    if okonchanye == 'ий' or okonchanye == 'ый' or okonchanye == 'ой':
        bukva = slovo[-3]
        if slovo == 'хороший' or slovo == 'плохой' or slovo == 'маленький' or slovo == 'простой':
            if slovo == 'хороший':
                f2 = 'лучше'
            elif slovo == 'плохой':
                f2 = 'хуже'
            elif slovo == 'маленький':
                f2 = 'меньше'
            elif slovo == 'простой':
                f2 = 'проще'
            
                
        elif bukva == 'г' or bukva == 'д' or bukva == 'з':
            f2 = slovo[:-3] + 'же'
        elif bukva == 'к' or bukva == 'т':
            f2 = slovo[:-3] + 'че'
        elif bukva == 'х':
            f2 = slovo[:-3] + 'ше'
        else:
            f2 = slovo[:-2] + 'ее' 
                
                
        if slovo == 'хороший' or slovo == 'плохой' or slovo == 'маленький':
            if slovo == 'хороший':
                f3 = 'лучший'
            if slovo == 'плохой':
                f3 = 'худший'
            if slovo == 'маленький':
                f3 = 'наименьший'
        elif bukva == 'г':
            f3 = slovo[:-3] + 'жайший'
        elif bukva == 'х':
            f3 = slovo[:-3] + 'шайший'
        elif bukva == 'к':
            f3 = slovo[:-3] + 'чайший'
        else:
            f3 = slovo[:-2] + 'ейший'
                
        f4 = 'самый' + ' ' + slovo
                
        print('Положительная степень прилагательного: ', slovo)
        print('Сравнительная степень прилагательного: ', f2)
        print('Превосходная степень прилагательного: ', f3)
        print('Превосходная степень прилагательного с "самый": ', f4)
    else:
        print('Что-то не так. Удостоверьтесь, что Вы ввели прилагательное.')

def comparative():
    slovo = input('Напишите прилагательное в м.р ед. ч.: ')
    okonchanye = slovo[-2:]
    if slovo == 'лучше' or slovo == 'хуже' or slovo == 'меньше' or slovo == 'проще':
            if slovo == 'лучше':
                f_ = 'хороший'
            elif slovo == 'хуже':
                f_ = 'плохой'
            elif slovo == 'меньше':
                f_ = 'маленький'
            elif slovo == 'проще':
                f_ = 'простой'
    elif okonchanye == 'ше':
        f_ = slovo[:-2] + 'хи' + 'й'
    elif okonchanye == 'же':
        f_ = slovo[:-2] + 'го' + 'й'
    elif okonchanye == 'ее':
        f_ = slovo[:-2] + '(ий)/(ой)/(ый)'
    
    bukva = f_[-3]
    if f_ == 'хороший' or f_ == 'плохой' or f_ == 'маленький':
            if f_ == 'хороший':
                f3 = 'лучший'
            if f_ == 'плохой':
                f3 = 'худший'
            if f_ == 'маленький':
                f3 = 'наименьший'
    elif bukva == 'г':
        f3 = f_[:-3] + 'жайший'
    elif bukva == 'х':
        f3 = f_[:-3] + 'шайший'
    elif bukva == 'к':
        f3 = f_[:-3] + 'чайший'
    else:
        f3 = f_[:-2] + 'ейший'
                
    f4 = 'самый' + ' ' + f_
        
    print('Положительная степень прилагательного: ', f_)
    print('Сравнительная степень прилагательного: ', slovo)
    print('Превосходная степень прилагательного: ', f3)
    print('Превосходная степень прилагательного с "самый": ', f4)

    
def superlative():
    slovo = input ('Напишите прилагательное в м.р. ед. ч.: ')
    okey = slovo[-6:]
   
                
    if okey == 'жайший' or okey == 'шайший' or okey == 'чайший':
        if okey == 'жайший':
            f = slovo[:-6] + 'гий'
        elif okey == 'шайший':
            f = slovo[:-6] + 'хий'
        elif okey == 'чайший':
            f = slovo[:-6] + 'кий'
        else:
            f = slovo[:-5] + '(ий)/(ой)/(ый)' 


        bukva = f[-3]       
        if bukva == 'г' or bukva == 'д' or bukva == 'з':
            f2 = f[:-3] + 'же'
        elif bukva == 'к' or bukva == 'т':
            f2 = f[:-3] + 'че'
        elif bukva == 'х':
            f2 = f[:-3] + 'ше'
        else:
            f2 = f[:-14] + 'ее' 
                
        f4 = 'самый' + ' ' + f
         
        print('Положительная степень прилагательного: ', f)
        print('Сравнительная степень прилагательного: ', f2)
        print('Превосходная степень прилагательного: ', slovo)
        print('Превосходная степень прилагательного с "самый": ', f4)

    else:
        print('Что-то не так. Удостоверьтесь, что Вы ввели прилагательное.')

def verylative():
    vvod = input('Напишите прилагательное в м.р. ед.ч.: ')
    slovo = vvod[6:]

    okonchanye = slovo[-2:]

    if okonchanye == 'ий' or okonchanye == 'ый' or okonchanye == 'ой':
        bukva = slovo[-3]
      
        if slovo == 'хороший' or slovo == 'плохой' or slovo == 'маленький' or slovo == 'простой':
            if slovo == 'хороший':
                f2 = 'лучше'
            elif slovo == 'плохой':
                f2 = 'хуже'
            elif slovo == 'маленький':
                f2 = 'меньше'
            elif slovo == 'простой':
                f2 = 'проще'
            
                
        elif bukva == 'г' or bukva == 'д' or bukva == 'з':
            f2 = slovo[:-3] + 'же'
        elif bukva == 'к' or bukva == 'т':
            f2 = slovo[:-3] + 'че'
        elif bukva == 'х':
            f2 = slovo[:-3] + 'ше'
        else:
            f2 = slovo[:-2] + 'ее' 
            
            
                
        if slovo == 'хороший' or slovo == 'плохой' or slovo == 'маленький':
            if slovo == 'хороший':
                f3 = 'лучший'
            if slovo == 'плохой':
                f3 = 'худший'
            if slovo == 'маленький':
                f3 = 'наименьший'
        elif bukva == 'г':
            f3 = slovo[:-3] + 'жайший'
        elif bukva == 'х':
            f3 = slovo[:-3] + 'шайший'
        elif bukva == 'к':
            f3 = slovo[:-3] + 'чайший'
        else:
            f3 = slovo[:-2] + 'ейший'

        print('Положительная степень прилагательного: ', slovo)
        print('Сравнительная степень прилагательного: ', f2)
        print('Превосходная степень прилагательного: ', f3)
        print('Превосходная степень прилагательного с "самый": ', vvod)

    else:
        print('Что-то не так. Удостоверьтесь, что Вы ввели прилагательное.')

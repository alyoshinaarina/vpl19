# Гороскоп
1. Программа принимает на вход дату рождения пользователя в формате 01.01.2000 или 1 января 2000, год можно опустить.
2. Далее с помощью модуля time программа определяет текущую дату в виде дд.мм.гггг, создаётся список с данными значениями по отдельности.
3. Месяцы распределяются по количеству дней и определяется тип года (високосный или нет).
4. Если текущее число - последний день месяца (кроме декабря), то следующий день будет вида - 01.текущий_месяц+1.гггг.
5. Если сегодня 31 декабря, то следующий день будет вида - 01.01.текущий_год+1
6. Если сегодня не последний день месяца, то следующий день будет вида - текущий_день+1.мм.гггг
7. Выводится дата следующего дня.
8. Возращаемся к анализу даты рождения. Создаётся переменные day и month, которые содержат день и месяц рождения соответственно.
9. Если месяц был введён не с помощью цифр, а буквами, то заменяем его на цифровое значение для удобства анализа.
10. Поскольку переменная day типа str, меняем формат на int.
11. В зависимости от месяца рождения, а впоследствии от дня определяется знак зодиака. 
12. Выводится сообщение с определённым знаком зодиака.
13. С помощью модуля random выбирается, каким будет следующий день (удивительным, грустным и т.д.).
14. В зависимости от того, хорошим или плохим будет следующий день, выводятся разные предсказания, связанные со здоровьем, любовью и семьёй, также с помощью модуля random.
15. В итоге на экране оказываются отображены: текущая дата, следующая дата, ваш знак зодиака, а также предсказание на следующий день

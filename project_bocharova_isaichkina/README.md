## **Проект по программированию**
# **Транслитерация слов**
###  Подготовили студентки 19ФПЛ-1, Бочарова Дарья, Исаичкина Анастасия
***
 ***Описание проекта:***Данная программа транслитерирует текст, написанный кириллическими буквами в текст, написанный при помощи латинского алфавита.
 Важно отметить, что акцент при создании данной программы был сделан на транслитерации текста с кириллицы на латиницу. Обратная транслитерация имеет место быть, однако нуждается в доработке по дополнительным правилами транслитерации.
***
Для выполения поставленной задачи программа производит следующие действия:
1.   В первую очередь мы спрашиваем у пользователя, хочет ли он транслитерировать текст в файле или ввести в ручную
2.   В зависимости от ответа пользователя, ему предоставляется возможность ввести имя файла, текст которого он хочет транслитерировать, или доступ к ручному набору текста
3.   Текст проходит анализ на наличие букв кириллицы или латиницы
4.   В зависимости от того, какой алфавит определила программа, каждая буква текста заменяется буквы другого алфавита
5.   После получения результата пользователю предлагается транслитерировать что-либо еще
6.   Пользователь может продолжать транслитерировать различные тексты, пока не прервет цикл ответом "нет" на вопрос о повторной транслитерации чего-либо
***
####***Примеры***
***Request:*** На горе стоял проклятый старый дом, в нем жили ежики и ершики
***Answer:*** Na gore stoyal proklyatyy staryy dom, v nem zhili yezhiki i yershiki
***
***Request:*** За свою длинную жизнь я успел повидать множество невиданных тварей
***Answer:*** Za svoyu dlinnuyu zhizn' ya uspel povidat' mnozhestvo nevidannykh tvarey
***
***Request:*** Съешь ещё этих мягких французских булок, да выпей же чаю
***Answer:*** Syesh' yeshchyo etikh myagkikh frantsuzskikh bulok, da vypey zhe chayu
***
***Request:*** Za oknom idyot dozhd'
***Answer:*** За окном идёт дождь
***
***Request:*** On ochen' umnyy potomu chto mnogo chitaet
***Answer:*** Он очэнь умный потому что много читаэт
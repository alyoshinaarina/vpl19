﻿# *Гороскоп*
* Программа принимимает на вход дату рождения пользователя (в нескольких форматах записи).
* Введеная дата рождения распределяется между двумя переменными day и month2(дата сохраняется в переменную day, месяц - в переменную mounth2).
* Если при вводе даты рождения месяц был записан буквами, то происходит замена на цифровое значение.
* В зависимости от даты рождения определяется знак задиака.
* Полученный знак зодиака выводится на экран.
* Из модуля time берется текущая дата: день месяца записывается в переменную date, номер месяца - в month, год с веком - в year.
* Затем вычисляется дата следующего дня.
* На экран выводится текст: «Гороскоп на», где далее следует число, месяц (полное название) и год.
* Затем из набора предсказаний рандомно (с помощью random.randint) выбирается одно и выводится на экран.
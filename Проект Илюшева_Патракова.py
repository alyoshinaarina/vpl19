import time

text = '''Не следует, однако, забывать о том, что начало повседневной работы по формированию позиции требует определения и уточнения существующих финансовых и административных условий. Значимость этих проблем настолько очевидна, что сложившаяся структура организации напрямую зависит от всесторонне сбалансированных нововведений. Значимость этих проблем настолько очевидна, что постоянный количественный рост и сфера нашей активности в значительной степени обуславливает создание позиций, занимаемых участниками в отношении поставленных задач.'''
error = 0
error_words = ''
t = text.split(' ')
p = ''
for x in t:
    x  += " "
    for i in range (0, len(x)):
        if x[i].isalpha() and x[i] != "n":
            p += x[i]
        elif x[i] == ' ':
            p += x[i]
p = p.lower()
p = p.split(' ')
#print(p)

print(text)
start_time = time.time()
text_check = input('Ready! Steady! Go!\n')
end_time = time.time()
t2 = text_check.split(' ')
p2 = ''
for x2 in t2:
    x2  += " "
    for i2 in range (0, len(x2)):
        if x2[i2].isalpha() and x2[i2] != "n":
            p2 += x2[i2]
        elif x2[i2] == ' ':
            p2 += x2[i2]
p2 = p2.lower()
p2 = p2.split(' ')
#print(p2)

for y in range (0, len(p)):
    if p[y] != p2[y]:
        error += 1
        error_words = error_words + p2[y] + ','
        y += 1
    else:
        y += 1

time_taken = (end_time - start_time)
print (round(time_taken, 2), "сек")
print (error, 'ош.')
print (error_words)


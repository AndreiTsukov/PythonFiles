#1. ЗАДАЧА «ДЕЛАЕМ СРЕЗЫ»
#1. Сначала выведите третий символ этой строки.
'''
stroka = input()
k = stroka[3]
print(k)

#2. Во второй строке выведите предпоследний символ этой строки.
stroka = input()
k = stroka[-2]
print(k)

#3. В третьей строке выведите первые пять символов этой строки.
stroka = input()
k = stroka[:5]
print(k)

#4. В четвертой строке выведите всю строку, кроме последних двух символов.
stroka = input()
k = stroka[0:-2]
print(k)

#5. В пятой строке выведите все символы с четными индексами (считая, что
#индексация начинается с 0, поэтому символы выводятся начиная с первого).
stroka = input()
k = stroka[0:-1:2]
print(k)

#6. В шестой строке выведите все символы с нечетными индексами, то есть начиная со
#второго символа строки.
stroka = input()
k = stroka[0:-1:1]
print(k)

#7. В седьмой строке выведите все символы в обратном порядке
stroka = input()
k = stroka[::-1]
print(k)

#8. В восьмой строке выведите все символы строки через один в обратном порядке,
#начиная с последнего.
stroka = input()
k = stroka[::-2]
print(k)
'''
#9. В девятой строке выведите длину данной строки
stroka = input()
z = len(stroka)
print(z)

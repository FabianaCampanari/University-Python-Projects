Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Fatiamento Sequencia
>>> lista = [30,12, 13,41,15,6,78,44,19]
>>> lista[2:4]
[13, 41]
>>> #se omitido passo é 1
>>> lista[1::3]#se omitido fim é len(lista)
[12, 15, 44]
>>> lista[:3]
[30, 12, 13]
>>> #se omitido inicio é zero
>>> lista[5:1] #se fim <=inicio, a fatia é vazia
[]
>>> lista[5:1:-1] #se passo é negativo, inverte ordem da fatia
[6, 15, 41, 13]
>>> 
===================== RESTART: Shell ====================
>>> lista = [30,12, 13,41,15,6,78,44,19]
>>> lista[2:4]
[13, 41]
>>> #se omitido passo é 1
>>> lista[1::3]#se omitido fim é len(lista)
[12, 15, 44]
>>> lista[5:1] #se fim <=inicio, a fatia é vazia
[]
>>> lista[5:1:-1] #se passo é negativo, inverte ordem da fatia
[6, 15, 41, 13]
>>> lista[:] #fatia correspondente a lista inteira
[30, 12, 13, 41, 15, 6, 78, 44, 19]

##Sequence slicing is an operation that extracts a part of a sequence, such as a list
#or a string, by specifying a start and an end index.
#For example,
#list[2:5] is a sequence slicing that returns a new list with the elements from index 2
#(inclusive) to index 5 (exclusive) of the original list.

##Sequence slicing can also use negative indexes to count from the end of the sequence,
#or omit the start or end index to use the default values.
#For example,
#list[-3:] is a sequence slicing that returns a new list with the last three elements
#of the original list.

Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

#Concatenação e repetição

#A concatenação e a repetição não alteram os objetos, geram um novo.
#Portanto, não é a forma mais eficiente para adicionar itens
#a uma sequência.Uma abordagem melhor é usar o método append()
#em uma lista,

#Concatenação

>>>(1, 2) + (3, 4)
(1, 2, 3, 4)
>>>'abc' + 'xyz'
'abcxyz'
>>>[30, 40] + [10,20,50]
[30, 40, 10, 20, 50]


#REPETICAO

>>>3 * 'ABC'
'ABCABCABC'
>>>5 * [0]
[0, 0, 0, 0, 0]
>>>4 * (123,)
(123, 123, 123, 123)

#Repeticao Lista aninhada

>>> s = [[2]] * 3
>>> s
[[2], [2], [2]]
>>> 
============= RESTART: Shell ============
>>> #Alteraçao Lista Interna

>>> s = [[2]] * 3
>>> s
[[2], [2], [2]]
>>> s[0][0] = 5
>>> s
[[5], [5], [5]]

##Concatenation is an operation that joins two or more sequences, such as lists or
#strings, into one. For example, list1 + list2 is a concatenation of two lists that
#creates a new list with all the elements of list1 and list2.

##Repetition is an operation that repeats a sequence, such as a list or a string, a
#certain number of times. For example, list * 3 is a repetition of a list that creates
#a new list with three copies of the original list.

## A nested list is a list that contains another list as an element. For example,
#[[1, 2], [3, 4]] is a nested list with two sublists. Repetition of a nested list is
#similar to repetition of a regular list, but it repeats the sublists as well.
#For example, [[1, 2], [3, 4]] * 2 is a repetition of a nested list that creates a new
#nested list with four sublists: [[1, 2], [3, 4], [1, 2], [3, 4]].

##Modification of an internal list is an operation that changes the elements of a
#sublist in a nested list. For example, if nested = [[1, 2], [3, 4]], then
#nested[0][1] = 5 is a modification of an internal list that changes the second
#element of the first sublist to 5: [[1, 5], [3, 4]].


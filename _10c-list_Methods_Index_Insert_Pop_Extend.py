#Metodos
>>> lista = [1,8,5,True, 3]
>>> id(lista)
4348608896
>>> lista[5]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    lista[5]
IndexError: list index out of range
>>> lista
[1, 8, 5, True, 3]
>>> lista.append(5)
>>> lista
[1, 8, 5, True, 3, 5]
>>> lista.append(7)
>>> lista
[1, 8, 5, True, 3, 5, 7]
>>> lista[3] = 22
>>> lista
[1, 8, 5, 22, 3, 5, 7]
>>> lista = [15, 10, 99]
>>> lista.extend((1, 2, 3))
[15, 10, 99, 1, 2, 3]

lista.remove(v)
lista.insert(i,v)
lista.pop(i)
lista[i]
lista[i] = v
lista.append
lista.extend #1

## 1estender a lista.A sequência que recebe os itens
#precisa ser mutável, portanto uma lista, mas a sequência que cede
#os itens pode ser de qualquer tipo

#Methods can perform operations on the object or modify its state. For example,
#list.append(x) is a method that adds an item to the end of a list.

##Index is a number that indicates the position of an item in a sequence, such as
#a list or a string. Indexes start from zero in Python. For example, list.index(x)
#is a method that returns the index of the first item whose value is equal to x in
#a list.

##insert means insert in English. Insert is an operation that adds an item to a
#specific position in a sequence, such as a list or a string.
#For example, list.insert(i, x) is a method that inserts an item x at position i
#in a list.

##pop means pop in English. Pop is an operation that removes and returns an item from
#a specific position in a sequence, such as a list or a string. If no position is
#specified, pop removes and returns the last item in the sequence. For example,
#list.pop(i) is a method that removes and returns the item at position i in a list.

##extend means extend in English. Extend is an operation that adds all the items from
#another sequence to the end of a sequence, such as a list or a string. For example,
#list.extend(iterable) is a method that extends a list by appending all the items from
#the iterable argument.




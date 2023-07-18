Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

lista = [1,2,3,4]
lista
[1, 2, 3, 4]
lista.append(5)
lista
[1, 2, 3, 4, 5]
lista.append(22)
lista
[1, 2, 3, 4, 5, 22]
lista[2]
3
lista[5] = 6
lista
[1, 2, 3, 4, 5, 6]
lista.pop(5)
6
LISTA
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    LISTA
NameError: name 'LISTA' is not defined
lista
[1, 2, 3, 4, 5]
lista.append(22)
lista
[1, 2, 3, 4, 5, 22]
lista[3]
4
lista[3] = 20
lista
[1, 2, 3, 20, 5, 22]
lista.pop(3)
20
lista
[1, 2, 3, 5, 22]
lista,remove(3)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    lista,remove(3)
NameError: name 'remove' is not defined
list.remove(3)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    list.remove(3)
TypeError: descriptor 'remove' for 'list' objects doesn't apply to a 'int' object
lista.remove(3)
lista
[1, 2, 5, 22]
lista[2]
5
lista[0] = [22]
lista
[[22], 2, 5, 22]
lista[0] = 22
lista
[22, 2, 5, 22]
lista.append(4)
lista
[22, 2, 5, 22, 4]
lista.remove(2)
lista
[22, 5, 22, 4]
lista.remove[2]
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    lista.remove[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
lista.append(12)
lista
[22, 5, 22, 4, 12]
lista.pop(4)
12
lista
[22, 5, 22, 4]
lista.append(12)
lista
[22, 5, 22, 4, 12]
lista.pop(12)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    lista.pop(12)
IndexError: pop index out of range
lista.pop(1)
5
lista
[22, 22, 4, 12]
lista.insert(1,11)
lista
[22, 11, 22, 4, 12]
lista.remove(4)
lista
[22, 11, 22, 12]
lista[3] = 11
lista
[22, 11, 22, 11]
lista.inset(2,2)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lista.inset(2,2)
AttributeError: 'list' object has no attribute 'inset'. Did you mean: 'insert'?
lista.insert(2,2)
lista
[22, 11, 2, 22, 11]
lista.pop[2]
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    lista.pop[2]
TypeError: 'builtin_function_or_method' object is not subscriptable
lista.pop(2)
2
>>> lista
[22, 11, 22, 11]
>>> lista.insert(2,2)
>>> lista
[22, 11, 2, 22, 11]
>>> lista.insert(2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    lista.insert(2)
TypeError: insert expected 2 arguments, got 1
>>> lista.insert(3,2)
>>> lista
[22, 11, 2, 2, 22, 11]
>>> lista(11)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    lista(11)
TypeError: 'list' object is not callable
>>> lista[1]
11
>>> lista.pop(2)
2
>>> lista
[22, 11, 2, 22, 11]
>>> lista.insert(3,0)
>>> lista
[22, 11, 2, 0, 22, 11]

#Lists are one of the most common data structures in Python. They are used to store
#multiple items in a single variable, and they are ordered, changeable and allow
#duplicates1. To work with lists in Python, you need to know how to perform some basic
#operations on them, such as:

##Access items: You can access items in a list by using their index number, which starts
#from 0 for the first item. You can use square brackets [ ] to get the item at a specific
#position. For example, list[0] returns the first item of the list.
#You can also use negative indexes to access items from the end of the list. For example,
#list[-1] returns the last item of the list2.

##Modify items: You can modify items in a list by assigning a new value to them using the
#assignment operator =. For example, list[0] = “new” changes the first item of the list to
#“new”. You can also modify a range of items by using slicing notation. For example,
#list[1:3] = [“a”, “b”] replaces the second and third items of the list with “a” and "b"2.

##Add items: You can add items to a list by using the append() method, which adds an item to
#the end of the list. For example, list.append(“new”) adds “new” to the end of the list.
#You can also use the insert() method to insert an item at a specific position. For example,
#list.insert(0, “new”) inserts “new” at the beginning of the list. To add multiple items at
#once, you can use the extend() method or the + operator to concatenate two lists2.

##Remove items: You can remove items from a list by using the remove() method, which removes
#the first occurrence of a specified value. For example, list.remove(“old”) removes “old”
#from the list. You can also use the pop() method to remove and return an item at a
#specific position. For example, list.pop(0) removes and returns the first item of the list.
#If you don’t specify a position, pop() removes and returns the last item of the list.
#To delete an item without returning it, you can use the del keyword or the clear() method.
#For example, del list[0] deletes the first item of the list, and list.clear() deletes all
#items from the list2.

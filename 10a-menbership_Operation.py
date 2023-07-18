Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Operacao Pertencimento - Sequencia
>>> 
>>> #Valor e Sting
>>> #1-valor
>>> 
>>> 3 in [1,2,5]
False
>>> 5 in range(10)
True
>>> 'z'not in 'banana'
True
>>> 
>>> #String
>>> 
>>> 'ana' in 'banana'
True
>>> 'ara' in 'Araraquara'
True
>>> 'ara ' not in 'Araraquara'
True
>>> 'ara' not in 'Araraquara'
False

#The membership operation in Python is used to check if a value or object is contained
#in a collection, such as a list, a tuple, a set or a string1. The membership operation uses the operators in and not in, which return a
#boolean value (True or False) depending on the result of the check2. For example:

lista = [1, 2, 3, 4]
print(2 in lista) # True
print(5 not in lista) # True


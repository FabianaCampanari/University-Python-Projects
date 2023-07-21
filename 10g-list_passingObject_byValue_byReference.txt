##Passagem de objeto por valor referencia 
#Teste objetos Mutaveis e Imutaveis,
#Visualizar no Py Tutor

def teste(n, s):       #crio a funcao
    n = n + 2
    s[0] = s[0] + 1 #testa com
    return

n1 = 1  #codig principal,crio var n1 e
lista = [1]  # crio lista

teste(n1, lista) #chamo a funcao teste q nao tem retorno
                 #portanto nao é preciso guardar o valor dela
print('fim')     #no print nao atribuimos o resultado do print a uma variaves


##Passing object by value is a way of passing arguments to a function that creates
#a copy of the object’s value and passes it to the function. This means that any
#changes made to the object inside the function will not affect the original object
#outside the function.
#For example, if a function receives an integer argument
#by value,it will not be able to modify the original integer variable that was passed
#to it.

##Passing object by reference is a way of passing arguments to a function that passes
#a reference to the object’s memory address and not its value. This means that any
#changes made to the object inside the function will affect the original object outside
#the function.
#For example, if a function receives a list argument by reference,it will
#be able to modify the original list variable that was passed to it.

##Mutable objects are objects that can be changed after they are created,such as lists,
#dictionaries, sets, etc.
#Mutable objects can be modified by adding, removing, or changing their elements.
#For example, list.append(x) is a method that modifies a mutable list object by adding
#an element x to it.

##Immutable objects are objects that cannot be changed after they are created, such as
#integers, strings, tuples, etc. Immutable objects cannot be modified by any method or
#operation. For example, str.upper() is a method that returns a new string object with
#all uppercase letters, but does not modify the original immutable string object.

#[Repeat Until]
#Crie u orograma que receba um numero n>= 0 e exiba o
#valor da raiz quadrada de n.
#Enquanto n for um numero negativo,repita a solicitação
#de entrada

from math import sqrt  #1

while True:  #2
    n = float(input('Type a Number:  '))  #3
    if n >= 0: break  #4

print(f'Square Root de {n} é {sqrt(n)}') #5

###Para iniciarmos lembrar q raiz quadrada nesse contexto
###só faz sentido para um numeroa > ou = (>=)a 0
###O comando Py da raiz quadrada é-- sqrtwtecamath 
## 1- importar de math a funçao sqrt
###Enunciado solicita q a validaçao seja feita, ou seja,
###só aceitará valor positivo ou 0, portanto:
## 2-Enquanto Verdadeiro,
## 3- n recebera um float.
## 4-Verficar se esse valor esta de acordo, se for maior
##ou igual a 0 (se for Verdade)o laço serea encerrado(Break)    
###Se não,como é um while True:o fluxo de exec será retomado p/ a condição que é sempre True e de novo será
#solicitando um valor p/ o usuar.
## 5-Por fim qdo o loop for encerrado será certo queo usuar.
#inseriu um valor de acordo c/ o q foi proposto desde o
#inicio, ou seja, valor >=0   
   

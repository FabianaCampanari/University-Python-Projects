#BREAK
#Crie um programa que receba um número natural n
#(n>1) e exiba uma mensagem indicando se (n) é primo.
#num. primo é um num.natural maior q 1 e apenas
#divisivel por 1 e por ele mesmo, ou seja só tem 2 divisores).


n = int(input('Type a number: '))
divisor = 2
while divisor < n:    #1
     print(f'{n} % {divisor} = {n % divisor}') #2
     if  n % divisor == 0:                                       
        break
     divisor += 1       #3

if divisor==n:
    print('is a prime number')
else:
    print('not a prime number')



#1 equivale dizer divisor  <= n-1
#2 mostra cada rodada do laço
#3 incrementado de 1 em 1    

#Estrategia:Verificar se o numero nao tem divisores do 2
#até n-1, por exemplo:7, nao preciso contar qtos divisores
#tem , dividindo por 2,3,4,5 e 6(n-1) se nao encontrar
#nenhum divisor 7 c/certeza é primo.Se encontrar algum
#divisor entre 2 e n-1, posso interromper o laço antes pq
# c/ certeza esse numer nao é primo, usaremos o break
#nesse contexto.
#Enquanto for verdade q divisor  < n
#Verificaremos se n é divisivel pelo divisor---
#-- (if n % divisor ==0:) e caso seja verdade esse num
#nao é primo e podemos encerrar o laço prematuramente.
#Caso nao seja verdade iremos p/ proximo divisor-----
#-- divisor += 1
#Esse laco pode ser encerrado por 1 das 2 condicoes:
#Ou pq a condicao while resultou False e i divisor ficou
#maior oo igual a n, encerrado aloaco
#Ou pq a condicao do if resultou Verdadeiro,ou seja, o
#num. é divisivel pelo divisor a estara entre 2 e n-1e ai
#encerramos o laço.
#Sao 2 formas de encerrar o laco nesse exemplo.
#Se o laco encerrou por causa da condicao---
#---while divisor < n:--é pq foram testados todos os
#divisores de 2 até n-1 e nao encontramos nenhum e
#como o divisor é incrementado de 1 em 1 é certeza q
#quando a condica while der Falsa o divisor vale o mesmo
#valor de n,entao:
#Posso perguntar se o divisor é igual a n--if divisor ==n:
#Se for verdade exibo a mensagem print('prime number')
#Caso nao seja imprimo print('not a prime number'), pq
#se a condicao--if divisor == n:nao for verdade é pq o loop
#tefrminou por causa do--if n% divisor == 0:e nesse caso
# o numero nao é primo.


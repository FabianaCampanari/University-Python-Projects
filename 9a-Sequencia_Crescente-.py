#LAÇO FOR (SEQUENCIAS)

#Crie um programa que solicite ao usuario um
#número natural e exiba a sequência crescente de
#um até o número dado.


n = int(input(' Type a Number:  '))#
for i in range(1, n-1): #2 
    print(i, end=' ')
    



# 1- valor digitado pelo usuario

# 2- O enunciado pede uma sequencia de 1 até n (1, n+1),
#entao nao posso escrever no range (1, n) pois o range
#é um intervalo aberto até a direta,segundo essa regra
#se usasse range (1, n) seria asim --[1..n[--, ou seja,
#o n ficaria de fora e nao ficaria incluso por isso uso
#n +1 q é para incluir o valor de n--[1..n+1[

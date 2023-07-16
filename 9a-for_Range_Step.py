#LAÇO FOR (SEQUENCIAS)

#Crie um programa que solicite ao usuário um
#número natural e exiba a sequência crescente de
#zero até o número dado, somente os pares

    
n = int(input('Type a Number:  '))#1
for i in range(0, n+1, 2):   #2
    print(i, end=' ')


# 1- n digitadp pelo usuario

# 2- No intervalde 0 ate n+1(pois quero incluir o valor
#de n),porem é só para mostrar os numeros pares, entao
#começo em 0 que é um numero par e vou somando de 2 em 2
#uso o(passo 2)----for i in range(0, n+1, 2):----



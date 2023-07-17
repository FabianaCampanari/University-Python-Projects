#Programa que exibe os pares e ímpares de um intervalo (com for).

# Crie um programa que exiba, em ordem crescente, os pares de 10
# até 100 e, em ordem decrescente, os ímpares de 100 até 10.



for par in range(10, 101, 2) :
    print(par, end=' ')

print()

for impar in range (99, 10, -2):
    print(impar, end=' ')

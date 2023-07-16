#WHILE - LISTA E USO DA VARIAVEL COMO INDICE P/ ALTERA-LA
#DE ACORDO COM INDEXAÇ˜AO

#Crie um programa que receba como entrada quatro salários,
#exiba a média salarial e os salários abaixo da média”.


salarios = [0,0,0,0]
soma = 0

i = 0     #variavel q sera usada como indice
while i < 4:
    salarios[i] = float(input('Salary: USD: '))
    soma += salarios[i]
    i += 1

media = soma / 4
print(f'Pay off Average = USD: {media:.2f}')

i = 0    #variavel q sera usada como indice
while i < 4:
    if salarios[i] < media:
        print(f'Salary below average: USD: {salarios[i]:.2f}')
        i += 1

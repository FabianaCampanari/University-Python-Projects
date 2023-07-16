#For - LISTA E USO do append() que anexa ao final da
#própria lista um novo item.

#Mesmo programa do 9E- while_lista_variavel porem com
#For e append()

#Crie um programa que receba como entrada quatro salários,
#exiba a média salarial e os salários abaixo da média”.



salarios = []
soma = 0

for _ in range(4):  #para cada item da sequencia,faça..
    salario = float(input('Salary = USD: '))
    soma += salario
    salarios.append(salario)

media = soma /4
print(f'Salary Average is = USD: {media:.2f}')

for salario in salarios:
    if salario < media:
        print(f'Salary below average: USD: {salario:.2f}')


    
#foram usados dois laços for:
        
# I-um para receber os valores dos salários,acumulá
#-los na variável soma e adicioná-los à lista

# II-percorrer a lista de salários e exibir os
#inferiores a média.No segundo laço, percorremos
#a lista de salários, independente do seu tamanho,
#e os valores dos itens serão usados para algo,
#no caso uma exibição condicionada a uma verificação.
#Portanto, foi adotado um identificador que faz
#referência ao conteúdo da lista, só que agora no
#singular, pois está representando apenas um item da
#lista por vez.

##Note que o nome da variável referencia seu
#conteúdo e está no plural, indicando que é uma
#sequência de salários.

##Note que a função range retorna um intervalo[0..4[,
#e portanto o laço será executado 4 vezes, como
#usamos append para incluir os itens na lista, não
#precisamos nos preocupar em gerenciar índices.

##Note que primeiro laço, usamos como identificador
#da variável de controle apenas um sublinhado (_),
#esse identificador é comum quando o objetivo do
#aço é apenas ser executado um número fixo de vezes
#,sem pretensão de usar os valoresda sequência
#atribuídos à variável de controle.

# 

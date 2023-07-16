#LAÇO FOR (SEQUENCIAS)

#Crie um programa que solicite ao usuário um
#número natural e exiba a sequência decrescente
#do número dado até um.



n = int(input('Type a number:  ')) #1
for i in range(n, 0 ,-1):
    print(i, end=' ')
    


# 1-Num. digitado pelo usuario

# 2-Para exibir a sequencia uso for i in range partindo
#de n e iremos ate o valor 1, porem o intervalo é
#decrescente e todo intervalo feito com range é aberto
#à direita,entao caso escreva (n, 1, -1):
#é o mesmo que: partir de n e nao chegar no 1--[n,..1[, ou
#seja, pararia no 2. Como preciso que va ate o 1 serei
#obrigado a colocar 0(n - 1), pq assim parte do n e nao chega no
#0 pois é decrescente, entao para no 1.

#PS: o -1 é usado no range para a exibir a sequencia
#DECRESCENTE



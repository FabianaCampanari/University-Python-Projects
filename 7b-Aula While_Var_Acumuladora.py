#[VARIÁVEL CONTROLADORA]

#Dados varios numeros inteiros,exibir a media dos numeros
#lidos. A entrada termina com a leitura do numero -1 que
#nao deve ser contabilizado.
soma = 0
qtd = 0
n= int(input('Please type a number:'))
while n != -1:
        soma += n
        qtd += 1
        n = int(input('Please type another number '))
print(f'The average is: {soma/qtd}')
     
#Raciocionio:
#-Para calculo de media precisamos da soma dos valores
#e da quantidade de valores e fazer uma divisao
# 1-A variavel soma comeca c/ 0 pois nenhum valorfoi dado
#ainda
#2-A qtd tambem comeca c/ 0 pois nenhum valor foi
# dado pelo usuario ainda.
#3-Peço p/ usuario0 1˙ valor,n= int(input('Digite um número:'))
#4- Verifico a partir do laço while se o num nao é o -1, já
#há uma garantia q -1 só pode ser dado ao final e q temos
#uma entrada q nao é o -1.Entao verifico se n != de -1 e
#enquanto isso for verdadeiro nós somaremos o valor q o
#usuario digitou na variavel soma ---  soma += n e claro tb
# aumentamos a qtd ---- qtd += 1
#5-Apos o loop encerrar  pedimos ao usuario um
#novo valor ----n= int(input('Please type another number '))
#E por fim pode mos calcular a media dividindo a soma
# pela quantidade-------print(f'The average is: {soma/qtd}')
#6-Resumo:
#-enquanto 'n != -1 for Verdade, óu seja enqanto usuario nao
#informar - 1;nos acrescentamos valor na soma---soma += n
#aumentamos a qtd--- qtd += 1 e pedimos um novo valor p/
#usuario----   n = int(input('Please type another number '))
#ATENCAO: a ordem da solicitacao do novo valor qé feita p/
#usuario, NESSE PROGRAMA tem q ser no final pq só posso
#somar esse valor na var soma qdo tenho certeza que ele
# é diferente de - 1-----n != -1

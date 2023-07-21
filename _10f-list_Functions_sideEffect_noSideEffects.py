#10_Apostila pg 19

#Execute o código da Codificação 10.34 no Py Tutor.
#Se ainda estiver na mesma janela em que testou a
#Codificação 10.33, ao editar o código e antes de
#visualizar a execução, retorne a renderização dos
#objetos na memória para a configuração padrão:
#inline primitives, don’t nest objects [default].
#Mesmo que omita alguns detalhes, essa configuração
#torna mais simples a visualização.
#Observe na Codificação 10.34 que na função com efeitos
#colaterais não há retorno de valor, pois as alterações
#são feitas no objeto original, enquanto na função sem
#efeitos colaterais, atribuímos o valor retornado a uma
#variável para guardá-lo e usá-lo.

#Funcão com efeitos colaterais

def converte 1(lista):
    for i in range(len(lista)):
    lista[i] = int (lista[i])

    

# Função sem efeitos colaterais

def converte_2(lista):
nova lista = []
    for item in lista:
    nova lista.append (int (item))
    return nova lista

numeros_1 = ['10','20','30','40']
numeros_2 = ['10','20,'20','30','40']

converte_1(numeros 1)
numeros_3 = converte_2(numeros_2)
             
print (f'lista 1: {numeros_1}', f'lista 2: {numeros_2}',
f'lista 3: {numeros_3}', sep='\n')

##A function with side effect is a function that changes the state of something
#outside of its own scope, such as a global variable, a file, or an object passed as
#an argument.
#For example, print(x) is a function with side effect because it writes
#something to the standard output, which is outside of its own scope.
             
##A function without side effect is a function that does not change the state of
#anything outside of its own scope, but only returns a value based on its input.
#For example, len(x) is a function without side effect because it only returns the
#length of x, without modifying x or anything else.
      

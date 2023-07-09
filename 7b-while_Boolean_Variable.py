#Codificação 7.12: Programa com loop controlado por flag booleana.
#[VARIAVEL FLAG BOOLEANA]
#Crie um programa que peça ao usuário preços
#de produtos comprados até que ele decida
#encerrar a compra. O programa, ao final, deve
#exibir o total gasto

total = 0 #variavel acumuladora
quero_comprar = True  #sera usada como flag boolena no loop

while quero_comprar:
    preco = float(input('Price: '))
    total += preco
    opcao = input('Keep Shopping (s/n)? ')
    if opcao != 's':
        quero_comprar = False
print(f'Total Shopping R$ {total: .2f}')
                 





#1- Incio pela var total qu e vai armazenar o total dos
#precos que o usuario inserir
#2-Criar flag booleana q começa c/ True p/ possibilitar
#q usuar. compre pelo menos 1 item--quero_comprar = True
#Criar Loop While q enquanto a var quero_comprar estiver
#valendo True, pediremos p/usuar. 1 preço-- preco = float(int(input('Price: '))
# depois acumularemos esse preço na var total-- total += preco
#Depois daremos opcão p/ q usuar possa ou nao continuar
#comprando---opcao = input('Keep Shopping (s/n)?
#NOTA:por mais que usuar. nao queira comprar algo, ele tem
#que digitar algo verificaçao e ver se usuar. digitou qqer coisa
#diferente de s,"s' é p/ continuar comprando e qqur coisa
#de "s q ele tenha digitado a compra sera finalizada, entao:
#--- if opcao != 's':se for diferente a var quero_comprar perde
#o valor q era True e sera atribuido valor False--
#---quero_comprar = False
#Nomomento q usuar digitar qqrer coisa != de s; quero_comp
#recebe False e a condicao do laço(quero_comp:)for avaliada
#novamente ela resultara em F e o lacco tb
#Qdo laco termina podemos exibir o total da compra
#e o total com 2 casa depois do ponto (.2f )p/ asemlhar
#com valor monetario

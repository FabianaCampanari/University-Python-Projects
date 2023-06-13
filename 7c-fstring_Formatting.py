#Crie um programa para um site ! O programa devera solicitar
# o valor de um item e a quantidade de unidades compradas
# deste item, ao final deve exibir o total com desconto de
# 10%. Considere que a quantidade será um numero
#natural positivo.

# valor = float ( input ( 'Valor do item:  ' ))
# qtd = int ( input ( 'Quantidade:  ' ))
# total = valor * qtd
# desconto = total * 0.10
# total_final = total - desconto
# print ( ' Total com desconto: R$ ' , total_final )
# Poderia ser assim mas para melhor formataçãousar string formatada:
# Usar f no inicio( antes apostrofo , apago 0 2* apostrofo, apagar a virgula, 
#colocar total_final entre {}, fechar aspas e fechar parentêsis. 
# Para formatar  total_final com duas casas utilizo  : .2f  - { total_final : .2f }
# Ficara assim:
# print ( f' Total com desconto: R$  { total_final : .2f }')

valor = float ( input ( 'Valor do item:  ' ))
qtd = int ( input ( 'Quantidade:  ' ))
total = valor * qtd
desconto = total * 0.10
total_final = total - desconto
print (f' Total com desconto: R$ ' , total_final )

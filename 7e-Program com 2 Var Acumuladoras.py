credito = float (input ('Seu crédito: ')) # variável acumuladora
total = 0 # variável acumuladora
preco = float (input('Preco do item: '))
while credito >= preco:
       total += preco
       credito -= preco 
       preco = float (input ('Preço do item: '))
print(f" Total da compra: R$ {total .2f})
print(f" Crédito restan e: R$ {credito:.2f}")
#APOSTILA AULA 7

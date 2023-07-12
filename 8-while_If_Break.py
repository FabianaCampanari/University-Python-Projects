#Crie um programa que receba como entrada o crédito de um cliente
#e depois o preço de itens comprados por esse cliente,o programa
#deverá parar de solicitar novos preços quando o crédito disponível
#for insuficiente para pagar um dos itens.Ao final, exiba o crédito
#restante.
credito = float(input('Seu crédito: R$ '))
while credito > 0:
    item = float(input('Preço do item: R$ '))
    if item > credito:
        print('Compra negada! Ultapassa seu credito.')
        break
    credito -= item
print(f'Crédito restante: R$ {credito:.2f}')

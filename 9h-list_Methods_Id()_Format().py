
frase = 'Whe are all {}!'

>>>frase
'Whe are all {}!'
>>>id(frase)
4477449200
>>>frase.format('one')
'Whe are all one!'

#O método id é uma função interna do Python que retorna a identidade
#de um objeto como um número inteiro1. O método .format() é um método
#de string que permite criar uma string que contém campos entre chaves
#que são substituídos pelos argumentos de format

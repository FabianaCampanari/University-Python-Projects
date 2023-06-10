## Funcoes ##
## idade = int(input ( 'Digite sua idade: ' )) ##
def pede_idade(mensagem):
    """Funçao que pede a idade do usuario
outras informaçoes ...
"""
    idade = int(input(mensagem))
    return idade

## Codigo Principal ##
## idade = int(input ( 'Digite sua idade: ' )) ##

idade = pede_idade('Digite sua idade: ')

if idade > 18:
    print ( 'Você tem mais de 18 anos ')    
else:
    print ( 'Você tem menos de 18 anos')
print ('Fim')    


## Codigo Inicia Assim ##

# idade = int(input ( 'Digite sua idade: ' )) 
# maior_de_idade = idade > 18

# if maior_de_idade:
 # print ( 'Você tem mais de 18 anos ')    
# else:
   # print ( 'Você tem menos de 18 anos')
   
# print ('Fim')    




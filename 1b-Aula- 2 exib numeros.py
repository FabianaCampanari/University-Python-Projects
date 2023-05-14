# Crie um pgrama que receba dois numeros naturais e exiba uma
# msg indicando se o promeiro é divisivel pelo segundo

a = int( input( 'Primeiro: '))
b = int( input( 'Segundo    '))
print( f' {a} é divisivel por {b}: { b != 0 and a % b ==0 }')
#Inverte a segunda chave
print( f' {a} é divisivel por {b}: { b ==0  and a % b != 0 }')
        

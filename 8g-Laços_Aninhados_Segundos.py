#[LAÇOumaS ]
#Crie uma função que simule um relogio digital exibindo
#desde 00:00:00 até 23:59:59


def relogio():   #1
    s = 0    #2
    while s < 60:    #3
        print(f'{0:02}: {0:02}: {s:02}') #4  #5  #6
        s += 1
                             
        
                




# 1-Inicar criando a função relogio q é uma funcão que não
#que nao tem parametros.

# 2-cria variavel s(segundos).

# 3-Enquanto o s for menor que 60;

##Será impresso o relogio digital.

# 4- colocando 0 hora e exibido c/ 2 digitos portanto
#formatação 02; --{0:02};para parecer um relogio digital.

# 5- colocando 0 hora e exibido c/ 2 digitos portanto
#formatação 02; --{0:02};para parecer um relogio digital.

# 6- colocando o s tb com formatação 02 para mostrar
#2 digitos mesmo qdo s fou um numero que ocupe apenas
#1 digito.

# 7- E por fim, incrementaremos a variavel s, para que
#ela valha o segundo seguinte.

##Executar e na Shell, chamar pela fun˜cao-- relogio()

#[LAÇOS ]
#Crie uma função que simule um relogio digital exibindo
#desde 00:00:00 até 23:59:59


def relogio(): #1
    h = 0  #--12----
    while h < 24:  #--13
        m = 0  ###8
        while m < 60: ###9
            s = 0 #2
            while s < 60: #3
               print(f'{h:02}: {m:02}: {s:02}') #--15----
            s += 1 #7
            m += 1  ###11
        h += 1 #--14--        
        
                             

# 1-Inicar criando a função relogio q é uma funcão que não
#que nao tem parametros.

# 2-cria variavel s(segundos).

# 3-Enquanto o s for menor que 60;
## print(f'{0:02}: {0:02}: {s:02}')#4 #5 #6
# #print(f'{0:02}: {m:02}: {s:02}')###10

##Será impresso o relogio digital.

# 4- colocando 0 hora e exibido c/ 2 digitos portanto
#formatação 02; --{0:02};para parecer um relogio digital.

# 5- colocando 0 hora e exibido c/ 2 digitos portanto
#formatação 02; --{0:02};para parecer um relogio digital.

# 6- colocando o s tb com formatação 02 para mostrar
#2 digitos mesmo qdo s fou um numero que ocupe apenas
#1 digito.

# 7- e por fim, incrementaremos a variavel s, para que
#ela valha o segundo seguinte.

##Executar e na Shell, chamar pela fun˜cao-- relogio()e sera
#exibido do 00:00:00 até 00:00:59

#--------MINUTOS------------------------------------#

# 8-para cada 1 min esse laço de segundos tem q se repetir,
#mas mostrar 60 minutos (desde 0 min até 59 min)-- m = 0.

# 9-enquanto m < 60 iremos executar a versao primeira da
#funcao relativa aos segundos.

# 10-a parte de minutos nao sera mais 0 e sim m.

# 11-a cada 60 minutos incrementaremos os minutos-- m += 1
## Executar e chamar a funcnao relogio ()e aparecera tb os
#minutos

###O IMPORTANTE NESSE EXERCICO, é notar q para cada uma
#rodada do laço mais externo (###9), executa-se uma execucao
#completa do laco while mais interno, ou seja, uma rodada do
#mais externo equivale a 60 rodadas do mais interno.

#------------HORAS----------------------------------#

# 12-criar variavel h valendo 0 (zero horas)

# 13-enquanto h < 24, executaremos o laço de minutos para
#cada hora, ou seja , a cada uma hora 60 minutos
#(SEMPRE ARRUMAR IDENTACAO QUA ANINHAE FUNCOES !

# 14- depois incrementaremos a variavel h

# 15-Volocar h na variavel de horas do print


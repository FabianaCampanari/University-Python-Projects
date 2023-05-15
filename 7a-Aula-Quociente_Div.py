#[VARIÁVEL CONTADORA]
#Dados dois números inteiros p (≥0) e q (>0),
#exibir o quociente da divisão inteira de p por q
#sem usar operadores de divisão e multiplicação.
p=int(input('p: '))    #usuario digita p
q=int(input('q: '))    #usuario digita q
contador = 0
while p >= q:
    p = p - q      #  p -= q
    contador += 1    # +1 pois consegui fazer +1 subtacao e por
#ser a ultima instruç do while qdo é executada o fluxo da
#execução retorna p/ expessao do while (cond while) e segue
# executando ate dar False
print(f'O quociente da divisão é {contador}')          


# ESTRATEGIA DO RACIOCINIO
#Dividir é o mesmo que subtrair diversas vezes Exemplo:
# 7 // 2 é o mesmo que subtrair 3 (quociente)x sem
# que de negativo.E a estrategia aqui é CONTAR qtas x consegui
# subtrair 2, no caso "q", do "p" --- p-q = ? (p -= q), para isso
# preciso de um contador que comeca com 0 pois nesse ponto
# do codigo nao consegui subtrair nada pois ainda nao recebi
# os valores do usuario (input), 0 é neutro assim como para soma
# e para o produto o valor neutro é 1
# 7-2
# 5-2
# 3-2
# 1-2
# -1
# apos isso escrever condicao while que enquanto p >= q: 
# (podemos fazer uma subtracao) entao basta subtrarir p de q
# p = p - q   ------- p -= q

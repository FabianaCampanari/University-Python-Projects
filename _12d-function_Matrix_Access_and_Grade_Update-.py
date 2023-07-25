'''
Codificação: Atualização de notas com acesso à matriz por sua linha e coluna

A codificação define uma função chamada atualiza_notas_3 que recebe um parâmetro
chamado turma. Espera-se que turma seja uma lista de listas que represente uma
matriz de notas. A função multiplica cada elemento na matriz por 2.

O código percorre cada elemento da matriz turma, multiplica-o por 2 e atualiza
o valor no local. Após a execução dessa função, as notas na matriz turma serão
dobradas.

'''


def atualiza_notas_3(turma):
    for linha in range(len(turma)):
        for coluna in range(len(turma[linha])):
            turma[linha][coluna] *= 2


'''
Grade Update with Access to Matrix by Row and Column.

The code defines a function named atualiza_notas_3 that takes a parameter turma,
which is expected to be a list of lists representing a matrix of grades.
The function multiplies each element in the matrix by 2.

The code iterates over each element in the turma matrix, multiplies it by 2, and
updates the value in-place.
After executing this function, the grades in the turma matrix will be doubled.
''' 

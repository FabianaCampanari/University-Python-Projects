
'''
Este código realiza um loop em uma matriz para atualizar as notas:

Neste código, a função atualiza_notas_3 recebe uma matriz turma como entrada.
Ela itera sobre cada linha usando a variável linha e cada coluna dentro dessa
linha usando a variável coluna. Em seguida, ela multiplica cada nota por 2 para
atualizar a nota no lugar dentro da matriz.

Certifique-se de passar a matriz correta para a função atualiza_notas_3 para
atualizar as notas dentro da matriz conforme necessário.
'''


def atualiza_notas_3(turma):
    for linha in range(len(turma)):
        for coluna in range(len(turma[linha])):
            turma[linha][coluna] *= 2


'''
The code you provided performs a loop over a matrix to update the grades:

This code, the function atualiza_notas_3 takes a matrix turma as input. It iteratover
each row using the linha variable and each column within that row using the coluna
variable. It then multiplies each grade by 2 to update the grade in place within the
matrix.

Make sure to pass the correct matrix to the function atualiza_notas_3 in order to
update the grades within the matrix accordingly.
'''

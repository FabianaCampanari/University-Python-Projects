
# Código corrigido do programa completo para coletar notas e exibir as
# médias dos alunos:

# Nesse código, foram feitas as seguintes correções:

# A função coleta_notas() foi corrigida para converter as notas em floats
#corretamente.
# A função preenche_turma() foi corrigida para adicionar os alunos corretamente
#à turma.
# A função calcula_media() foi corrigida para calcular corretamente a média do aluno.
# A função resumo_turma() foi corrigida para exibir corretamente as notas e médias
#dos alunos.
# Certifique-se de fornecer as notas corretamente ao digitar cada nota separada por
#espaço.

'''
Abaixo exemplo da codificaçao da Matriz:

Quantidade:4
1・aluno: 5.5 7.0 8.7
2・aluno: 8.0 6.0 9.2
3・aluno: 7.8 8.3 8.5
4・aluno: 0.0 9.9 9.1
notas: [5.5, 7.0, 8.7] | média: 7.07
notas: [8.0, 6.0, 9.2] | média: 7.73
notas: [7.8, 8.3, 8.5] | média: 8.20
notas: [0.0, 9.9. 9.1] | média: 6.33

'''


def coleta_notas():
    notas = input().split()
    for i in range(len(notas)):
        notas[i] = float(notas[i])
    return notas

def preenche_turma(qtd_alunos):
    turma = []
    for i in range(qtd_alunos):
        print(f'Aluno {i+1}:', end=' ')
        aluno = coleta_notas()
        turma.append(aluno)
    return turma

def calcula_media(aluno):
    soma = sum(aluno)
    return soma / len(aluno)

def resumo_turma(turma):
    for aluno in turma:
        media = calcula_media(aluno)
        print(f'Notas: {aluno} | Média: {media:.2f}')

qtd_alunos = int(input('Quantidade: '))
turma = preenche_turma(qtd_alunos)
resumo_turma(turma)

'''

Corrected code of the complete program to collect grades and display the averages of the students:

In this code, the following corrections were made:

The function coleta_notas() was fixed to convert the grades to floats correctly.
The function preenche_turma() was fixed to add the students correctly to the class.
The function calcula_media() was fixed to calculate the student's average correctly.
The function resumo_turma() was fixed to display the grades and averages of the students correctly.
Make sure to provide the grades correctly by typing each grade separated by a space.

Below is an example of the Matrix encoding:

Quantity: 4
1・student: 5.5 7.0 8.7
2・student: 8.0 6.0 9.2
3・student: 7.8 8.3 8.5
4・student: 0.0 9.9 9.1
grades: [5.5, 7.0, 8.7] | average: 7.07
grades: [8.0, 6.0, 9.2] | average: 7.73
grades: [7.8, 8.3, 8.5] | average: 8.20
grades: [0.0, 9.9. 9.1] | average: 6.33
'''

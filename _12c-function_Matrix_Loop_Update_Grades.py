'''
Crie uma funcão que receba como argumento uma matriz de notas em que cada
linha representa as notas de um aluno em escala zero a dez. A função deve
atualizar a matriz para a escala zero a vinte, mantendo a proporção.
'''

''''
Nesse código, a função atualiza_notas_1 recebe uma turma (matriz de notas dos alunos)
como parâmetro. Em seguida, ela itera sobre cada aluno e cada nota dentro de cada
aluno, multiplicando cada nota por 2 e adicionando a nota atualizada à lista
aluno_atualizado. Por fim, a lista aluno_atualizado é adicionada à lista
turma_atualizada. Ao final do loop, a função retorna a turma atualizada.

Certifique-se de chamar a função atualiza_notas_1 passando a turma correta como
argumento para obter a turma atualizada.
'''


def atualiza_notas_1(turma):
    turma_atualizada = []
    for aluno in turma:
        aluno_atualizado = []
        for nota in aluno:
            aluno_atualizado.append(nota * 2)
        turma_atualizada.append(aluno_atualizado)
    return turma_atualizada

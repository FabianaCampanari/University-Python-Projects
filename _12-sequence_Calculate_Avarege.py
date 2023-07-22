# Here is an example Python code to calculate the average of students based
# on four calls to the calcula_media function. Let's assume that the calcula_media
# function takes a list of grades as a parameter and returns the average of those
# grades.

'''
This example considers four students with their respective grades in each of the
four calls to the calcula_media function. In the end, we calculate the overallaverage of the students by dividing the sum of individual averages by 4.

Please note that this is just a simple example to calculate the average of students.
Depending on your specific needs, the implementation may vary.
'''


def calcula_media(notas):
    total = sum(notas)
    media = total / len(notas)
    return media

# Lista de notas dos alunos
notas_aluno1 = [7.5, 8.0, 6.5, 9.0]
notas_aluno2 = [6.0, 7.5, 8.5, 7.0]
notas_aluno3 = [8.0, 7.0, 9.5, 8.5]
notas_aluno4 = [7.5, 9.0, 8.0, 7.0]

# Chamadas à função calcula_media
media_aluno1 = calcula_media(notas_aluno1)
media_aluno2 = calcula_media(notas_aluno2)
media_aluno3 = calcula_media(notas_aluno3)
media_aluno4 = calcula_media(notas_aluno4)

# Cálculo da média geral dos alunos
media_geral = (media_aluno1 + media_aluno2 + media_aluno3 + media_aluno4) / 4

# Exibição dos resultados
print("Média do aluno 1:", media_aluno1)
print("Média do aluno 2:", media_aluno2)
print("Média do aluno 3:", media_aluno3)
print("Média do aluno 4:", media_aluno4)
print("Média geral dos alunos:", media_geral)


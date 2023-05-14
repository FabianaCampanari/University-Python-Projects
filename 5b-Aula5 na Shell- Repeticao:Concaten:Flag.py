Python 3.11.3 (v3.11.3:f3909b8bc8, Apr  4 2023, 20:12:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> ' olá ' + ' mundo
... SyntaxError: incomplete input
... ' olá ' + ' mundo '
... ' olá  mundo '
... 'olá ' + 'mundo'
... 'olá mundo'
... 'olá' + ' mundo'
... 'olá mundo'
... # Os casos acima são chamados de Strins literal,
... # Abaixo snao os casos de string apartir de uma variável, ode o acesso da string ocorre por dentro de uma variável
... #Exemplo
SyntaxError: unterminated string literal (detected at line 1)
>>> palavra_1 = 'olá'
>>> palavra_2 = 'mundo'
>>> palavra_1 + palavra_2
'olámundo'
>>> #Aconcatenação nã altera o valor original, veja exemplo abaixo
>>> palavra_1
'olá'
>>> palavra_2
'mundo'
>>> # REPETIÇÃO (*)
>>> 'w' * 3
'www'
>>> # Repetição tb funciona com a variavel
>>> 3 * palavra_1
'oláoláolá'
>>> # Comparação
>>> 'a' < 'b'
True
>>> 'a' < 'b'
True
>>> 'a' > 'b'
False
>>> 'a' == 'b'
False
>>> 'a' != 'b'
True
>>> # O Py tem a função (ord) que diz o codogo de cada letra
>>> # é uma função () embutida
>>> ord('a')
97
>>> ord('b')
98
>>> 'aaa' < 'aaa'
False
>>> 'aaa' <= 'aaa'
True
>>> 'aaa' < 'aab'
True
>>> # ATENÇÃO NA COMPARACAO DE STRING NUMERO '12' E NUMERO DIGITO pois valor é diferente, string numero usa valor do ord() o nemero vale ele mesmo
>>> '12' > '9'
False
>>> 12 > 9
True
ord('12')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    ord('12')
TypeError: ord() expected a character, but string of length 2 found
TypeError: ord() expected a character, but string of length 2 found
SyntaxError: invalid syntax
ord('1')
49
ord('9')
57
# Formatação
f'nosso texto formatado'
'nosso texto formatado'
f'nosso texto formatado: {palavra_1}'
'nosso texto formatado: olá'
f'nosso texto formatado: {palavra_2}'
'nosso texto formatado: mundo'
f'nossotexto formatado: {palavra_1 } +{palavra_2}'
'nossotexto formatado: olá +mundo'
f'nosso texto formatado: {palavra_1 }, { palavra_2}'
'nosso texto formatado: olá, mundo'
flag = True
n = 10
f'número: {n}, flag: {flag}'
'número: 10, flag: True'
# Exemplo da flag no código

idade = int(input('Digite sua idade ' ))
maior_de_idade = idade > 18

if maior_de_idade:
  print('Você tem mais de 18 anos')
else:
  print('Você tem menos de 18 anos')

print('fim')


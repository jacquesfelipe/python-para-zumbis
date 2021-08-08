"""A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples:
os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores.
Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
"""

n = int(input("Digite qual posição da sequência deseja ver: "))

a = 1
b = 1
z = 1

while z <= n - 2 :
    a, b = b, a + b
    z = z + 1
    
print(b)
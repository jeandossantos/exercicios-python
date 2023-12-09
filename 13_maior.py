""" Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada	Exemplos de Saída
7 14 106           | 106 eh o maior

 """

# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())

maior_entre_a_b = (a + b + abs(a - b)) / 2
print(maior_entre_a_b)

maior = max(maior_entre_a_b, c)


print("{} eh o maior".format(int(maior)))
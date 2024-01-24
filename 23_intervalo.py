# -*- coding: utf-8 -*-
"""
Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Entrada
O arquivo de entrada contém um número com ponto flutuante qualquer.

Saída
A saída deve ser uma mensagem conforme exemplo abaixo.

Exemplo de Entrada	Exemplo de Saída
25.01              | Intervalo (25,50]
"""

valor = float(input())

if valor >= 0 and valor <= 25.00:
    print("Intervalo [0,25]")
    
elif valor > 25.00 and valor <= 50.0:
    print("Intervalo (25,50]")
    
elif valor > 50.00 and valor <= 75.0:
    print("Intervalo (50,75]")

elif valor > 75.00 and valor <= 100.00:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
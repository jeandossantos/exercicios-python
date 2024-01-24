# -*- coding: utf-8 -*-
valor = int(input())
valor_inicial = valor

notas = [100, 50, 20, 10, 5, 2, 1]

celulas = []

for n in notas:
    celulas.append(valor // n)
    valor = valor % n

print(str(valor_inicial))
for n in range(len(notas)):
    print("{0} nota(s) de R$ {1},00". format(celulas[n], notas[n]))
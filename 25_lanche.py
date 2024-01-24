# -*- coding: utf-8 -*-
""" Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

[https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1038_pt.png]

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

Exemplo de Entrada	Exemplo de Saída 
3 2                | Total: R$ 10.00"""

item, qtd = input().split()

items =  {
    '1': 4.0,
    '2': 4.5,
    '3': 5.0,
    '4': 2.0,
    '5': 1.5
}

total = items[item] * float(qtd)

print(f"Total: R$ {total:.2f}")
"""
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Exemplo de Entrada	Exemplo de Saída
576.73         |   NOTAS:
               |    5 nota(s) de R$ 100.00
               |     1 nota(s) de R$ 50.00
               |     1 nota(s) de R$ 20.00
               |     0 nota(s) de R$ 10.00
               |     1 nota(s) de R$ 5.00
               |     0 nota(s) de R$ 2.00
               |     MOEDAS:
               |     1 moeda(s) de R$ 1.00
               |     1 moeda(s) de R$ 0.50
               |     0 moeda(s) de R$ 0.25
               |     2 moeda(s) de R$ 0.10
               |     0 moeda(s) de R$ 0.05
               |     3 moeda(s) de R$ 0.01
"""
valor = float(input()) * 100
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

troco_em_notas = []
troco_em_moedas = []

for n in notas:
  if valor >= 200:
    troco_em_notas.append(int(valor // n))
    valor = valor % n
  else:
    troco_em_notas.append(0)

for m in moedas:
 if valor > 0:
     troco_em_moedas.append(int((valor // m)))
     valor = valor % m
 else:
     troco_em_moedas.append(0)
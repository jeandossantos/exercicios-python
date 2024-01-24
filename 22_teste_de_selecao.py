"""
Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

Entrada
Quatro números inteiros A, B, C e D.

Saída
Mostre a respectiva mensagem após a validação dos valores.

Exemplo de Entrada	Exemplo de Saída
5 6 7 8       |     Valores nao aceitos
"""
A, B, C, D = map(int, input().split())

CD = C + D
AB = A + B

if B > C and D > A and CD > AB and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

print("NOTAS:")

for tn in range(len(troco_em_notas)):
  print("{} nota(s) de R$ {:.2f}".format(troco_em_notas[tn], notas[tn] / 100))

print("MOEDAS:")

for tm in range(len(troco_em_moedas)):
  print("{} moeda(s) de R$ {:.2f}".format(troco_em_moedas[tm], moedas[tm] / 100))

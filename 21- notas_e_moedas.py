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
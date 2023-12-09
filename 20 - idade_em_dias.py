dias = int(input())

anos = dias // 365
dias_restantes = dias % 365
meses = dias_restantes // 30
dias_restantes = dias_restantes % 30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias_restantes))
horas = int(input())
km_media = int(input())
KM_POR_LITRO = 12 
litros = horas * km_media / KM_POR_LITRO

print("{:.3f}".format(litros))
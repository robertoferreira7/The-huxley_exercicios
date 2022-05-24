segundos = int(input())

horas = int(segundos / 3600)
minutos = int(segundos / 60 - horas * 60)
segundos = segundos - (horas * 3600) - (minutos*60)

print("{} h " "{} m " "{} s ".format(horas, minutos, segundos))
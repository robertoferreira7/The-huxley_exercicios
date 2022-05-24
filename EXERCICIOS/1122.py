entrada = input()
media, totalAulas, faltas = entrada.split(" ")
media  = float(media)
totalAulas = int(totalAulas)
faltas = int(faltas)

presenca = totalAulas - faltas

freqencia1 = totalAulas * 0.75
freqencia2 = totalAulas * 0.50

if presenca >= freqencia1:
    if media >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
elif presenca >= freqencia2:
    if media >= 7:
        print("APROVADO")
    else:
        print("REPROVADO")
else:
    print("REPROVADO")
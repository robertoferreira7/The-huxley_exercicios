entrada = input()
quantidade, custo = entrada.split(" ")
quantidade = float(quantidade)
custo1 = float(custo)
agua = (quantidade * custo1) * 1000
esgoto = (agua / 100) * 80
valortotal = agua + esgoto
print("{:.2f}".format(agua))
print("{:.2f}".format(esgoto))
print("{:.2f}".format(valortotal))
valor_galao = float(input())
plitro = float(input())
cotacao = float(input())
galao = valor_galao/ 3.80 * cotacao

print("Gasolina EUA: R$ {:.2f}".format(galao))
print("Gasolina Brasil: R$ {:.2f}".format(plitro))

if galao < plitro:
    print("Mais barata nos EUA")

elif galao > plitro:
    print("Mais barata no Brasil")
else:
    print("Igual")
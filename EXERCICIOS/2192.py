d, r, l, p, g = input().split(" ")
d = int(d)
r = int(r)
l = int(l)
p = int(p)
g = int(g)

if d <= (l*10):
    print("Pode viajar.")
    print("R$: {:.0f}".format(r))
else:
    if d > (l*10):
        distancia_restante = d - (l * 10) #km/litros
        valor = (distancia_restante * g) / 10 #Litros/reais
        postos = d // (p+1)
        if valor <= r and (l*10) >= postos:
             print("Pode viajar.")
             print("R$: {:.0f}".format(r - valor))
        else:
            print("Nao pode viajar.")
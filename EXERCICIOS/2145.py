nacionalidade = str(input())
ocupacao = str(input())
quantidade_armas = int(input())
calibre_arma = int(input())

if nacionalidade == "E" and quantidade_armas == 0:
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "M":
    print("Liberado")
elif nacionalidade == "B" and (ocupacao == "T" or ocupacao == "O") and quantidade_armas <= 1 and calibre_arma < 23:
    print("Liberado")
elif nacionalidade == "B" and ocupacao == "C" and quantidade_armas <= 2 and calibre_arma <= 38:
    print("Liberado")
else:
    print("Barrado")
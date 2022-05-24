dias_com_carro = int(input())
km_rodados = int(input())
diaria= 30.00
taxa_km_rodado = 0.01
aluguel_normal = (dias_com_carro * diaria) + (taxa_km_rodado * km_rodados)
aluguel_desconto = aluguel_normal * 0.90
print("{:.2f}".format(aluguel_desconto))
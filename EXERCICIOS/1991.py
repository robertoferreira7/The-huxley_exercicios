kilowats = 1.5
consumo = float(input())
valor_ser_pago = consumo * kilowats
valor_com_desconto = valor_ser_pago * 0.85
print("Valor a ser pago: R$ {:.2f} reais".format(valor_ser_pago))
print("Valor a ser pago com desconto: R$ {:.2f} reais".format(valor_com_desconto))
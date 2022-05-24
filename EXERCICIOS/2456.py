genero = str(input())
anos_casa = int(input())
salario = float(input())

if genero == "h" and anos_casa >= 15:
    salario = salario * 1.20
    print("{:.2f}".format(salario))
    
elif genero == "m" and anos_casa >= 10:
    salario = salario * 1.25
    print("{:.2f}".format(salario))

else:
    salario = salario + 200
    print("{:.2f}".format(salario))
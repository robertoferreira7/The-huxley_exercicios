salario = float(input())

if salario < 280:
    print("{:.2f}".format(salario * 1.2))
    
elif salario >= 280 and salario < 700:
    print("{:.2f}".format(salario * 1.15))

elif salario >= 700 and salario < 1500:
    print("{:.2f}".format(salario * 1.10))
    
else:
    print("{:.2f}".format(salario * 1.05))
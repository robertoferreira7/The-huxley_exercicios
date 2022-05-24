salario = float(input())
bonus1 = salario * 0.75

if bonus1 < 2000:
    print("ARGENTINA")
elif bonus1 >= 2000 and bonus1 < 3000:
    print("ESPANHA")
elif bonus1 >= 3000:
    print("ALEMANHA")
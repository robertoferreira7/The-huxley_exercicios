idade  = int(input())

if idade >= 0 and idade <=10:
    print("infantil")
elif idade >= 11 and idade <= 14:
    print("junior")
elif idade >= 15 and idade <= 20:
    print("adolescente")
elif idade >= 21 and idade <= 35:
    print("jovem")
elif idade > 35:
    print("master")
    
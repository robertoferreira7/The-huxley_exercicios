temperatura = str(input())

if temperatura == "F":
    f = float(input())
    if f >= -459.67:
        c = float((f - 32) * 5/9)
        k = float((f + 459.67)* 5/9)
        print("{:.2f} C".format(c))
        print("{:.2f} K".format(k))
    else:
        print("Valor de temperatura abaixo do minimo")
elif  temperatura == "K":
    k = float(input())
    if k >= 0.0:
        c = float(k - 273.15)
        f = float((k - 273.15)* 9/5 + 32)
        print("{:.2f} C".format(c))
        print("{:.2f} F".format(f))
    else:
        print("Valor de temperatura abaixo do minimo")

elif temperatura == "C":
    c = float(input())
    if c >= -273.0:
        k = float(c + 273.15)
        f = float((c * 9/5) + 32)
        print("{:.2f} F".format(f))
        print("{:.2f} K".format(k))
    else:
        print("Valor de temperatura abaixo do minimo")
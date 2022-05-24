dia1= int(input())
co, re, de = input().split()
co = float(co)
re = float(re)
de = float(de)
dia2 = int(input())
co1, re1, ce1, de1 = input().split()
co1 = float(co1)
re1 = float(re1)
ce1 = float(ce1)
de1 = float(de1)

soma1 = float()
soma2 = float()
somatotal = float()

if dia1 >= 1 and dia1 < 20:
    co = co
    re = re * 0.90
    de = de * 0.85
    soma1 = co + re + de
    
elif dia1 == 20:
    co = co * 0.88
    re = re * 0.85
    de = de * 0.80
    soma1 = co + re + de
    
elif dia1 == 21:
    co = co * 0.83
    re = re * 0.78
    de = de * 0.73
    soma1 = co + re + de
    
elif dia1 == 22:
    co = co * 0.80
    re = re * 0.78
    de = de * 0.70
    soma1 = co + re + de
    
elif dia1 == 23:
    co = co * 0.75
    re = re * 0.71
    de = de * 0.65
    soma1 = co + re + de
    
elif dia1 == 24:
    co = co * 0.65
    re = re * 0.65
    de = de * 0.50
    soma1 = co + re + de
    


if dia2 == 25:
    co1 = co1 * 0.85
    re1 = re1 * 0.87
    ce1
    de1 = de1 * 0.90
    soma2 = co1 + re1 + ce1 + de1
    
elif dia2 == 26:
    co1 = co1 * 0.81
    re1 = re1 * 0.75
    ce1 = ce1 * 0.95
    de1 = de1 * 0.77
    soma2 = co1 + re1 + ce1 + de1
    
elif dia2 == 27:
    co1 = co1 * 0.76
    re1 = re1 * 0.70
    ce1 = ce1 * 0.88
    de1 = de1 * 0.67
    soma2 = co1 + re1 + ce1 + de1
    
elif dia2 == 28:
    co1 = co1 * 0.70
    re1 = re1 * 0.68
    ce1 = ce1 * 0.80
    de1 = de1 * 0.65
    soma2 = co1 + re1 + ce1 + de1
    
elif dia2 == 29 or dia2 ==30:
    co1 = co1 * 0.65
    re1 = re1 * 0.60
    ce1 = ce1 * 0.67
    de1 = de1 * 0.58
    soma2 = co1 + re1 + ce1 + de1
    
elif dia2 == 31:
    co1 = co1 * 0.60
    re1 = re1 * 0.53
    ce1 = ce1 * 0.55
    de1 = de1 * 0.34
    soma2 = co1 + re1 + ce1+  de1

somatotal = soma1 + soma2

print("Compras de natal: R$ {:.2f}.".format(soma1))
print("Compras de ano novo: R$ {:.2f}.".format(soma2))
print("Total das compras: R$ {:.2f}.".format(somatotal))



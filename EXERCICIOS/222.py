Cv, Ce, Cs, Fv, Fe, Fs = input().split()
Cv = int(Cv)
Ce = int(Ce)
Cs = int(Cs)
Fv = int(Fv)
Fe = int(Fe)
Fs = int(Fs)

Cv = Cv * 3
Fv = Fv * 3

soma1 = Cv + Ce
soma2 = Fv + Fe

if soma1 < soma2:
    print("F")
elif soma1 > soma2:
    print("C")
elif soma1 == soma2:
    if Cs > Fs:
        print("C")
    elif Cs < Fs:
        print("F")
    else:
        print("=")
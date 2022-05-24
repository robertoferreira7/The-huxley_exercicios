level = int(input())
if (level >= 1 and level <= 20):
    print("Potencia de : {} W".format(20 + level**3))
elif (level >= 21 and level <= 40):
    print("Potencia de : {} W".format(8000 + (level-10)**2))
elif (level >= 41 and level <= 60):
    print("Potencia de : {} W".format(9000 + 5 * level))
elif (level >= 61 and level <= 80):
    print("Potencia de : {} W".format(9300 + 2 * level))
elif (level >= 81 and level < 100):
    print("Potencia de : {} W".format(9500 + level))
nota1 = float(input("Informe a primeira nota:\n"))
nota2 = float(input("Informe a segunda nota:\n"))
nota3 = float(input("Informe a terceira nota:\n"))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Aprovado com media {:.1f}".format(media))
    
elif media >= 5 and media < 7:
    print("Recuperacao com media {:.1f}".format(media))

elif media < 5:
    print("Reprovado com media {:.1f}".format(media))
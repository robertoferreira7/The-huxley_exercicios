livros = int(input())
alunos = int(input())
calculo = alunos / livros

if calculo <= 8:
    print("A")
    
elif calculo <= 12:
    print("B")
    
elif calculo <= 18:
    print("C")
    
elif calculo > 18:
    print("D")
pergunta = input("Digite a quantida de notas existentes")

if (pergunta == "2"):
    nota1 = int(input("Digite aqui a nota:"))
    nota2 = int(input("Digite aqui a segunda nota:"))

    soma = nota1 + nota2
    final = (soma) / 2

    print(final)

if (pergunta == "3"):
    nota1 = int(input("Digite aqui a nota:"))
    nota2 = int(input("Digite aqui a segunda nota:"))
    nota3 = int(input("Digite aqui a terceira nota:"))
    
    soma = nota1 + nota2 + nota3
    final = (soma)/3

    print(final)

else:
    print(" ")




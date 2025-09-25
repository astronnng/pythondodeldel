print(" Ola cadu seja bem vindo!")

print(" O valor inteiro é:", 10)

print(f" O valor em decimal é: {10: d}")
print(f" O valor em binario é: {10: b}")

print(f" O valor de PI é:{3.14159265: f}")
print(f" O valor de PI é:{3.14159265: .2f}") #.2f usado quando for preciso limtiar a duas casas decimais


#primeiro teste usando resposta do cliente para jogar dados na tela#

nome = input("Digite seu nome: ")
print("Olá,", nome)
idade = input("Digite sua idade:")
print(f"A idade de", nome, "é:", idade)
salario = input("Digite seu salario:")
print(f"O salario de:", nome, "é:", salario)
nacionalidade=input("Digite a sua nacionalidade:")
print(f"Sua nacionalidade é:", nacionalidade)
print("\n", nome, "Contem:", idade, "anos","\n",
    "Com o salario de:", salario,"\n",
    "e a sua naciolidade é:", nacionalidade)

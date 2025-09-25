'''
i = 1

while i <= 10: # laço de I se for menor ou igual a 10 
    print(i, " ", end="")
    i += 1 # I recebe o valor dele + 1 

'''


'''
i = 10

while i >= 1: # laço de I se for menor ou igual a 10 
    print(i, " ", end="")
    i -= 1 # I recebe o valor dele + 1 

'''

numeroqualquer = int(input("Digite um numero qualquer:"))

while numeroqualquer != 0:
        print("Voce digitou:", numeroqualquer)
        numeroqualquer = int(input("Digite outro numero (0 para sair): "))

print("Programa encerrado.")
"""
for i in range(1, 11): #USADO O FOR COM RANGE PARA CONTAR ATE O 11
    if i == 5: SE O I FOR IGUAL A 5 ELE VAI PULAR O 5 E CONTINUAR  
        continue
    print(i, "", end="")
"""

"""
for i in range(1, 30):  #USADO O FOR COM RANGE PARA CONTAR ATE O 30
    if i ==10:  #SE O I FOR IGUAL A 10 ELE VAI BRECAR 
        break
    print(i, " ", end="") 
"""




"""
for a in range(0, 11):
    print(a, " ", end=" ")
if a <= 10:
    input("Digite um valor ou 0 para sair: ")
else:
    a=0
    
"""


contador = 0

for _ in range(1000):  # Laço "infinito" controlado por break
    print(f"Contador atual: {contador}")
    print("Digite 1 para incrementar o contador")
    print("Digite 0 para encerrar o programa")
    escolha = input("Sua escolha: ")

    if escolha == "1":
        contador += 1
        continue  # Vai para o início do loop

    elif escolha == "0":
        print("Programa encerrado pelo usuário.")
        break  # Encerra o loop

    else:
        print("Opção inválida. Tente novamente.")
        continue

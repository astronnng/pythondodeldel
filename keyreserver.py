import math
import os
import time

#USANDO FUNÇÕES DO MATH

x = 10 
raiz_quadrada = math.sqrt(x)
print(f"A raiz quadrada de: ", x, "é igual à:", raiz_quadrada)

angulo = 90 
seno = math.sin(angulo)
print(f"O seno do:", angulo, "é igual a:", seno)

############################

diretorio = os.getcwd()
print(f"O diretorio de onde esta sendo usado é: ", diretorio)

##seria bom se eu conseguisse fazer com o sc query "nome do serviço"
# os.system("cls")

delfito  = [10, 60, 20]
tam = len(delfito)
print(f"A lista do delfito ", delfito, "Tem tamanho de: ", tam)

soma = sum(delfito)
print(f"A soma da lista do delfito", delfito, "é:", tam)

timerzinho = (5)
print(f"O tempo de espere para a tela apagar é: ", timerzinho, "segundos")
espera = time.sleep(5)
os.system("cls")
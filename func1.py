"""
def encontra_maior(A,B):  #definindo o que deve ser realizado
    if A > B:
        return A
    else:
        return B
    
 
res = encontra_maior(10, 20) #dando valor para a DEF e alocando em uma variavel 
print(f"O valor maior é: {res}") #printando o valor da variavel RES

"""


def encontra_maior(A,B): #mesmo esquema do de cima 
    if A > B:
        return A
    else:
        return B

check1 = input(f"Digite um numero: ") #pedindo ao usuario estar informando o 1° valor 
check2 = input(f"Digite o segundo numero: ") #pedidno ao user estar informando o 2° valor 

res = encontra_maior(check1, check2) #passando os valores que a def precisa usar, no caso usar as variaveis que o usuario informou CHECK1 e CHECK2 
print(f"O valor maior é: {res}")

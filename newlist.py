"""

v = [] #lista
s = 0 #variavel que vai ser usada para fazer a média

for i in range(5): #pode ter ate 5 dados salvos
    dado = int(input("Digite um numero inteiro: "))
    v.append(dado)
    s += dado #recebe o dado que o usuario deu + S 
media = s / 5
for elem in v:
    print(elem, end=" ")
print(f"Media dos elementos: {media}")

"""

alista = [] #seta o nome da lista com o nome de alista

while True: #faz um while validando tudo que for verdadeiro 
    dado = int(input("Digite um numero inteiro (0 para sair): ")) #armazena o dado que o usuario digitar 
    if dado == 0: #se o dado digitado pelo usuario for igual a zero ele da o break 
        break
    alista.append(dado)#pendurando a variavel dado na lista 
if alista: #if valendo o toba e mostrando os resultados, os valores/maior e menor numero 
    print(f"Numeros digitados: {alista}")
    print(f"Quantidade de numeros digitados:{len(alista)}")
    print(f"Menor numero: {min(alista)}")
    print(f"Maior numero: {max(alista)}")
else:
    print(f"Nenhum numero foi digitado.") #aqui so acontece quando o mano digita 0 
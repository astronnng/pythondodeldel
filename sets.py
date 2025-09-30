conj1 = {1, 2, 3, 4} #conjunto é com colchete 
conj2 = {3, 4, 5, 6} #conjunto é com colchete 

print(f"Primeiro conjunto: {conj1}") #imprimindo o primeiro colchete 
print(f"Segundo conjunto: {conj2}") #imprimindo o segundo colchete 

uniao = conj1.union(conj2) #unindo o conjunto 1 com o conjunto 2 usando o .union 
intersec = conj1.intersection(conj2) #realizando a intersecção do conjunto 1 com o conjunto 2 
diferenca = conj1.difference(conj2) #realizando a diferença do conjunto 1 com o conjunto 2 
print(f"Uniao do conjunto 1 com o 2: {uniao}") #imprimindo a uniao deles 
print(f"O resultado da intersecção é: {intersec}") #imprimindo  a intersecção 
print(f"Resultado da diferença é: {diferenca}") #imprimindo a diferença 
tupla = (0, 1, 3, 3, 5, 7, 7, 7) #tuplas a sequencia importa

print("Conteudo da tupla: ", tupla)

qtde_elems = len(tupla) #lendo a quantidade de elementos dentro da tupla 
print(f"Quantidade de elementos na tupla: ", qtde_elems)

qtde_setes = tupla.count(7) #count conta a quantidade de numeros 7 dentro da tupla 
print(f"Quantidades de 7 dentro da tupla: {qtde_setes}")

elem_pos4 = tupla[4] #busca o 4 elemento na tupla sendo 0 o primeiro e n-1 ultimo 
print(f"Elemento na 4° posição da tupla: {elem_pos4}")
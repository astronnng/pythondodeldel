variavel_numerica = 5 #variavel com valor e slot atribuido, sendo variavel imutavel pórem o id se torna mutavel quando alocado na memoria ID: 140730275492904

print(f"Variavel númerica(antes da alteração): ")
print(f"Conteudo:{variavel_numerica}")
print(f"ID:", id(variavel_numerica))

variavel_numerica = 10 

print(f"Variavel númerica (depois da atualização):")
print(f"Conteudo: {variavel_numerica}")
print(f"ID:", id(variavel_numerica))

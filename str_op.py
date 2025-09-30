nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")

comp_nome = len(nome) #usado para ler o comprimento do nome 
comp_sobrenome = len(sobrenome) #usado para ler o comprimento do sobrenome 

nome_completo = nome + " " + sobrenome #usado o operador de soma para atribuir um espaço ao dado que a variavel pegou 

comp_nome_completo = len(nome_completo) #len para ler e contar o numero de operadores dentro dos dados que foi digitado

#print(f"Olá!", nome, sobrenome, end=" ")
print(f"Olá! {nome_completo}, tudo bem? Vou te fornecer os dados na qual me digitou!")
print(f"Comprimento do nome: {comp_nome}")
print(f"Comprimento do sobrenome: {comp_sobrenome}")
print(f"Comprimento do nome completo: {comp_nome_completo}")

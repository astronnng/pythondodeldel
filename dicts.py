
pessoa = { #Dicionario aqui eu posso estar dando valores a strings 
    "nome": "Teste",
    "peso": 0.0,
    "idade": 0
}
print(f"Dados da pessoa:")
print(f"Nome", pessoa["nome"]) #usando o print para imprimir o dado de NOME na qual foi inserido no dicionario
print(f"Nome", pessoa["peso"]) #usando o print para imprimir o dado de PESO na qual foi inserido no dicionario
print(f"Nome", pessoa["idade"]) #usando o print para imprimir o dado de IDADE na qual foi inserido no dicionario
print()

pessoa["nome"] = "Texto" #setando outros valores para os campos NOME, PESO e IDADE
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print(f"Dados da pessoa:")
print(f"Nome", pessoa["nome"])
print(f"Nome", pessoa["peso"])
print(f"Nome", pessoa["idade"])



pessoa["nome"] = input("Digite o seu nome: ") #Pedindo ao usuario estar inseridos os valores nos campos NOME, PESO e IDADE
pessoa["peso"] = input("Digite o seu peso: ")
pessoa["idade"] = input("Digite a sua idade: ")

print(f"Seu nome é: {pessoa["nome"]}")
print(f"Seu peso é: {pessoa['peso']} KG")
print(f"Sua idade é: {pessoa['idade']}")
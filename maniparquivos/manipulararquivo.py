nome_arquivo = input(f"Digite o nome do arquivo para armazenar:")

with open(nome_arquivo, "w") as arquivo:
    while True:
        palavra = input(f"Digite uma palavra (ou /exit para encerrar): ")
        if palavra == "/exit":
            break
        arquivo.write(f"{palavra}\n")
print(f"Palavras armazenadas com sucesso... \n")

with open(nome_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
    print(f"Conteudo do arquivo:")
    print(conteudo)
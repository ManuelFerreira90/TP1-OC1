def lerArquivo(arquivo):

    try:
        with open("Projeto/Arquivos_teste/"+arquivo) as a:
            conteudo = a.read()
            print(conteudo)
    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)
        

arquivo = input("Digite o nome do arquivo teste: ")
lerArquivo(arquivo)
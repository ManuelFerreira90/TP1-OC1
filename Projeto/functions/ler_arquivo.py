def lerArquivo(arquivo):

    try:
        with open("Projeto/Arquivos_teste/"+arquivo) as arq:
            texto = arq.readlines()
            print("\nConteudo:")
            #variavel para armzenar cada linha do comando em assembly
            x = ''
            for linha in texto :
                print(linha)
                x = linha.split(" ")
                #x = x.strip()
                print(x)
            arq.close()

    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)
import functions.montador as mont

def lerArquivo(arquivo):

    try:
        with open("Projeto/Arquivos_teste/"+arquivo) as arq:
            texto = arq.readlines()
            print("\nConteudo:")
            #variavel para armzenar cada linha do comando em assembly
            x = ''
            for linha in texto :
                print(linha)
                #removendo vírgulas
                linha = linha.replace(",","")
                #removendo "\n"
                linha = linha.replace("\n","")
                #armazendo cada comando em uma posição do vetor
                #x = linha.split(" ")
                #identificando cada instrução
                #removendo parenteses
                linha = linha.replace("("," ")
                linha = linha.replace(")"," ")
                linha = linha.split(" ")
                mont.indentificar_funcao(linha)
            arq.close()

    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)

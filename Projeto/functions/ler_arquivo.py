import functions.montador as mont

def lerArquivo(arquivo):
    
    try:
        # with open("Projeto/Arquivos_teste/"+arquivo) as arq1:
        #     texto_parat = arq1.read()
        #     arq1.close()
        with open("Projeto/Arquivos_teste/"+arquivo) as arq:
            texto = arq.readlines()
            print("\nConteudo:")
            #variavel para armzenar cada linha do comando em assembly
            x = ''
            y = 0
            for linha in texto :
                linha = linha.replace("\n","") #removendo "\n"
                print(linha)
                linha = linha.replace(",","") #removendo vírgulas
                #armazendo cada comando em uma posição do vetor
                #x = linha.split(" ")
                #identificando cada instrução
                #removendo parenteses
                linha = linha.replace("("," ")
                linha = linha.replace(")"," ")
                linha = linha.split(" ")
                _linha = list(filter(lambda letra: letra != '', linha)) #Removendo ''
                num = 1
                mont.indentificar_funcao(_linha, num, arquivo, arq)
                y += 1
            arq.close()

    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)

def tratarConteudo(instrucao):
    #removendo vírgulas
    x = ''
    instrucao = instrucao.replace(",","")
    #removendo "\n"
    instrucao = instrucao.replace("\n","")
    #armazendo cada comando em uma posição do vetor
    #x = instrucao.split(" ")
    #identificando cada instrução
    #removendo parenteses
    instrucao = instrucao.replace("("," ")
    instrucao = instrucao.replace(")"," ")
    instrucao = instrucao.split(" ")
    num = 2
    mont.indentificar_funcao(instrucao, num, x)
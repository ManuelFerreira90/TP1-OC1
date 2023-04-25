import functions.montador as mont

def lerArquivo(arquivo):
    
    try:
        with open("Projeto/Arquivos_teste/"+arquivo) as arq:
            texto = arq.readlines()
            print("\nConteudo:")
            #variavel para armzenar cada linha do comando em assembly
            x = ''
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
                num = 1
                mont.indentificar_funcao(linha, num, arquivo)
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

def mostrar_conteudo():
    try:
        print("")
        with open("Projeto/Arquivos_saida/output_entrada_01_bin_oct_hex.txt") as arq1:
            mostrar = arq1.read()
            print(mostrar)  
        arq1.close()
    except FileNotFoundError:
        msg = "Infelizmente, ocorreu um erro no arquivo de saida!"
        print(msg)
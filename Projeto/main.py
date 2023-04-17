#xor beq
import os  
import functions.ler_arquivo as func
import functions.montador as mont

num = 0
while(num != 9):
    print("\n1 = Ler arquivo;\n"
        "2 = Inserir instrucoes;\n"
        "9 = Encerrar.\n")
    num = int(input("Digite uma opcao: "))

    #Limpar tela do terminal
    os.system('clear')
    if num == 1:
        pasta = "Projeto/Arquivos_teste/"
        files = os.listdir(pasta) 
        print("Arquivos de teste: \n", files)
        num = int(input("\nDigite qual arquivo teste deseja: "))       
        arquivo = files[num]
        func.lerArquivo(arquivo)

    elif num == 2:
        instrucao = input("Digite sua instrucao assembly: ")
        func.tratarConteudo(instrucao)
    elif num == 9:
        print("Encerrando...")
    else:
        print("ERRO: opcao invalida!")

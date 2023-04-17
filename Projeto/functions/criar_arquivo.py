def criarArquivo(instrucao, num, nome):
    nomeArq = str(nome).replace(".asm", "")
    if num == 1: #Para leitura de arquivo 
        with open("Projeto/Arquivos_saida/output_" + nomeArq + ".txt", "a") as arq:
            arq.write("\n" + instrucao)
            arq.close()
    elif num == 2: #Para incersao individual, pelo teclado
        with open("Projeto/Arquivos_saida/output.txt", "a") as arq:
            arq.write("\n" + instrucao)
            arq.close()
def criarArquivo_bin(instrucao, num, nome):
    nomeArq = str(nome).replace(".asm", "")
    if num == 1: #Para leitura de arquivo 
        with open("Arquivos_saida/Binario/output_" + nomeArq + ".txt", "a") as arq:
            arq.write("0b"+instrucao + "\n")
            arq.close()
    elif num == 2: #Para incersao individual, pelo teclado
        with open("Arquivos_saida/Binario/output.txt", "a") as arq:
            arq.write("0b"+instrucao + "\n")
            arq.close()

    with open("Arquivos_saida/output_" + nomeArq +".txt", "a") as arq:
            octal = oct(int(instrucao, 2))[2:]
            hex_ = hex(int(instrucao, 2))[2:]

            arq.write("0b" + instrucao + " - " + "0c" + octal + " - " + "0x" + hex_ + "\n")
            arq.close()
    
def criarArquivo_hex(instrucao, num, nome):
    nomeArq = str(nome).replace(".asm", "")
    if num == 1: #Para leitura de arquivo 
        with open("Arquivos_saida/Hexadecimal/output_" + nomeArq + ".txt", "a") as arq:
            arq.write("0x" + instrucao + "\n")
            arq.close()
    elif num == 2: #Para incersao individual, pelo teclado
        with open("Arquivos_saida/Hexadecimal/output.txt", "a") as arq:
            arq.write("0x"+instrucao + "\n")
            arq.close()

def criarArquivo_octal(instrucao, num, nome):
    nomeArq = str(nome).replace(".asm", "")
    if num == 1: #Para leitura de arquivo 
        with open("Arquivos_saida/Octal/output_" + nomeArq + ".txt", "a") as arq:
            arq.write("0c"+instrucao + "\n")
            arq.close()
    elif num == 2: #Para incersao individual, pelo teclado
        with open("Arquivos_saida/Octal/output.txt", "a") as arq:
            arq.write("0c"+instrucao + "\n")
            arq.close()
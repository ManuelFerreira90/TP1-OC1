#xor beq
import os  
import functions.ler_arquivo as func
import functions.montador as mont

pasta = "Projeto/Arquivos_teste/"
files = os.listdir(pasta) 
print("Arquivos de teste: \n", files)

num = int(input("\nDigite qual arquivo teste deseja: "))       
arquivo = files[num]
func.lerArquivo(arquivo)


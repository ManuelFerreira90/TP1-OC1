import os

def lerArquivo(arquivo):

    try:
        with open("Projeto/Arquivos_teste/"+arquivo) as arq:
            conteudo = arq.read()
            print("\nConteudo:")
            print(conteudo)

    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)
        

pasta = "Projeto/Arquivos_teste/"
files = os.listdir(pasta) 
print("Arquivos de teste: \n", files)

num = int(input("\nDigite qual arquivo teste deseja: "))       
arquivo = files[num]
lerArquivo(arquivo)

#lw sw sub xor addi srl beq



import os

def lerArquivo(arquivo):

    try:
        with open("Projeto/Arquivos_teste/"+arquivo) as arq:
            texto = arq.readlines()
            print("\nConteudo:")
            for linha in texto :
                print(linha)
            arq.close()

    except FileNotFoundError:
        msg = "Infelizmente, o arquivo " + arquivo + " não existe!"
        print(msg)
    
        

pasta = "Projeto/Arquivos_teste/"
files = os.listdir(pasta) 
print("Arquivos de teste: \n", files)

num = int(input("\nDigite qual arquivo teste deseja: "))       
arquivo = files[num]
lerArquivo(arquivo)

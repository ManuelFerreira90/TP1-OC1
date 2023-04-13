def lw(linha):
    opcode, rd, func3, rs1, immediate, resultado = ''
    opcode = '0000011' 
    func3 = '010'
    x = list.linha()
    print(x)
    #for i in range(linha[3]):
        #immediate = 
    return 

def sw(linha):
    return

def sub(linha):
    return 

def xor(linha): 
    return 

def addi(linha):
     return 

def srl(linha): 
    return 

def beq(linha):
    return

def indentificar_funcao(x):
    if x[0] == 'lw':
        lw(x)
    elif x[0] == 'sw':
        sw(x)
    elif x[0] == 'sub':
        sub(x)
    elif x[0] == 'xor':
        xor(x)
    elif x[0] == 'addi':
        addi(x)
    elif x[0] == 'srl':
        srl(x)
    elif x[0] == 'beq':
        beq(x)
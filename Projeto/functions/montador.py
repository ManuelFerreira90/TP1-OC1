def lw(linha):
    rd = linha[1]
    rd = rd.replace("x","")
    rd = int(rd)
    rd = bin(rd)[2:]
    rs1 = linha[3]
    rs1 = rs1.replace("x","")
    rs1 = int(rs1)
    rs1 = bin(rs1)[2:]
    immediate = linha[2]
    immediate = int(immediate)
    immediate = bin(immediate)
    immediate_aux = "000000000000"
    x = 0
    for i in immediate:
        x += 1
    i = 0
    for i in immediate_aux:
        if(i == 12 - x):
            immediate_aux[i] = immediate[x]
            x -=1
    opcode = '0000011' 
    func3 = '010'
    resultado = immediate_aux + rs1 + func3 + rd + opcode  
    print(resultado)
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
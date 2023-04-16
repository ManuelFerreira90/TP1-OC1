def lw(linha):
    rd = linha[1]
    rd = rd.replace("x","")
    rd = int(rd)
    rd = bin(rd)[2:]
    rd = list(rd)
    rd_aux = "00000"
    rd_aux = list(rd_aux)
    rs1 = linha[3]
    rs1 = rs1.replace("x","")
    rs1 = int(rs1)
    rs1 = bin(rs1)[2:]
    rs1 = list(rs1)
    rs1_aux = "00000"
    rs1_aux = list(rs1_aux)
    immediate = linha[2]
    immediate = int(immediate)
    immediate = bin(immediate)[2:]
    immediate = list(immediate)
    immediate_aux = "000000000000"
    opcode = '0000011' 
    func3 = '010'
    x = len(immediate) - 1
    y = len(rd) - 1
    z = len(rs1) - 1
    v = 0
    immediate_aux = list(immediate_aux)
    
    for k in range(12): 
        if(k == 11 - x):
            immediate_aux[k] = immediate[v]
            v += 1
            x -= 1
    v = 0    
    for k in range(5):
        if(k == 4 - y):
            rd_aux[k] = rd[v]
            y -=1
            v += 1
    v = 0
    for k in range(5):
        if(k == 4 - z):
            rs1_aux[k] = rs1[v]
            z -=1
            v += 1

    immediate_aux = ''.join(immediate_aux)
    rd_aux = ''.join(rd_aux)
    rs1_aux = ''.join(rs1_aux)
    resultado = ''

    aux = [immediate_aux] + [rs1_aux] + [func3] + [rd_aux] + [opcode]
    for i in aux:
        resultado += i  
    print(resultado)
    return 

def sw(linha):
    opcode = '0100011'
    funct3 = '010'
    rs2 = linha[1]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits
    rs1 = linha[3]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    immediate = int(linha[2])
    if (immediate <= 31):
        immediate_4 = bin(immediate)[2:]
        immediate_11 = '0000000'
    else:
        immediate_11 = ''
        immediate_4 = ''
        immediate = format(int(bin(immediate), 2), '012b') # immediate com um total de 12 bits
        for i in range(12):
            if(i < 7):
                immediate_11 += immediate[i]
            else:
                immediate_4 += immediate[i]
    instrucao = immediate_11 + str(rs2) + str(rs1) + funct3 + immediate_4 + opcode
    print(instrucao)
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
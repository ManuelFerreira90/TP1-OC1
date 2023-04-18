import functions.criar_arquivo as criar

def converter_oc_e_hex(var, tipo):
    if tipo == 0:
        var = var[2:]
        f = bin(int(var, 16))[2:]
        return f
    else:
        var = var[2:]
        f = bin(int(var, 8))[2:]
        return f

def lw(linha, num, nome_arq):
    c = 1
    h = 0
    rd = linha[1]
    rs1 = linha[3]
    immediate = linha[2]
    rd = str(rd)
    rs1 = str(rs1)

    if rd[0] == '0' and rd[1] == 'x':
        rd = converter_oc_e_hex(rd,h)
    elif rd[0] == '0' and rd[1] == 'c':
        rd = converter_oc_e_hex(rd,c)
    else:
        rd = rd.replace("x","")
        rd = int(rd)
        rd = bin(rd)[2:]
        
    if rs1[0] == '0' and rs1[1] == 'x':
        rs1 = converter_oc_e_hex(rs1,h)
    elif rs1[0] == '0' and rs1[1] == 'c':
        rs1 = converter_oc_e_hex(rs1,c)
    else:
        rs1 = rs1.replace("x","")
        rs1 = int(rs1)
        rs1 = bin(rs1)[2:]
    
    immediate = bin(int(immediate))[2:]
    
    rd_aux = ['0','0','0','0','0']
    rs1_aux = ['0','0','0','0','0']
    immediate_aux = ['0','0','0','0','0','0','0','0','0','0','0','0']
    opcode = '0000011'
    func3 = '010'
    
    x = len(immediate) - 1
    y = len(rd) - 1
    z = len(rs1) - 1
    v = 0
    
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

    resultado = [immediate_aux] + [rs1_aux] + [func3] + [rd_aux] + [opcode]
    
    print(resultado)
    criar.criarArquivo(resultado, num, nome_arq)
    return 

def sw(linha, num, nome_arq):
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
        immediate_4 = format(int(immediate_4, 2), '05b')
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
    criar.criarArquivo(instrucao, num, nome_arq)
    print(instrucao)
    return

def sub(linha, num, nome_arq):
    c = 1
    h = 0
    opcode = '0110011'
    funct3 = '000'
    funct7 = '0100000'
    rd = linha[1]
    rs1 = linha[2]
    rs2 = linha[3]
    rd = str(rd)
    rs1 = str(rs1)
    rs2 = str(rs2)
    
    if rd[0] == '0' and rd[1] == 'x':
        rd = converter_oc_e_hex(rd,h)
    elif rd[0] == '0' and rd[1] == 'c':
        rd = converter_oc_e_hex(rd,c)
    else:
        rd = rd.replace("x","")
        rd = int(rd)
        rd = bin(rd)[2:]
        
    if rs1[0] == '0' and rs1[1] == 'x':
        rs1 = converter_oc_e_hex(rs1,h)
    elif rs1[0] == '0' and rs1[1] == 'c':
        rs1 = converter_oc_e_hex(rs1,c)
    else:
        rs1 = rs1.replace("x","")
        rs1 = int(rs1)
        rs1 = bin(rs1)[2:]
    
    if rs2[0] == '0' and rs2[1] == 'x':
        rs2 = converter_oc_e_hex(rs2,h)
    elif rs2[0] == '0' and rs2[1] == 'c':
        rs2 = converter_oc_e_hex(rs2,c)
    else:
        rs2 = rs2.replace("x","")
        rs2 = int(rs2)
        rs2 = bin(rs2)[2:] 
    
    rd = str(rd)
    rs1 = str(rs1)
    rs2 = str(rs2)
    x = len(rs2) - 1
    y = len(rd) - 1
    z = len(rs1) - 1
    v = 0
    
    rd_aux = ['0','0','0','0','0']
    rs1_aux = ['0','0','0','0','0']
    rs2_aux = ['0','0','0','0','0']
    resultado = ''
    
    for k in range(5): 
        if(k == 4 - x):
            rs2_aux[k] = rs2[v]
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
    
    rs2_aux = ''.join(rs2_aux)
    rd_aux = ''.join(rd_aux)
    rs1_aux = ''.join(rs1_aux)
    resultado = [funct7] + [rs2_aux] + [rs1_aux] + [funct3] + [rd_aux] + [opcode]
    
    print(resultado)
    criar.criarArquivo(resultado, num, nome_arq)
    return 

def xor(linha, num, nome_arq): 

    #criar.criarArquivo(resultado, num, nome_arq)
    return 

def addi(linha, num, nome_arq):
    c = 1
    h = 0
    opcode = '0010011' 
    func3 = '000'
    rd = linha[1]
    rs1 = linha[2]
    immediate = linha[3]
    rd = str(rd)
    rs1 = str(rs1)
    immediate = str(immediate)
    complemento_II = False
    
    if rd[0] == '0' and rd[1] == 'x':
        rd = converter_oc_e_hex(rd,h)
    elif rd[0] == '0' and rd[1] == 'c':
        rd = converter_oc_e_hex(rd,c)
    else:
        rd = rd.replace("x","")
        rd = int(rd)
        rd = bin(rd)[2:]
        
    if rs1[0] == '0' and rs1[1] == 'x':
        rs1 = converter_oc_e_hex(rs1,h)
    elif rs1[0] == '0' and rs1[1] == 'c':
        rs1 = converter_oc_e_hex(rs1,c)
    else:
        rs1 = rs1.replace("x","")
        rs1 = int(rs1)
        rs1 = bin(rs1)[2:]
    
    if immediate[0] == '0' and immediate[1] == 'x':
        immediate = converter_oc_e_hex(immediate,h)
    elif immediate[0] == '0' and immediate[1] == 'c':
        immediate = converter_oc_e_hex(immediate,c)
    elif immediate[0] == 'x':
        immediate = immediate.replace("x","")
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
    elif immediate[0] =='-':
        complemento_II = True
        immediate = int(immediate)
        immediate = immediate * -1
        immediate = list(bin(immediate)[2:])
        for k in range(len(immediate)):
            if(immediate[k] == "0"):
                immediate[k] = "1"
            else:
                immediate[k] = "0"
        aux = len(immediate)
        immediate = int(''.join(immediate),2) + 1 
        immediate = bin(immediate)[2:]
        immediate = immediate.zfill(aux)

    immediate_aux = ['0','0','0','0','0','0','0','0','0','0','0','0']
    rd_aux = ['0','0','0','0','0']
    rs1_aux = ['0','0','0','0','0']
    rs2_aux = ['0','0','0','0','0']
    
    x = len(immediate) - 1
    y = len(rd) - 1
    z = len(rs1) - 1
    v = 0

    for k in range(12): 
        if(k == 11 - x):
            immediate_aux[k] = immediate[v]
            v += 1
            x -= 1
        elif(complemento_II == True):
            immediate_aux[k] = '1'
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
    
    resultado = [immediate_aux] + [rs1_aux] + [func3] + [rd_aux] + [opcode]
     
    print(resultado)
    criar.criarArquivo(resultado, num, nome_arq)
    return 

def srl(linha, num, nome_arq): 
    c = 1
    h = 0
    opcode = '0110011'
    funct3 = '101'
    funct7 = '0000000'
    rd = linha[1]
    rs1 = linha[2]
    rs2 = linha[3]
    rd = str(rd)
    rs1 = str(rs1)
    rs2 = str(rs2)
    
    if rd[0] == '0' and rd[1] == 'x':
        rd = converter_oc_e_hex(rd,h)
    elif rd[0] == '0' and rd[1] == 'c':
        rd = converter_oc_e_hex(rd,c)
    else:
        rd = rd.replace("x","")
        rd = int(rd)
        rd = bin(rd)[2:]
        
    if rs1[0] == '0' and rs1[1] == 'x':
        rs1 = converter_oc_e_hex(rs1,h)
    elif rs1[0] == '0' and rs1[1] == 'c':
        rs1 = converter_oc_e_hex(rs1,c)
    else:
        rs1 = rs1.replace("x","")
        rs1 = int(rs1)
        rs1 = bin(rs1)[2:]
    
    if rs2[0] == '0' and rs2[1] == 'x':
        rs2 = converter_oc_e_hex(rs2,h)
    elif rs2[0] == '0' and rs2[1] == 'c':
        rs2 = converter_oc_e_hex(rs2,c)
    else:
        rs2 = rs2.replace("x","")
        rs2 = int(rs2)
        rs2 = bin(rs2)[2:]       
    
    rd = str(rd)
    rs1 = str(rs1)
    rs2 = str(rs2)
    x = len(rs2) - 1
    y = len(rd) - 1
    z = len(rs1) - 1
    v = 0
    
    rd_aux = ['0','0','0','0','0']
    rs1_aux = ['0','0','0','0','0']
    rs2_aux = ['0','0','0','0','0']
    resultado = ''
    
    for k in range(5): 
        if(k == 4 - x):
            rs2_aux[k] = rs2[v]
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
    
    rs2_aux = ''.join(rs2_aux)
    rd_aux = ''.join(rd_aux)
    rs1_aux = ''.join(rs1_aux)
    resultado = [funct7] + [rs2_aux] + [rs1_aux] + [funct3] + [rd_aux] + [opcode]
    
    print(resultado)
    criar.criarArquivo(resultado, num, nome_arq)
    return 

def beq(linha, num, nome_arq):
    #beq rs1, rs2, L1
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode
    opcode = '1100011'
    funct3 = '000'
    rs1 = linha[1]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    rs2 = linha[2]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits

    immediate = int(linha[2])
    if (immediate <= 31):
        immediate_4 = bin(immediate)[2:]
        immediate_4 = format(int(immediate_4, 2), '05b')
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
   # criar.criarArquivo(instrucao, num, nome_arq)
    print(instrucao)
    return

def indentificar_funcao(x, num, arq):
    if x[0] == 'lw':
        lw(x, num, arq)
    elif x[0] == 'sw':
        sw(x, num, arq)
    elif x[0] == 'sub':
        sub(x, num, arq)
    elif x[0] == 'xor':
        xor(x, num, arq)
    elif x[0] == 'addi':
        addi(x, num, arq)
    elif x[0] == 'srl':
        srl(x, num, arq)
    elif x[0] == 'beq':
        beq(x, num, arq)
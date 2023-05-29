import functions.criar_arquivo as criar

def converter_oc_e_hex(var, tipo):
    if tipo == 0:
        f = bin(int(var[2:], 16))[2:]
        return f
    elif tipo == 1:
        f = bin(int(var[2:], 8))[2:]
        return f
    elif tipo == 2: #Convertendo a instrucao de 32 bits de bin para hex
        f = hex(int(var, 2))[2:]
        return f
    elif tipo == 3: #Convertendo a instrucao de 32 bits de bin para octal
        f = oct(int(var, 2))[2:]
        return f
    elif tipo == 4:
        f = var[2:]
        return f

def verificar_immediate(immediate, x, h, c, b):
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'b':
            verificar = converter_oc_e_hex(immediate,b)
            verificar = int(verificar,2)
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 2047 or verificar < -2048:
        return 0
    else:
        return 1

def converter_immediate(immediate, x, h, c, b):
    if(x > 1):
        if immediate[0] == '-':
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
            #print(immediate)
            immediate = "{:1>{}}".format(immediate, 12)
            return immediate
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
            immediate = format(int(immediate, 2), '012b')
            return immediate
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c)
            immediate = format(int(immediate, 2), '012b')
            return immediate
        elif immediate[0] == '0' and immediate[1] == 'b':
            immediate = converter_oc_e_hex(immediate,b)
            immediate = format(int(immediate, 2), '012b')
            return immediate
        else:
            immediate = int(immediate)
            immediate = bin(immediate)[2:]
            immediate = format(int(immediate, 2), '012b')
            return immediate   
    else:
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        immediate = format(int(immediate, 2), '012b')
        return immediate

#100% funcional
def lw(linha, num, nome_arq):
    c = 1
    h = 0
    b = 4
    rd = linha[1]
    rs1 = linha[3]
    immediate = linha[2]
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs1 = str(rs1)
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    
    #converter immediate
    immediate = converter_immediate(immediate, x, h, c, b)
    
    opcode = '0000011'
    func3 = '010'

    resultado = ''

    resultado = immediate + rs1 + func3 + rd + opcode

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#100% funcional
def sw(linha, num, nome_arq):
    c = 1
    h = 0
    b = 4
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
    immediate = linha[2]
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)#verificando se o immediate cabe em 12 bits
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    #converter immediate
    immediate = converter_immediate(immediate, x, h, c, b) 
    immediate1 = immediate[0:7]
    immediate2 = immediate[7:12]
    resultado = immediate1 + str(rs2) + str(rs1) + funct3 + immediate2 + opcode
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def sub(linha, num, nome_arq):
    opcode = '0110011'
    funct3 = '000'
    funct7 = '0100000'
    
    rd = linha[1]
    rs1 = linha[2]
    rs2 = linha[3]
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs1 = str(rs1)
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')
    
    rs2 = str(rs2)
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b')
     
    
    resultado = funct7 + rs2 + rs1 + funct3 + rd + opcode
        
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#100% funcional
def xor(linha, num, nome_arq): 
    #xor x9,x10,x12
    opcode = '0110011'
    funct3 = '100'
    funct7 = '0000000'
    rd = linha[1]
    rd = str(rd).replace("x","")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    rs1 = linha[2]
    rs1 = str(rs1).replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')
    rs2 = linha[3]
    rs2 = str(rs2).replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b')
    resultado = funct7 + str(rs2) + str(rs1) + funct3 + rd + opcode
        
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#100% funcional
def addi(linha, num, nome_arq):
    c = 1
    h = 0
    b = 4
    opcode = '0010011' 
    func3 = '000'
    rd = linha[1]
    rs1 = linha[2]
    immediate = linha[3]
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs1 = str(rs1)
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')
    
    complemento_II = False
    
    x = len(immediate)
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    
    #converter immediate
    immediate = converter_immediate(immediate, x, h, c, b)

    rd = str(rd)
    rs1 = str(rs1)
    
    resultado = ''
    
    resultado = immediate + rs1 + func3 + rd + opcode

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#100% funcional
def srl(linha, num, nome_arq): 
    opcode = '0110011'
    funct3 = '101'
    funct7 = '0000000'
    rd = linha[1]
    rs1 = linha[2]
    rs2 = linha[3]
 
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs1 = str(rs1)
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')

    rs2 = str(rs2)
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b')
    
    resultado = funct7 + rs2 + rs1 + funct3 + rd + opcode

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#100% funcional
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

    immediate = linha[3]
    immediate = int(immediate) / 2
    immediate = str(int(immediate))
    complemento_II = False
    
    x = len(immediate)
    c = 1
    h = 0
    b = 4
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    immediate = converter_immediate(immediate, x, h, c, b)
    
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return

    imm10_5 = immediate[2:8]
    imm4_1 = immediate[8:12]
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def jalr(linha, num, nome_arq):
    c = 1
    h = 0
    b = 4
    complemento_II = False
    opcode = '1100111'
    funct3 = '000'
    rd = linha[1]
    rs1 = linha[2]
    immediate = linha[3]
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs1 = str(rs1)
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')
    
    complemento_II = False
    
    x = len(immediate)
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    
    #converter immediate
    immediate = converter_immediate(immediate, x, h, c, b)
    
    resultado = ''
    
    resultado = immediate + rs1 + funct3 + rd + opcode
        
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def mv(linha, num, nome_arq):
    c = 1
    h = 0
    opcode = '0010011' 
    func3 = '000'
    rd = linha[1]
    rs1 = linha[2]
    immediate = '000000000000'
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs1 = str(rs1)
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')

    rd = str(rd)
    rs1 = str(rs1)
    
    resultado = ''
    
    resultado = immediate + rs1 + func3 + rd + opcode

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def noti(linha, num, nome_arq):
    opcode = '0010011'
    funct3 = '100'
    immediate = '111111111111'
    rd = linha[1]
    rd = str(rd).replace("x","")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    rs1 = linha[2]
    rs1 = str(rs1).replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b')

    resultado = immediate + str(rs1) + funct3 + rd + opcode
        
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return
    
#100% funcional
def li(linha, num, nome_arq):
    c = 1
    h = 0
    b = 4
    opcode = '0010011' 
    func3 = '000'
    rd = linha[1]
    rs1 = '00000'
    immediate = linha[2]
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    complemento_II = False
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    
    #converter immediate
    immediate = converter_immediate(immediate, x, h, c, b)
    
    resultado = ''
    
    resultado = immediate + rs1 + func3 + rd + opcode

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#100% funcional 
def nop(linha, num, nome_arq):
    opcode = '0010011'
    rd = '00000'
    funct3 = '000'
    rs1 = '00000'
    immediate = '000000000000'
    resultado = ''
    
    resultado = immediate + rs1 + funct3 + rd + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def j(linha, num, nome_arq):
    complemento_II = False
    c = 1
    h = 0
    b = 4
    opcode = '1101111'
    rd = '00000'
    immediate = linha[1]
    resultado = ''
    
    #verificando se o immediate cabe em 12 bits
    
    x = len(immediate)
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'b':
            verificar = converter_oc_e_hex(immediate,b)
            verificar = int(verificar,2)
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 1048576 or verificar < -1048577:
        return print("ERRO: immediate maior que 20 bits!")
    
    if(x > 1):
        if immediate[0] == '-':
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
            #print(immediate)
            immediate = "{:1>{}}".format(immediate, 20)
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
            immediate = format(int(immediate, 2), '020b')
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c)
            immediate = format(int(immediate, 2), '020b')
        elif immediate[0] == '0' and immediate[1] == 'b':
            immediate = converter_oc_e_hex(immediate,b)
            immediate = format(int(immediate, 2), '020b')
        else:
            immediate = int(immediate)
            immediate = bin(immediate)[2:]
            immediate = format(int(immediate, 2), '020b')   
    else:
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        immediate = format(int(immediate, 2), '020b')
    
    immediate = bin(int(immediate, 2) >> 1)[2:] 
    if(complemento_II):
        immediate = "{:1>{}}".format(immediate, 20)
    else:
        immediate = "{:0>{}}".format(immediate, 20)
    
    resultado = immediate[0] + immediate[10:20] + immediate[9] + immediate[1:9] + rd + opcode
    #resultado = immediate[0] + immediate[9:20] + immediate[8] + immediate[1:8] + rd + opcode
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def ret(linha, num, nome_arq):
    opcode = '1100111'
    funct3 = '000'
    rd = '00000'
    rs1 = '00001'
    immediate = '000000000000'
    resultado = ''
    
    resultado = immediate + rs1 + funct3 + rd + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def neg(linha, num, nome_arq):
    opcode = '0110011'
    funct3 = '000'
    funct7 = '0100000'
    rs1 = '00000'
    
    rd = linha[1]
    rs2 = linha[2]
    
    rd = str(rd)
    rd = rd.replace("x", "")
    rd = bin(int(rd))[2:]
    rd = format(int(rd, 2), '05b')
    
    rs2 = str(rs2)
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b')
    
    resultado = ''
    
    resultado = funct7 + rs2 + rs1 + funct3 + rd + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def bne(linha, num, nome_arq):
    opcode = '1100011'
    funct3 = '001'
    rs1 = linha[1]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    rs2 = linha[2]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits

    immediate = linha[3]
    immediate = int(immediate) / 2
    immediate = str(int(immediate))
    complemento_II = False
    
    x = len(immediate)
    c = 1
    h = 0
    b = 4
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    immediate = converter_immediate(immediate, x, h, c, b)
    
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return

    imm10_5 = immediate[2:8]
    imm4_1 = immediate[8:12]
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)

#100% funcional
def blt(linha, num, nome_arq):
    opcode = '1100011'
    funct3 = '100'
    rs1 = linha[1]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    rs2 = linha[2]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits

    immediate = linha[3]
    immediate = int(immediate) / 2
    immediate = str(int(immediate))
    complemento_II = False
    
    x = len(immediate)
    c = 1
    h = 0
    b = 4
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    immediate = converter_immediate(immediate, x, h, c, b)
    
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return

    imm10_5 = immediate[2:8]
    imm4_1 = immediate[8:12]
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)

#100% funcional
def bge(linha, num, nome_arq):
    opcode = '1100011'
    funct3 = '101'
    rs1 = linha[1]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    rs2 = linha[2]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits

    immediate = linha[3]
    immediate = int(immediate) / 2
    immediate = str(int(immediate))
    complemento_II = False
    
    x = len(immediate)
    c = 1
    h = 0
    b = 4
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    immediate = converter_immediate(immediate, x, h, c, b)
    
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return

    imm10_5 = immediate[2:8]
    imm4_1 = immediate[8:12]
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)

#100% funcional
def bltu(linha, num, nome_arq):
    opcode = '1100011'
    funct3 = '110'
    rs1 = linha[1]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    rs2 = linha[2]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits

    immediate = linha[3]
    immediate = int(immediate) / 2
    immediate = str(int(immediate))
    complemento_II = False
    
    x = len(immediate)
    c = 1
    h = 0
    b = 4
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    immediate = converter_immediate(immediate, x, h, c, b)
    
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return

    imm10_5 = immediate[2:8]
    imm4_1 = immediate[8:12]
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)

#100% funcional
def bgeu(linha, num, nome_arq):
    opcode = '1100011'
    funct3 = '111'
    rs1 = linha[1]
    rs1 = rs1.replace("x", "")
    rs1 = bin(int(rs1))[2:]
    rs1 = format(int(rs1, 2), '05b') #preenchendo rs1 para 5bits
    rs2 = linha[2]
    rs2 = rs2.replace("x", "")
    rs2 = bin(int(rs2))[2:]
    rs2 = format(int(rs2, 2), '05b') #preenchendo rs2 para 5bits

    immediate = linha[3]
    immediate = int(immediate) / 2
    immediate = str(int(immediate))
    complemento_II = False
    
    x = len(immediate)
    c = 1
    h = 0
    b = 4
    
    #verificando se o immediate cabe em 12 bits
    x = len(immediate)
    verificar = verificar_immediate(immediate, x, h, c, b)
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return
    immediate = converter_immediate(immediate, x, h, c, b)
    
    if(verificar == 0):
        print("ERRO: immediate maior que 12 bits!")
        return

    imm10_5 = immediate[2:8]
    imm4_1 = immediate[8:12]
    #imm[12]  imm[10:5] | rs2 |rs1 | funct3| imm[4:1] imm[11] |opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)

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
    elif x[0] == 'jalr':
        jalr(x, num, arq)
    elif x[0] == 'mv':
        mv(x, num, arq)
    elif x[0] == 'not':
        noti(x, num, arq)   
    elif x[0] == 'li':
        li(x, num, arq)  
    elif x[0] == 'nop':
        nop(x, num, arq)
    elif x[0] == 'j':
        j(x, num, arq)
    elif x[0] == 'ret':
        ret(x, num, arq)
    elif x[0] == 'neg':
        neg(x, num, arq)
    elif x[0] == 'bne':
        bne(x, num, arq)
    elif x[0] == 'blt':
        blt(x, num, arq)
    elif x[0] == 'bge':
        bge(x, num, arq)
    elif x[0] == 'bltu':
        bltu(x, num, arq)
    elif x[0] == 'bgeu':
        bgeu(x, num, arq)
    
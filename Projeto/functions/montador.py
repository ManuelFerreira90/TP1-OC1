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

#100% funcional
def lw(linha, num, nome_arq):
    c = 1
    h = 0
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
    
    x = len(immediate)
    #verificando se o immediate cabe em 12 bits
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2) 
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 2047 or verificar < -2048:
        return print("Erro: Immediate não cabe em 12 bits")
    
    if(x > 1):
        if immediate[0] =='-':
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
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c) 
        else:
            immediate = int(immediate)
            immediate = bin(immediate)[2:]    
    else:
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        
    immediate = format(int(immediate, 2), '012b')
    
    opcode = '0000011'
    func3 = '010'

    resultado = ''

    resultado = immediate + rs1 + func3 + rd + opcode
    print(resultado)

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

def sw(linha, num, nome_arq):
    c = 1
    h = 0
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
    
    #verificando se o immediate cabe em 12 bits
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2) 
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 2047 or verificar < -2048:
        return print("Erro: Immediate não cabe em 12 bits")
    
    if(x > 1):
        if immediate[0] =='-':
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
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c)
        else:
            immediate = immediate.replace("x","")
            immediate = int(immediate)
            immediate = bin(immediate)[2:]     
    else:
        immediate = immediate.replace("x","")
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        
    immediate = format(int(immediate, 2), '012b')
    
    immediate1 = immediate[0:7]
    immediate2 = immediate[7:12]
    
    resultado = immediate1 + str(rs2) + str(rs1) + funct3 + immediate2 + opcode
    print(resultado)

    # resultado_hex = converter_oc_e_hex(resultado, 2)
    # resultado_octal = converter_oc_e_hex(resultado, 3)
    # criar.criarArquivo_bin(resultado, num, nome_arq)
    # criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    # criar.criarArquivo_octal(resultado_octal, num, nome_arq)
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
    print(resultado)
        
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
    print(resultado)
        
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
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2) 
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 2047 or verificar < -2048:
        return print("Erro: Immediate não cabe em 12 bits")
    
    if(x > 1):
        if immediate[0] =='-':
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
            immediate = "{:1>{}}".format(immediate, 12)
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c)  
        else:
            immediate = immediate.replace("x","")
            immediate = int(immediate)
            immediate = bin(immediate)[2:]
            immediate = format(int(immediate, 2), '012b')   
    else:
        immediate = immediate.replace("x","")
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        immediate = format(int(immediate, 2), '012b')

    rd = str(rd)
    rs1 = str(rs1)
    
    resultado = ''
    
    resultado = immediate + rs1 + func3 + rd + opcode
    print(resultado)

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
    print(resultado)

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return 

#falta immediate receber outras bases
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
    complemento_II = False
    x = len(immediate)
    c = 1
    h = 0
    
    if(x > 1):
        if immediate[0] =='-':
            complemento_II = True
            immediate = int(immediate)
            immediate = immediate * -1
            if(immediate > 2048):
                print("ERRO: out of range")
                return
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
            immediate = "{:1>{}}".format(immediate, 12)
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate, h)
            if(int(immediate) < -2048 or int(immediate) > 2047):
                print("ERRO: out of range")
                return
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate, c)
            print(int(immediate, 10))
            if(int(immediate, 10) < -2048 or int(immediate) > 2047):
                print("ERRO: out of range")
                return  
        else:
            immediate = immediate.replace("x","")
            immediate = int(immediate)
            if(immediate > 2047):
                print("ERRO: out of range")
                return
            immediate = bin(immediate)[2:]
            immediate = format(int(immediate, 2), '012b')   
    else:
        immediate = immediate.replace("x","")
        immediate = int(immediate)
        if(immediate > 2047):
            print("ERRO: out of range")
            return
        immediate = bin(immediate)[2:]
        immediate = format(int(immediate, 2), '012b')

    imm10_5 = ''
    imm4_1 = ''
    for i in range(len(immediate)):
        if(i > 0 and i < 7):
            imm10_5 += immediate[i]
        elif(i > 6 and i < 11):
            imm4_1 += immediate[i]

    # resultado = immediate[0] + " - " + imm10_5 + " - " + str(rs2) + " - " + str(rs1) + " - " + funct3 + " - " + imm4_1 + " - " + immediate[1] + " - " + opcode

    resultado = immediate[0] + imm10_5 + str(rs2) + str(rs1) + funct3 + imm4_1 + immediate[1] + opcode
    print(resultado)

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
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2) 
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 2047 or verificar < -2048:
        return print("Erro: Immediate não cabe em 12 bits")
    
    if(x > 1):
        if immediate[0] =='-':
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
            immediate = "{:1>{}}".format(immediate, 12)
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c)  
        else:
            immediate = immediate.replace("x","")
            immediate = int(immediate)
            immediate = bin(immediate)[2:]
            immediate = format(int(immediate, 2), '012b')   
    else:
        immediate = immediate.replace("x","")
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        immediate = format(int(immediate, 2), '012b')

    rd = str(rd)
    rs1 = str(rs1)
    
    resultado = ''
    
    resultado = immediate + rs1 + funct3 + rd + opcode
    print(resultado)
        
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
    print(resultado)

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    
    
    
    #compressed function 16bits
    # opcode = '10'
    # funct4 = '100'
    # rs1 = '0'
    
    # rd = linha[1]
    # rs2 = linha[2]
    
    # rd = rd.replace("x","")
    # rs2 = rs2.replace("x","")
    # rd = int(rd)
    # rd = bin(rd)[2:]
    # rs2 = int(rs2)
    # rs2 = bin(rs2)[2:]
    
    # rd = str(rd)
    # rs2 = str(rs2)
   
    # rd_aux = ['0','0','0','0','0']
    # rs2_aux = ['0','0','0','0','0']
    
    # y = len(rd) - 1
    # z = len(rs2) - 1
    # v = 0
  
    # for k in range(5):
    #     if(k == 4 - y):
    #         rd_aux[k] = rd[v]
    #         y -=1
    #         v += 1
    # v = 0
    # for k in range(5):
    #     if(k == 4 - z):
    #         rs2_aux[k] = rs2[v]
    #         z -=1
    #         v += 1

    # rd_aux = ''.join(rd_aux)
    # rs2_aux = ''.join(rs2_aux)
    # resultado = ''
    
    # resultado = [funct4] + [rs1] + [rd_aux] + [rs2_aux] + [opcode]
    # print(resultado)
        
    # resultado_hex = converter_oc_e_hex(resultado, 2)
    # resultado_octal = converter_oc_e_hex(resultado, 3)
    # criar.criarArquivo_bin(resultado, num, nome_arq)
    # criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    # criar.criarArquivo_octal(resultado_octal, num, nome_arq)
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
    print(resultado)
        
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    
    #compressed function 16bits
    #jr
    # opcode = '10'
    # funct3 = '100'
    # immediate = '00000'
    # rd = '0'
    # rs1 = linha[3]
    # rs1 = str(rs1)
    # rs1 = rs1.replace("x","")
    # rs1 = int(rs1)
    # rs1 = bin(rs1)[2:]
    
    # rs1_aux = ['0','0','0','0','0']
    
    # z = len(rs1) - 1
    # v = 0
    
    # for k in range(5):
    #     if(k == 4 - z):
    #         rs1_aux[k] = rs1[v]
    #         z -=1
    #         v += 1

    # rs1_aux = ''.join(rs1_aux)
    # resultado = ''

    # resultado = [funct3] + [rd] + [rs1_aux] + [immediate] + [opcode]
    # print(resultado)
        
    # resultado_hex = converter_oc_e_hex(resultado, 2)
    # resultado_octal = converter_oc_e_hex(resultado, 3)
    # criar.criarArquivo_bin(resultado, num, nome_arq)
    # criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    # criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return
    
#100% funcional
def li(linha, num, nome_arq):
    c = 1
    h = 0
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
    
    x = len(immediate)
    #verificando se o immediate cabe em 12 bits
    if(x > 1):
        if immediate[0] == '0' and immediate[1] == 'x':
            verificar = converter_oc_e_hex(immediate,h)
            verificar = int(verificar,2)
        elif immediate[0] == '0' and immediate[1] == 'c':
            verificar = converter_oc_e_hex(immediate,c)
            verificar = int(verificar,2) 
        else:
            verificar = int(immediate)
    else:
            verificar = int(immediate)
    if verificar > 2047 or verificar < -2048:
        return print("Erro: Immediate não cabe em 12 bits")
    
    if(x > 1):
        if immediate[0] =='-':
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
            immediate = "{:1>{}}".format(immediate, 12)
        elif immediate[0] == '0' and immediate[1] == 'x':
            immediate = converter_oc_e_hex(immediate,h)
        elif immediate[0] == '0' and immediate[1] == 'c':
            immediate = converter_oc_e_hex(immediate,c)  
        else:
            immediate = immediate.replace("x","")
            immediate = int(immediate)
            immediate = bin(immediate)[2:]
            immediate = format(int(immediate, 2), '012b')   
    else:
        immediate = immediate.replace("x","")
        immediate = int(immediate)
        immediate = bin(immediate)[2:]
        immediate = format(int(immediate, 2), '012b')

    rd = str(rd)
    rs1 = str(rs1)
    
    resultado = ''
    
    resultado = immediate + rs1 + func3 + rd + opcode
    print(resultado)

    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    #compressed function 16bits
    # c = 1
    # h = 0
    # opcode = '01'
    # funct3 = '010'
    # rd = linha[1]
    # immediate = linha[2]
    
    # rd = str(rd)
    # rd = rd.replace("x","")
    # rd = int(rd)
    # rd = bin(rd)[2:]
    
    # immediate = str(immediate)
    # complemento_II = False
    
    # if immediate[0] == '0' and immediate[1] == 'x':
    #     immediate = converter_oc_e_hex(immediate,h)
    # elif immediate[0] == '0' and immediate[1] == 'c':
    #     immediate = converter_oc_e_hex(immediate,c)     
    # elif immediate[0] =='-':
    #     complemento_II = True
    #     immediate = int(immediate)
    #     immediate = immediate * -1
    #     immediate = list(bin(immediate)[2:])
    #     for k in range(len(immediate)):
    #         if(immediate[k] == "0"):
    #             immediate[k] = "1"
    #         else:
    #             immediate[k] = "0"
    #     aux = len(immediate)
    #     immediate = int(''.join(immediate),2) + 1 
    #     immediate = bin(immediate)[2:]
    #     immediate = immediate.zfill(aux)
    # else:
    #     immediate = immediate.replace("x","")
    #     immediate = int(immediate)
    #     immediate = bin(immediate)[2:]

    # immediate_aux = ['0']
    # immediate2 = ['0','0','0','0','0']
    # rd_aux = ['0','0','0','0','0']
    
    # x = len(immediate) - 1
    # y = len(rd) - 1
    # v = 0

    # for k in range(6): 
    #     if k == 0:
    #         if(k == 5 - x):
    #             immediate_aux[k] = immediate[v]
    #             v += 1
    #             x -= 1
                
    #     else:
    #         if(k == 5 - x):
    #             immediate2[k-1] = immediate[v]
    #             v += 1
    #             x -= 1
        
    # v = 0    
    # for k in range(5):
    #     if(k == 4 - y):
    #         rd_aux[k] = rd[v]
    #         y -=1
    #         v += 1
    # v = 0
    
    # rd_aux = ''.join(rd_aux)
    # immediate_aux = ''.join(immediate_aux)
    # immediate2 = ''.join(immediate2)
    # resultado = ''


    # resultado = [funct3] + [immediate_aux] + [rd_aux] + [immediate2] + [opcode]
    # print(resultado)
        
    # resultado_hex = converter_oc_e_hex(resultado, 2)
    # resultado_octal = converter_oc_e_hex(resultado, 3)
    # criar.criarArquivo_bin(resultado, num, nome_arq)
    # criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    # criar.criarArquivo_octal(resultado_octal, num, nome_arq)
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
    print(resultado)
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
    return

#100% funcional
def j(linha, num, nome_arq):
    opcode = '1101111'
    rd = '00000'
    immediate = '00000000000000000000'
    resultado = ''
    
    resultado = immediate + rd + opcode
    print(resultado)
    
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
    print(resultado)
    
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
    print(resultado)
    
    resultado_hex = converter_oc_e_hex(resultado, 2)
    resultado_octal = converter_oc_e_hex(resultado, 3)
    criar.criarArquivo_bin(resultado, num, nome_arq)
    criar.criarArquivo_hex(resultado_hex, num, nome_arq)
    criar.criarArquivo_octal(resultado_octal, num, nome_arq)
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
opcode = '0000011' 
    func3 = '010'
    v = 2
    w = 6
    x = len(immediate) - 1
    y = len(rs1) - 1
    z = len(rd) - 1
    
    for j in range(32):
        if j <= 11:
            if j == 12 - x:
                resultado[j] = immediate[x]
                x -= 1
        elif j > 11 and j <= 16:
            if j == 17 - y:
                resultado[j] = rs1[y]
                y -= 1
        elif j > 16 and j <= 19:
            if j == 20 - v:
                resultado[j] = func3[v]
                v -= 1
        elif j > 19 and j <= 23:
            if j == 24 - z:
                resultado[j] = rd[z]
                z -= 1
        elif j > 23 and j <= 31:
            if j == 32 - w:
                resultado[j] = opcode[w]
                w -= 1
    resultado = str(resultado)
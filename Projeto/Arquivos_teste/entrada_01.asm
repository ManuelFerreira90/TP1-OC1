loop:
lw x7, 0b100000000001(x10)
addi x5, x2, -50
sw x9, 500(x10)
sub x5, x6, x7
srl x7, x7, x6
xor x9, x10, x12
beq x10, x9, loop:
jalr x5, x1, -100
mv x5, x2
not x6, x6
li x5, 0c4001
nop
j loop
ret 
neg x6, x6
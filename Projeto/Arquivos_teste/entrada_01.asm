lw x7, 4(x10)
addi x5, x2, -50
sw x9, 0b1010(x10)
sub x5, x6, x7
srl x7, x7, x6
xor x9, x10, x12
beq x10, x9, 100
jalr x5, x1, 6
mv x5, x2
not x6, x6
li x5, 10
nop
j loop
ret 
neg x6, x6
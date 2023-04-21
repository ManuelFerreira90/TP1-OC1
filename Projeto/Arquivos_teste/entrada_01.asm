lw x7, 4(x10)
addi x15, x1, -50
sw x9, 0(x10)
sub x5, x6, x7
srl x7, 0c4, 0xF
xor x9, x10, x12
beq x10, x9, 100
jalr x0, x1, 6
mv x5, x2
jr x0, 0(x10)
li x5, 10
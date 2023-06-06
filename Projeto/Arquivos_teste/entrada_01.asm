addi x5, x5, 50
addi x4, x4, 20
slr x5, x5, x5
and x6, x5, x2
or x7, x2, x5
addi x10, x10, 5
sw x7, 0(x0)
lw x8, 0(x0)
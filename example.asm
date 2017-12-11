section .text

_ADD
ADD A, B
JMP _OUT

_START
LDA A, NUM
LDI B, 7
JMP _ADD

_OUT
OUT A

HLT

section .data

NUM 3
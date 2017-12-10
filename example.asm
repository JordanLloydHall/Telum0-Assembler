section .text

_START

LDA A, NUM
LDI B, 7
ADD A, B

OUT A

section .data

NUM 3
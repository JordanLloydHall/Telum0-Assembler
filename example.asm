
section .text
; Code goes here

_start:
JMpz 44
lda a, hello
jmpz _start
IN A ; Inputs a reg
Out b ; Outputs b reg

section .data

a 44
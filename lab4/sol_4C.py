stringa="75620000 74315f37 7334775f 625f376e 33745572 7230665f 62343363 00216531 24313325 20783830 24323325 20783830 24373325"
l=["0x"+i for i in stringa.split(' ')]
hex_string=[int(i,16) for i in l]
hex_string1=[str(i.to_bytes(4,'little'),'utf-8') for i in hex_string]
print("".join(hex_string1))



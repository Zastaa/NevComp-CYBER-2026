from pwn import *
from factordb.factordb import FactorDB
from Crypto.Util.number import *

def solve_with_factordb(n):
    f = FactorDB(n)
    f.connect()

    factors = f.get_factor_list()

    if len(factors) >= 2:
        return factors
    else:
        status = f.get_status()
        return f"Gagal"

conn = remote('10.10.10.10', 1337)

conn.recvuntil(b'Anda: ')
conn.sendline(b'malasnyoooooyy')

conn.recvuntil(b'Anda: ')
conn.sendline(b'malasnyooooyyV2')

conn.recvuntil(b'Anda: ')
conn.sendline(b'jagobangetkamuh:-')

conn.recvuntil(b'Anda: ')
conn.sendline(b'caesaraseacaesar')

conn.recvuntil(b'Anda: ')
conn.sendline(b'atbash_termasuk_substitution')

conn.recvuntil(b'n=')
n = int(conn.recvline().strip().decode())
conn.recvuntil(b'c=')
c = int(conn.recvline().strip().decode())
conn.recvuntil(b'e=')
e = int(conn.recvline().strip().decode())

conn.recvuntil(b'Anda: ')

result = solve_with_factordb(n)

p = result[0]
phi = p * (p - 1)
d = pow(e, -1, phi)

answer = long_to_bytes(pow(c, d, n))

conn.sendline(answer)

conn.interactive()
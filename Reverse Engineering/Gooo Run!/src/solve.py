import struct
from z3 import *

V54 = 0x48BE0977D21F5CA3
V53 = 0x9D137AC02B55E419
V52 = 0xE5810172D7D6747F

b54 = V54.to_bytes(8, "little")
b53 = V53.to_bytes(8, "little")
b52 = V52.to_bytes(8, "little")

def rol1_8(x):
    x = x & BitVecVal(0xFF, 8)
    return ((x << 1) & BitVecVal(0xFF, 8)) | LShR(x, 7)

s = Solver()
d = [Int(f"d{i}") for i in range(8)]

for i in range(8):
    s.add(And(d[i] >= 0, d[i] <= 9))
    expr = rol1_8(
        BitVecVal(b53[i], 8) +
        ( (BitVecVal((3*i) & 0xFF, 8) + Int2BV(d[i], 8)) ^ BitVecVal(b54[i], 8) )
    )
    s.add(expr == BitVecVal(b52[i], 8))

assert s.check() == sat
m = s.model()
inp = "".join(str(m[d[i]].as_long()) for i in range(8))
print("PIN:", inp)

def rol1(x):
    return ((x << 1) & 0xFF) | (x >> 7)

digits = [ord(c) - 48 for c in inp]
v51 = bytes(
    rol1((b53[i] + (((3*i + digits[i]) ^ b54[i]) & 0xFF)) & 0xFF)
    for i in range(8)
)

v30 = 0
for b in v51:
    v30 = (131 * v30 + b) & 0xFFFFFFFF

blob = (
    bytes([76]) +
    struct.pack("<h", -6210) +
    struct.pack("<i", 1506053295) +
    struct.pack("<Q", 0x2EAFB54BA54540C3) +
    struct.pack("<Q", 0x02C7CC009E60E2D8) +
    struct.pack("<Q", 0x890CBD58A1825CE7)
)

out = []
for j in range(31):
    v32 = (((((v30 << 13) & 0xFFFFFFFF) ^ v30) >> 17) ^ ((v30 << 13) & 0xFFFFFFFF) ^ v30) & 0xFFFFFFFF
    v30 = ((32 * v32) ^ v32) & 0xFFFFFFFF
    out.append((v30 & 0xFF) ^ blob[j])

print("FLAG:", bytes(out).decode("ascii"))

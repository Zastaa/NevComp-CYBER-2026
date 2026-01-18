import random
FLAG = "NevComp{brute_force_the_seed_brahh!}"
MY_SEED = random.randint(0, 999999)

def rotate_left_16(n, d, bits=16):
    return ((n << d) | (n >> (bits - d))) & 0xFFFF

def encrypt(plaintext, seed_value):
    random.seed(seed_value)
    ciphertext = []
    for char in plaintext:
        byte = ord(char)
        key = random.getrandbits(16)
        
        xor_result = byte ^ key
        
        final_val = rotate_left_16(xor_result, 3)
        
        ciphertext.append(final_val)
    return ciphertext

encrypted_data = encrypt(FLAG, MY_SEED)
with open('output.txt', 'w') as f:
    f.write('ciphertext = ' + str(encrypted_data))
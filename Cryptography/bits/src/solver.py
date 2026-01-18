import random

def rotate_right_16(n, d, bits=16):
    return ((n >> d) | (n << (bits - d))) & 0xFFFF

def solve():
    ciphertext = [2915, 22405, 53762, 38757, 32735, 17711, 26517, 65515, 39331, 62059, 8716, 31163, 16597, 58873, 60327, 54336, 61352, 48809, 1439, 46762, 46955, 3382, 18884, 53913, 15437, 6605, 60704, 25341, 29006, 13102, 26713, 49100, 59671, 24728, 51128, 35050]
    
    print("Mencari seed...")
    
    for trial_seed in range(999999):
        random.seed(trial_seed)
        decrypted_attempt = ""
        
        for val in ciphertext:
            key = random.getrandbits(16)
            
            rotated_back = rotate_right_16(val, 3)
            
            char_code = rotated_back ^ key
            
            decrypted_attempt += chr(char_code & 0xFF)
        
        if decrypted_attempt.startswith("NevComp{"):
            print(f"--- SEED DITEMUKAN: {trial_seed} ---")
            print(f"FLAG: {decrypted_attempt}")
            return

    print("Seed tidak ditemukan dalam range tersebut.")

solve()
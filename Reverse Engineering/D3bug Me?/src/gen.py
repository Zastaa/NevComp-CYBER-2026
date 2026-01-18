import sys

FLAG = "NevComp{congratulations_you_managed_to_get_this_ridiculously_long_flag_without_triggering_my_anti_debug_logic_or_maybe_you_patched_it_who_knows_but_one_thing_is_certain_the_program_really_hates_being_watched_stepped_or_paused_so_if_you_see_this_flag_you_deserve_it_well_done}"
KEY_STRING = "Gengg_is_Here"
XOR_KEY = 0x55

def simple_encrypt(plaintext, key):
    key_bytes = [ord(k) for k in key]
    key_len = len(key_bytes)
    encrypted = []
    
    for i, char in enumerate(plaintext):
        p = ord(char)
        k = key_bytes[i % key_len]
        c = p ^ k ^ (i & 0xFF)
        encrypted.append(c)
    return encrypted

def obfuscate_key_string(key_str):
    obfuscated = []
    for char in key_str:
        obfuscated.append(ord(char) ^ XOR_KEY)
    return obfuscated

enc_bytes = simple_encrypt(FLAG, KEY_STRING)
obf_key_bytes = obfuscate_key_string(KEY_STRING)

with open("flag_data.h", "w") as f:
    f.write(f"// Generated Data\n")
    f.write(f"unsigned char encrypted_flag[] = {{ {', '.join(map(str, enc_bytes))} }};\n")
    f.write(f"int flag_len = {len(enc_bytes)};\n\n")
    
    f.write(f"// Hidden Key Data\n")
    f.write(f"unsigned char hidden_key[] = {{ {', '.join(map(str, obf_key_bytes))} }};\n")
    f.write(f"int key_len_val = {len(KEY_STRING)};\n")

print(f"[+] flag_data.h generated successfully!")
print(f"[+] Hidden key & Flag ready.")
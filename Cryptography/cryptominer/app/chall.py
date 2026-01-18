import sys
from Crypto.Util.number import *

def generate_rsa():
    m = bytes_to_long(b"cepet_banget_bang")
    p = getPrime(1024)
    n = p * p
    e = 65537
    c = pow(m, e, n)
    return n, c, e

def challenge():
    mod, cipher, pub = generate_rsa()

    daftar_soal = [
        ["(Base64): bWFsYXNueW9vb29veXk=", "malasnyoooooyy"],
        ["(Hex): 0x6d616c61736e796f6f6f6f79795632", "malasnyooooyyV2"],
        ["(XOR): 1:<49:5<>/0:6.3av", "jagobangetkamuh:-"],
        ["(Classic Cipher | Substitusi): fdhvdudvhdfdhvdu", "caesaraseacaesar"],
        ["(Classic Cipher V2 | Substitusi): zgyzhs_gvinzhfp_hfyhgrgfgrlm", "atbash_termasuk_substitution"],
        [f"(RSA): \nn={mod}\nc={cipher}\ne={pub}", "cepet_banget_bang"]
    ]

    print("=== Crypto Miner Challenge ===")
    print("Selesaikan semua soal untuk mendapatkan Flag!")
    print("-" * 30)

    for i, (teks_soal, kunci_jawaban) in enumerate(daftar_soal, 1):
        print(f"\n[Level {i}]")
        print(teks_soal)
        sys.stdout.write("Jawaban Anda: ")
        sys.stdout.flush()

        input_user = sys.stdin.readline().strip()

        if input_user == kunci_jawaban:
            print(f"CORRECT!")
        else:
            print(f"WRONG! Jawaban yang benar bukan '{input_user}'.")
            print("Koneksi ditutup.")
            sys.stdout.flush()
            return

    print("\n" + "="*30)
    print("CONGRATULATIONS!")
    print("FLAG : NevComp{crypto_miner_eakkkk!?!1337}")
    print("="*30+"\n")
    sys.stdout.flush()

if __name__ == "__main__":
    challenge()
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/ptrace.h>
#include <sys/types.h>

#include "flag_data.h"

void build_key(char *buffer) {
    for(int i = 0; i < key_len_val; i++) {
        buffer[i] = hidden_key[i] ^ 0x55;
    }
    buffer[key_len_val] = '\0'; 
}

void decrypt_flag(char *real_key) {
    int key_len = strlen(real_key);
    char decrypted[1024];

    printf("\n\033[1;34m[*] Password Accepted. Decrypting Root Files...\033[0m\n");
    
    for (int i = 0; i < flag_len; i++) {
        unsigned char c = encrypted_flag[i];
        char p = c ^ real_key[i % key_len] ^ (i & 0xFF);
        decrypted[i] = p;
    }
    decrypted[flag_len] = '\0';

    printf("\033[1;32m[+] FLAG: %s\033[0m\n\n", decrypted);
}

void junk_code() {
    printf("\n\033[1;31m[!] SECURITY BREACH: Debugging tools detected!\033[0m\n");
    printf("[!] System will now self-destruct.\n");
    exit(1337);
}

int main() {
    char input[100];
    char REAL_KEY[100];

    build_key(REAL_KEY); 

    printf("========================================\n");
    printf("           NEVCOMP SECURE VAULT         \n");
    printf("========================================\n");
    
    printf("[?] Enter Access Key: ");
    scanf("%99s", input);

    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {
        junk_code();
    }

    if (strcmp(input, REAL_KEY) == 0) {
        decrypt_flag(REAL_KEY);
    } else {
        printf("\n\033[1;31m[-] Access Denied. Invalid Key.\033[0m\n");
    }

    return 0;
}

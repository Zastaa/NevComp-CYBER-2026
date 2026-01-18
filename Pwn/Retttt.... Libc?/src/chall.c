#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void init() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void useful_gadgets() {
    __asm__("pop %rdi; ret");
    __asm__("pop %rsi; ret");
}

void print_banner() {
    puts("\n");
    puts("  _   _             _____                       ");
    puts(" | \\ | |           / ____|                      ");
    puts(" |  \\| | _____   _| |     ___  _ __ ___  _ __   ");
    puts(" | . ` |/ _ \\ \\ / / |    / _ \\| '_ ` _ \\| '_ \\  ");
    puts(" | |\\  |  __/\\ V /| |___| (_) | | | | | | |_) | ");
    puts(" |_| \\_|\\___| \\_/  \\_____\\___/|_| |_| |_| .__/  ");
    puts("                                        | |     ");
    puts("          SECURE VAULT v2.1             |_|     ");
    puts("------------------------------------------------");
}

void secure_login() {
    char token[72]; 

    printf("[>] Enter Maintenance Authorization Token: ");
    
    read(0, token, 0x100);

    puts("[!] Verifying token...");
    printf("[-] Error: Invalid Token Format.\n");
    puts("[-] Access Denied. Incident reported.");
}

int main() {
    init();
    print_banner();
    secure_login();
    return 0;
}
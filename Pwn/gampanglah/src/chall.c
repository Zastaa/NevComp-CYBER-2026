#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void shell() {
    char code[35];

    printf("[!] Give me your shellcode (max 35 bytes): ");

    read(0, code, 35);

    printf("[*] Executing your code...\n");

    (*(void(*)()) code)();
}

void vuln() {
    char buffer[20];

    printf("[+] Input: ");
    read(0, buffer, 100); 
}

int main() {
    init();
    vuln();
    return 0;
}

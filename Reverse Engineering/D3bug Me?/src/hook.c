#include <stdio.h>

// Override fungsi ptrace sistem
// Kita pake ... (titik tiga) biar cocok sama definisi sistem apapun
long ptrace(int request, ...) {
    // Selalu return 0 (Success)
    // Program akan mengira "Oh, aku berhasil panggil PTRACE_TRACEME, 
    // berarti gak ada debugger lain yang nempel."
    return 0;
}
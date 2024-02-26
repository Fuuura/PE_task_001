#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 15

int check(int *I, int *V, int *X, int *L, int *C, int *D, int *M);
void fck();
void fix_previous(int **n);

int main() {
    int error = 0;
    int I = 0, V = 0, X = 0, L = 0, C = 0, D = 0, M = 0;
    error = check(&I, &V, &X, &L, &C, &D, &M);
    if (error) {
        fck();
        return 1;
    }
    int sum = I + V * 5 + X * 10 + L * 50 + C * 100 + D * 500 + M * 1000;
    printf("%d", sum);
    return 0;
}

int check(int *I, int *V, int *X, int *L, int *C, int *D, int *M) {
    int error = 0;
    char ch;
    while (ch != 10) {
        ch = fgetc(stdin);
        if (ch == 'I') {
            *I = *I + 1;
        } else if (ch == 'V') {
            *V = *V + 1;
            fix_previous(&I);
        } else if (ch == 'X') {
            *X = *X + 1;
            fix_previous(&I);
            fix_previous(&V);
        } else if (ch == 'L') {
            *L = *L + 1;
            fix_previous(&V);
            fix_previous(&X);
        } else if (ch == 'C') {
            *C = *C + 1;
            fix_previous(&X);
            fix_previous(&L);
        } else if (ch == 'D') {
            *D = *D + 1;
            fix_previous(&L);
            fix_previous(&C);
        } else if (ch == 'M') {
            *M = *M + 1;
            fix_previous(&C);
            fix_previous(&D);
        } else if (ch != 10) {
            error++;
            break;
        }
    }
    return error;
}

void fck() { printf("Puck you, Verter!"); }

void fix_previous(int **n) {
    if (**n != 0) **n = **n - 2;
}
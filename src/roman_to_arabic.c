#include <stdio.h>
#include <string.h>

#define MAX_LENGTH 16
#define ROM_FULL 13

int roman_to_arabic(char *str, int *sum);
int nulla(char *str);
void arabic_to_roman(char *roman, int n);
void fix_previous(int *n);
void fck();

int main() {
    int error = 0;
    char str[MAX_LENGTH] = {0};
    int sum = 0;
    fgets(str, MAX_LENGTH, stdin);
    if (str[strlen(str) - 1] == '\n') str[strlen(str) - 1] = '\0';
    if (!nulla(str)) error = roman_to_arabic(str, &sum);
    if (error || strlen(str) == 0) {
        fck();
        return 1;
    }
    printf("%d", sum);
    return 0;
}

int nulla(char *str) {
    return (strcmp(str, "nulla") == 0 || strcmp(str, "nihil") == 0 || strcmp(str, "N") == 0);
}

int roman_to_arabic(char *str, int *sum) {
    int error = 0;
    int I = 0, V = 0, X = 0, L = 0, C = 0, D = 0, M = 0;
    for (int i = 0; str[i]; i++) {
        if (str[i] == 'I') {
            I++;
        } else if (str[i] == 'V') {
            V++;
            fix_previous(&I);
        } else if (str[i] == 'X') {
            X++;
            fix_previous(&I);
        } else if (str[i] == 'L') {
            L++;
            fix_previous(&X);
        } else if (str[i] == 'C') {
            C++;
            fix_previous(&X);
        } else if (str[i] == 'D') {
            D++;
            fix_previous(&C);
        } else if (str[i] == 'M') {
            M++;
            fix_previous(&C);
        } else {
            error++;
            break;
        }
    }
    if (!error) {
        *sum = I + V * 5 + X * 10 + L * 50 + C * 100 + D * 500 + M * 1000;
        char roman[MAX_LENGTH] = {0};
        arabic_to_roman(roman, *sum);
        if (strcmp(str, roman)) error++;
    }
    return error;
}

void fck() { fprintf(stderr, "Puck you, Verter!"); }

void fix_previous(int *n) {
    if (*n != 0) *n = *n - 2;
}

void arabic_to_roman(char *roman, int n) {
    if (n < 0 || n > 3999) return;
    const char full_letters[ROM_FULL][3] = {"M",  "CM", "D",  "CD", "C",  "XC", "L",
                                            "XL", "X",  "IX", "V",  "IV", "I"};
    int MDCLXVI[ROM_FULL] = {0};
    int numbers[ROM_FULL] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    for (int i = 0; i < ROM_FULL; i++) {
        if (n / numbers[i] > 0) {
            MDCLXVI[i] = n / numbers[i];
            n = n % numbers[i];
        }
    }
    for (int i = 0; i < ROM_FULL; i++)
        for (int j = 0; j < MDCLXVI[i]; j++) strcat(roman, full_letters[i]);
}
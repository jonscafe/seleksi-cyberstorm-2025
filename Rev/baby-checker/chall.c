#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void s_n_x(char *flag, int key) {
    int len = strlen(flag);

    for (int i = 0; i < len - 1; i += 2) {
        char temp = flag[i];
        flag[i] = flag[i + 1];
        flag[i + 1] = temp;
    }


    for (int i = 0; i < len; i++) {
        flag[i] ^= key;
    }
}

int check_flag(char *input) {
    char encrypted_flag[] = "\x63\x64\x65\x78\x4c\x7a\x03\x55\x4e\x55\x54\x68\x04\x5f\x5c\x54\x65\x14\x4a";

    char input_copy[sizeof(encrypted_flag)];
    strncpy(input_copy, input, sizeof(input_copy) - 1);
    input_copy[sizeof(input_copy) - 1] = '\0'; 

    int key = 0x1337;
    s_n_x(input_copy, key);

    return strcmp(input_copy, encrypted_flag) == 0;
}

int main() {
    char input[32];

    printf("Enter the flag: ");
    scanf("%31s", input);

    if (check_flag(input)) {
        printf("Correct flag!\n");
    } else {
        printf("Incorrect flag.\n");
    }

    return 0;
}

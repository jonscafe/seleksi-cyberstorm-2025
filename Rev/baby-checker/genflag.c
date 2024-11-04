#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void shuffle_and_xor(char *flag, int key) {
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

int main() {
    char flag[] = "STORM{b4by_ch3ck#R}";
    int key = 0x1337;

    printf("%s\n", flag);

    shuffle_and_xor(flag, key);

    printf("enc flag: ");
    for (int i = 0; i < strlen(flag); i++) {
        printf("\\x%02x", (unsigned char)flag[i]);
    }
    printf("\n");

    return 0;
}

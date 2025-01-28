#include <stdio.h>

int main() {
    int numbers[] = {
        123,124,117,122,115,173,160,145,162,142,141,151,153,151,137,145,154,146,137,162,165,156,137,146,154,141,147,137,162,145,164,162,151,145,166,145,144,137,60,60,145,146,144,141,142,143,145,70,67,67,175
    };

    int size = sizeof(numbers) / sizeof(numbers[0]);

    for (int i = 0; i < size; i++) {
        printf("%d", numbers[i]);
        if (i < size - 1) {
            printf(","); 
        }
    }

    printf("\n"); 
    return 0;
}

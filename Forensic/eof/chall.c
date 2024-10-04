#include <stdio.h>

int main() {
    // Array of numbers to print
    int numbers[] = {
        173,144,141,160,145,164,151,156,137,146,154,141,147,137,144,141,162,151,137,145,154,146,137,171,141,156,147,137,162,165,163,141,153,175
    };

    // Get the size of the array
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // Loop through the array and print each number
    for (int i = 0; i < size; i++) {
        printf("%d", numbers[i]);
        if (i < size - 1) {
            printf(","); // Print a comma after each number except the last one
        }
    }

    printf("\n"); // Print a newline after the last number
    return 0;
}

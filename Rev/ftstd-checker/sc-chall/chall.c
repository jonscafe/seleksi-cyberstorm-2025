#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FLAG_LENGTH 1024

typedef enum {
    STATE_0,
    STATE_1,
    STATE_2,
    STATE_3,
    STATE_4,
    STATE_5,
    STATE_6,
    STATE_7,
    STATE_8,
    STATE_9,
    NUM_STATES
} State;

State transition[NUM_STATES][2] = {
    {STATE_4, STATE_1}, // STATE_0 transitions
    {STATE_3, STATE_5}, // STATE_1 transitions
    {STATE_7, STATE_6}, // STATE_2 transitions
    {STATE_2, STATE_8}, // STATE_3 transitions
    {STATE_0, STATE_9}, // STATE_4 transitions
    {STATE_1, STATE_4}, // STATE_5 transitions
    {STATE_9, STATE_3}, // STATE_6 transitions
    {STATE_6, STATE_2}, // STATE_7 transitions
    {STATE_5, STATE_0}, // STATE_8 transitions
    {STATE_8, STATE_7}  // STATE_9 transitions
};

const char encrypted_flag[] = "498040151515151326980154013851513851540138015154015401385498015138013263263263804976385138013804015138540151385138549726972769727269769851540132726972769727269854015497638513269726976980497263263854976380401326327272726976385401549769727697638049851515497276385401326972698549851326972638549804985497632697272632726976976385497272632727632638013804049854980154015401327269769854015497638040498015151515404049801380404980154980132763263263851540498515154972726980132632698049763804015132727269727697638015154015404015132763804972727263804976327272726380497638540151327272697638515404976326380138049854015401327272638049769769854985151540497697276385154049804972763272697269854980151515497272632638515401327263851515497272";

void shuffle_flag(char *flag) {
    State current_state = STATE_0;
    size_t len = strlen(flag);
    for (size_t i = 0; i < len; ++i) {
        int bit = flag[i] - '0';
        if (bit != 0 && bit != 1) {
            fprintf(stderr, "Invalid character in flag: %c\n", flag[i]);
            exit(EXIT_FAILURE);
        }
        current_state = transition[current_state][bit];
        flag[i] = '0' + current_state;
    }
}

int check_flag(char *input) {
    char input_copy[MAX_FLAG_LENGTH];
    strncpy(input_copy, input, MAX_FLAG_LENGTH - 1);
    input_copy[MAX_FLAG_LENGTH - 1] = '\0'; 
    shuffle_flag(input_copy);

    return strcmp(input_copy, encrypted_flag) == 0;
}

// Main function
int main() {
    char input[MAX_FLAG_LENGTH];

    printf("Enter the flag in binary (only 0s and 1s): ");
    scanf("%1023s", input);

    if (check_flag(input)) {
        printf("Correct flag!\n");
    } else {
        printf("Incorrect flag.\n");
    }

    return 0;
}

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 1024
#define NUM_STATES 10

int t[NUM_STATES][2] = {
    {4, 1},
    {3, 5},
    {7, 6},
    {2, 8},
    {0, 9},
    {1, 4},
    {9, 3},
    {6, 2},
    {5, 0},
    {8, 7}
};

void inv_t(int it[NUM_STATES][NUM_STATES]) {
    for (int i = 0; i < NUM_STATES; i++) {
        for (int j = 0; j < NUM_STATES; j++) {
            it[i][j] = -1;
        }
    }
    
    for (int s = 0; s < NUM_STATES; s++) {
        for (int b = 0; b < 2; b++) {
            int ns = t[s][b];
            it[ns][s] = b;
        }
    }
}

void unshuffle(const char* ef, char* df) {
    int it[NUM_STATES][NUM_STATES];
    inv_t(it);
    int cs = 0;
    size_t len = strlen(ef);

    for (size_t i = 0; i < len; i++) {
        int ns = ef[i] - '0';
        int ob = it[ns][cs];
        df[i] = '0' + ob;
        cs = ns;
    }
    df[len] = '\0';
}

void binary_to_ascii(const char* binary, char* ascii) {
    int len = strlen(binary);
    for (int i = 0; i < len; i += 8) {
        char byte[9] = {0};
        strncpy(byte, binary + i, 8);
        ascii[i / 8] = (char)strtol(byte, NULL, 2);
    }
    ascii[len / 8] = '\0';
}

int main() {
    const char* ef = "498040151515151326980154013851513851540138015154015401385498015138013263263263804976385138013804015138540151385138549726972769727269769851540132726972769727269854015497638513269726976980497263263854976380401326327272726976385401549769727697638049851515497276385401326972698549851326972638549804985497632697272632726976976385497272632727632638013804049854980154015401327269769854015497638040498015151515404049801380404980154980132763263263851540498515154972726980132632698049763804015132727269727697638015154015404015132763804972727263804976327272726380497638540151327272697638515404976326380138049854015401327272638049769769854985151540497697276385154049804972763272697269854980151515497272632638515401327263851515497272";

    char df[MAX_LEN];
    unshuffle(ef, df);

    char check[MAX_LEN];
    binary_to_ascii(df, check);

    char user_input[MAX_LEN];
    printf("Masukkan flag: ");
    scanf("%s", user_input);

    if (strcmp(user_input, check) == 0) {
        printf("Benar!\n");
    } else {
        printf("Salah! Coba lagi.\n");
    }

    return 0;
}

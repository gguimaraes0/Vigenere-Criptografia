# from socket import *
# serverName = "172.20.10.14" # IPv4 // ::1 IPv6
# serverPort = 12500
# clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET6
# print("UDP Client\n")
# while 1:
#     message = input("Input message: ")
#     if message == "exit":
#             break
#     clientSocket.sendto(bytes(message,"utf-8"), (serverName, serverPort))
# clientSocket.close()

from socket import *

def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_len = len(key)
    
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % key_len]
        encrypted_char = chr(ord(char) + ord(key_char))
        encrypted_text += encrypted_char
    
    return encrypted_text

serverName = "192.168.0.39"
serverPort = 12500
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("UDP Client\n")
key = "CHAVE"

while True:
    message = input("Input message: ")
    if message == "exit":
        break

    encrypted_message = vigenere_encrypt(message, key)
    clientSocket.sendto(bytes(encrypted_message, "utf-8"), (serverName, serverPort))

clientSocket.close()

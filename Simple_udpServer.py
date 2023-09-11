# from socket import *
# serverPort = 12500
# serverSocket = socket(AF_INET, SOCK_DGRAM)
# serverSocket.bind(("",serverPort))
# print ("UDP server\n")
# while 1:
#     message, clientAddress = serverSocket.recvfrom(2048)
#     text = str(message,"utf-8") #cp1252 #utf-8
#     print ("Received from Client: ", text)

from socket import *

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_len = len(key)
    
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % key_len]
        decrypted_char = chr(ord(char) - ord(key_char))
        decrypted_text += decrypted_char
    
    return decrypted_text

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print("UDP server\n")
key = "CHAVE"

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message, "utf-8")
    decrypted_message = vigenere_decrypt(text, key)
    print("Received from Client (Encrypted):", text)
    print("Decrypted Message:", decrypted_message)

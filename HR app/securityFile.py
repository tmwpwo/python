import random
import hexdump


class security():
    def encrypt(key, plaintext):
        
        plaintext = list(plaintext)#Convert the plaintext to a list of characters
        random.seed(key)
        
        keystream = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(plaintext))]# Generate a random stream of characters to use as the keystream
        
        
        ciphertext = [chr(ord(a) ^ ord(b)) for (a, b) in zip(plaintext, keystream)]# Perform the encryption by XORing the plaintext with the keystream
        
        return ''.join(ciphertext)

    def decrypt(key, ciphertext):
        random.seed(key)
        
        keystream = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(len(ciphertext))]# Generate the keystream using the same method as the encrypt() function
        
        
        plaintext = [chr(ord(a) ^ ord(b)) for (a, b) in zip(ciphertext, keystream)]# Decrypt the ciphertext by XORing it with the keystream
        
        return ''.join(plaintext)





# print('Plaintext:', "assignment")
# print(hexdump.dump(bytes("assignment", encoding='utf-8'), sep=" "))
# print('Ciphertext:', obj)
# print(hexdump.dump(bytes(obj, encoding='utf-8'), sep=" "))
# # print('Decrypted:', obj1)
# # print(hexdump.dump(bytes(obj1, encoding='utf-8'), sep=" "))
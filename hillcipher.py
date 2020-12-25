import numpy as np

class HillCipher:
    '''
        Works on the principle of Linear Algebra.
        Encrypted text is derived after multiplying the plaintext
        character with a KEY matrix. 
        Decryption works by multiplying the Cipher text with the
        inverse of key matrix
    '''

    key = None
    size = None
    def __init__(self, key="encryptit"):
        self.size = int(len(key)**(1/2))
        self.key = np.zeros((self.size, self.size), dtype=np.int32)
        for i in range(self.size):
            self.key[i] = [ord(i) for i in key[i*self.size:self.size*(i+1)]]
        print(self.key)

    def shift(self,char):
        # if char > 96:
        #     ans = (char - 97) % (122 - 97 + 1) + 97
        # else:
        #     ans = (char - 65) % (90 - 65 + 1) + 65
        ans = (char - 97) % (122 - 97 + 1) + 97
        return chr(ans)


    def encrypt(self, message):
        if len(message) > self.size:
            print("Error: Length of the entered message should equal the length of key")
            return
        else:
            plaintext = [ord(i) for i in message.lower()]
            cipher = np.matmul(self.key, plaintext)
            ciphertext = [self.shift(x) for x in cipher]
            print("Original Text: {}\nEncrypted Text: {}".format(message, "".join(ciphertext)))

    def decrypt(self, message):
        if len(message) > self.size:
            print("Error: Length of the entered message should equal the length of key")
            return
        else:
            ciphertext = [ord(i) for i in message.lower()]
            cipher = np.matmul(np.linalg.inv(self.key), np.array(ciphertext))
            # print(np.linalg.inv(self.key))
            plaintext = [self.shift(int(x)) for x in cipher]
            print("Encrypted Text: {}\nOriginal Text: {}".format(message, "".join(plaintext)))



if __name__ == "__main__":
    ob = HillCipher()
    ob.encrypt("anu")
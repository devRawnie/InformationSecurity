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
    def __init__(self, key="alphabeta"):
        self.size = int(len(key)**(1/2))
        self.key = np.zeros((self.size, self.size), dtype=np.int32)
        for i in range(self.size):
            self.key[i] = [ord(j)-97 for j in key[i*self.size:self.size*(i+1)]]
        print(self.key)

    def shift(self,char):
        # if char > 96:
        #     ans = (char - 97) % (122 - 97 + 1) + 97
        # else:
        #     ans = (char - 65) % (90 - 65 + 1) + 65
        ans = (char - 97) % (122 - 97 + 1) + 97
        return chr(ans)

    def getInverseDeterminant(self, key):
        det = round(np.linalg.det(key), 1) % 26
        i = 1
        while True:
            if det*i % 26 == 1.0:
                return i
            i += 1 

    def getInverse(self, key):
        dinv = self.getInverseDeterminant(key)
        kinv = np.zeros((self.size, self.size), dtype=np.int32)
        for i in range(self.size):
            for j in range(self.size):
                kinv[i,j] = self.key[i]

        exit(0)

    def encrypt(self, message):
        message = message.replace(" ", "").lower()
        if len(message) % self.size != 0:
            print("Error: Length of the entered message should a multiple of the length of key")
            return
        else:
            components = [message[i:i+self.size] for i in range(0, len(message), self.size)]
            output = []
            for msg in components:
                plaintext = [ord(i) for i in msg]
                cipher = np.matmul(self.key, plaintext)
                ciphertext = [chr(x%26 + 97) for x in cipher]
                output.append("".join(ciphertext))
            print("Original Text: {}\nEncrypted Text: {}".format(message, "".join(output)))

    def decrypt(self, message):
        message = message.replace(" ","").lower()

        if len(message) % self.size != 0:
            print("Error: Length of the entered message should be a multiple of the length of key")
            return
        else:
            # inverse = self.getInverse(self.key)
            print(np.linalg.inv(self.key))
            exit(0)
            components = [message[i:i+self.size] for i in range(0, len(message), self.size)]
            ciphertext = [ord(i) for i in message.lower()]
            cipher = np.matmul(np.linalg.inv(self.key), np.array(ciphertext))
            # print(np.linalg.inv(self.key))
            plaintext = [self.shift(int(x)) for x in cipher]
            print("Encrypted Text: {}\nOriginal Text: {}".format(message, "".join(plaintext)))



if __name__ == "__main__":
    ob = HillCipher()
    # ob.encrypt("Hey Are You May")
    ob.decrypt("ioazfblkkwkm")
import numpy as np
from math import pow

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

    def getInverseDeterminant(self):
        det = round(np.linalg.det(self.key), 1) % 26
        i = 1
        while True:
            if det*i % 26 == 1.0:
                return i
            i += 1 

    def getInverse(self):
        dinv = self.getInverseDeterminant()
        kinv = np.zeros((self.size, self.size), dtype=np.int32)
        for i in range(self.size):
            for j in range(self.size):
                x = np.delete(self.key, i, axis=0)
                x = np.delete(x, j, axis=1)
                det = x[0,0]*x[1,1] - x[1,0]*x[0,1]
                kinv[i,j] =  int(pow(-1, i+j)) * det % 26
        return (dinv * kinv.transpose()) % 26
        

    def encrypt(self, message):
        message = message.replace(" ", "").lower()
        if len(message) % self.size != 0:
            print("Error: Length of the entered message should a multiple of the length of key")
            return
        else:
            components = [message[i:i+self.size] for i in range(0, len(message), self.size)]
            output = []
            for msg in components:
                plaintext = [ord(i)-97 for i in msg]
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
            inverse = self.getInverse()
            components = [message[i:i+self.size] for i in range(0, len(message), self.size)]
            output = []
            for msg in components:
                ciphertext = [ord(i)-97 for i in msg]
                cipher = np.matmul(inverse, np.array(ciphertext))
                plaintext = [chr(x%26+97) for x in cipher]
                output.append("".join(plaintext))
            print("Decrypted Text: {}\nOriginal Text: {}".format(message, "".join(output)))



if __name__ == "__main__":
    ob = HillCipher("alphabeta")    # Passing key in the constructor
    ob.encrypt("Hey folkss")
    # ob.decrypt("ovahuaaks")

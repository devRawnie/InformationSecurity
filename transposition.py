from random import sample
import numpy as np

class Transposition:

    def __init__(self, key=4312567):
        self.key = [int(i) for i in str(key)]
        self.size = len(self.key)

    def process(self, text):
        leftover = self.size - (len(text) % self.size)
        extra = sample(range(65, 90), leftover)
        characters = [chr(i) for i in extra]
        return text + "".join(characters)
    
    def encrypt(self, message):
        plaintext = message.replace(" ", "")
        
        # Append extra characters to make the message compatible with the key size
        if len(plaintext) % self.size != 0:
            plaintext = self.process(plaintext)        

        # Divide the message into key sized components
        components = np.array([list(plaintext[i:i+self.size]) for i in range(0, len(plaintext), self.size)])
        output = []
        for i in range(self.size):
            output.append("".join(components[:,self.key.index(i+1)]))
        print("Original text: {}\nEncrypted text: {}".format(plaintext, "".join(output)))

    def decrypt(self, message):
        block = len(message) // len(self.key)

        # Convert encrypted text into decryption matrix
        components = np.array([list(message[i:i+block]) for i in range(0, len(message), block)])

        output = []
        for i in self.key:
            temp = components[i-1:i,].tolist()[0]
            output.append(temp)

        # Extract plain text column wise
        output = np.array(output)
        plaintext = []
        for i in range(output.shape[1]):
            plaintext.append("".join(output[:,i].tolist()))

        print("Encrypted text: {}\nDecrypted text: {}".format(message, "".join(plaintext)))

if __name__ == "__main__":
    ob = Transposition()
    # ob.encrypt("ATTACK POSTPONED UNTIL TWO AM")
    ob.decrypt("TTNAAPTMTSUOAODWCOISKNLJPETH")
    
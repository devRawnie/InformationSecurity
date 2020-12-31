from random import randint

class FAttack:
    def __init__(self):
        self.key = randint(1, 27)
        self.ciphertext = None
        self.frequency = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]

    def hamming(self, attempt):
        distance = 0
        for i in range(len(self.ciphertext)):
            distance += abs(ord(attempt[i]) - ord(self.ciphertext[i]))
        return distance

    def encrypt(self, filename):
        message = None
        with open(filename, "r") as file:            
            message = file.read().lower()
        if message is None:
            print("Error: Invalid plaintext")
            exit(0)

        cipher = []
        for char in message:
            if char != " ":
                nword = (ord(char)+self.key - 97 ) % 26 + 97
                cipher.append(chr(nword))
            else:
                cipher.append(char)

        self.ciphertext = "".join(cipher)

        with open("ciphertext.txt", "w") as f:
            f.write("CIPHERTEXT:\n")
            f.write(self.ciphertext)

    def generateFrequency(self, message):
        f = {}
        for i in message:
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        return f

    def breakCipher(self):
        freq = self.generateFrequency(self.ciphertext)
        freq = {key: val for key, val in sorted(freq.items(), key= lambda ele: ele[1], reverse=True)}
        cipherFreq = list(freq.keys())[1:]
        print(cipherFreq)
        lookup = {cipherFreq[i]: self.frequency[i] for i in range(len(cipherFreq))}
        attempt = []
        for i in range(len(self.ciphertext)):
            if self.ciphertext[i] == " ":
                attempt.append(" ")
            else:
                attempt.append(lookup[self.ciphertext[i]])
        ans = "".join(attempt)
        # print(len(ans))
        # print(len(self.ciphertext))
        # exit(0)
        distance = self.hamming(ans)
        with open("attempt1.txt", "w") as f:
            f.write(str(distance))
            f.write("\n")
            f.write(ans)

                

if __name__ == "__main__":
    ob = FAttack()
    ob.encrypt("plaintext.txt")
    ob.breakCipher()
from random import randint

class FAttack:
    def __init__(self, plainfile, cipherfile=None):
        self.key = randint(1, 27)
        self.plainfile = plainfile
        if cipherfile is None:
            self.cipherfile = plainfile.split(".")[0] + " cryptanalysis.txt"
        else:
            self.cipherfile = cipherfile 
        self.ciphertext = None
        self.frequency = ["e","t","a","o","i","n","s","h","r","d","l","c","u","m","w","f","g","y","p","b","v","k","j","x","q","z"]

    def hamming(self, l1, l2):
        distance = 0
        for i in range(len(l1)):
            distance += abs(ord(l1[i]) - ord(l2[i]))
        return distance

    def write_to_file(self, filename, message=None, heading="", mode="w"):
        with open(filename, mode) as file:
            file.write(heading)
            if message is not None:
                for line in message:
                    file.write(line)
                    file.write("\n")

    def encrypt(self):
        message = []
        try:
            with open(self.plainfile, "r") as file:            
                message = list(map(lambda x: x.lower().rstrip("\n"), file.readlines()))
            if len(message) == 0:
                raise Exception("Error: No content in file")
        except Exception as e:
            print(str(e))
            print("here")
            exit(0)

        cipher = [[] for _ in range(len(message))]

        for i in range(len(message)):
            for char in message[i]:
                if char != " ":
                    nword = (ord(char)+self.key - 97 ) % 26 + 97
                    cipher[i].append(chr(nword))
                else:
                    cipher[i].append(char)
            cipher[i] = "".join(cipher[i])

        self.ciphertext = cipher
        self.write_to_file(filename=self.cipherfile, message=self.ciphertext, heading="--->CIPHERTEXT\n")


    def generateFrequency(self, message):
        f = {}
        for i in ":".join(message):
            if i in f:
                f[i] += 1
            else:
                f[i] = 1
        f.pop(":")
        return f

    def decrypt(self, lookup):
        attempt = [[] for _ in range(len(self.ciphertext))]
        for i in range(len(self.ciphertext)):
            for char in self.ciphertext[i]:
                if char == " ":
                    attempt[i].append(" ")
                else:
                    attempt[i].append(lookup[char])
            attempt[i] = "".join(attempt[i])
        
        distance = sum([self.hamming(attempt[i], self.ciphertext[i]) for i in range(len(attempt))])

        self.write_to_file(filename=self.cipherfile, message=attempt, heading="\n\n--->Hamming Distance: %d\n" % distance, mode="a")        


    def breakCipher(self):
        self.write_to_file(filename=self.cipherfile, heading="\n--->CRYPTANALYSIS\n", mode="a")        

        freq = self.generateFrequency(self.ciphertext)
        freq = {key: val for key, val in sorted(freq.items(), key= lambda ele: ele[1], reverse=True)}
        cipherFreq = list(freq.keys())[1:]

        lookup = {cipherFreq[i]: self.frequency[i] for i in range(len(cipherFreq))}

if __name__ == "__main__":
    ob = FAttack("plaintext.txt")
    ob.encrypt()
    ob.breakCipher()
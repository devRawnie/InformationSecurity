class Vignere:
    key = None
    keypos = None
    def __init__(self, key="LUCK"):
        self.key = key
        self.keypos = 0

    def keyChar(self, backward=False):
        x = ord(self.key[self.keypos % 4])
        self.keypos += 1
        return x if not backward else -1*x


    def shift(self, segment, backward=False):
        result = []
        for char in segment:
            temp = ord(char)
            if temp > 96:
                ans = ((temp + self.keyChar(backward) - 97) % (122 - 97 + 1)) + 97
            else:
                ans = ((temp + self.keyChar(backward) - 65) % (90 - 65 + 1)) + 65
            result.append(chr(ans))
        return "".join(result)


    def encrypt(self, message):
        if message is None or len(message) == 0:
            print("Error: Invalid text passed")
        else:
            cipher = [self.shift(x) for x in message.split()]
            return " ".join(cipher)

    def decrypt(self, message):
        if message is None or len(message) == 0:
            print("Error: Invalid text passed")
        else:
            cipher = [self.shift(x, True) for x in message.split()]
            return " ".join(cipher)

if __name__ == "__main__":
    ob = Vignere()
    result = ob.encrypt("CRYPTOGRAPHY IS LOVE")
    # result = ob.decrypt("AYNMRVVOYWWV")
    print(result)
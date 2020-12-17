# Implementing encryption and decryption with caesar cipher

# Code fragment to rotate the values between an interval [min, max]:
# # ((val-min) `mod` (max-min+1)) + min
class Caesar:
    key = None
    def __init__(self, key=None):
        if key is not None:
            self.key = key

    def setKey(self, key=None):
        if key is not None:
            self.key = key
        else:
            print("Error: Invalid/Missing key value")

    def shiftForward(self, char,lower=True,key=None):
        ans = None
        if key is None:
            key = self.key
        if lower:
            ans = ((char + key - 97) % (122 - 97 + 1)) + 97
        else:
            ans = ((char + key - 65) % (90 - 65 + 1)) + 65
        return ans

    def shiftBackward(self, char, lower=True, key=None):
        ans = None
        if key is None:
            key = self.key
        if lower:
            ans = ((char - key - 97) % (122 - 97 + 1)) + 97
        else:
            ans = ((char - key - 65) % (90 - 65 + 1)) + 65
        return ans
                
    def encrypt(self, message):
        op =[]
        for x in message:
            oldchar = ord(x)
            newchar = self.shiftForward(oldchar) if oldchar > 96 else self.shiftForward(oldchar, False)
            op.append(chr(newchar))
        return "".join(op)

    def decryptMessage(self, message):
        op =[]
        for x in message:
            oldchar = ord(x)
            newchar = self.shiftBackward(oldchar) if oldchar > 96 else self.shiftBackward(oldchar,False)
            op.append(chr(newchar))
        return "".join(op)


if __name__ == '__main__':
    inp = input("Enter the text to be encrypted: ").split()
    k = int(input("Enter the key: "))
    # output = [decryptMessage(word, k) for word in inp]

    # print(*output, sep=" ")
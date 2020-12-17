class Caesar:
    key = None
    def __init__(self, key=None):
        if key is not None:
            self.key = key

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
        message = message.split()
        msg = []
        for word in message:
            op =[]
            for x in word:
                oldchar = ord(x)
                newchar = self.shiftForward(oldchar) if oldchar > 96 else self.shiftForward(oldchar, False)
                op.append(chr(newchar))
            msg.append("".join(op))
        
        return " ".join(msg)
    
    def decrypt(self, message):
        message = message.split()
        msg = []
        for word in message:
            op =[]
            for x in word:
                oldchar = ord(x)
                newchar = self.shiftBackward(oldchar) if oldchar > 96 else self.shiftBackward(oldchar, False)
                op.append(chr(newchar))
            msg.append("".join(op))

        return " ".join(msg)

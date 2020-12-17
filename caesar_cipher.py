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
#############################################
class CaesarFB(Caesar):
    front = None
    back = None
    p = None

    def setParam(self, front, back, p):
        if front is not None:
            self.front = front
        else:
            print("Error: Invalid argument 1")
        if back is not None:
            self.back = back
        else:
            print("Error: Invalid argument 2") 
        if p is not None:
            self.p = p
        else:
            print("Error: Invalid argument 3")

    def forward(self, portion, key=None):
        op = []
        if key is None:
            key = self.front
        for p in portion:
            oldchar = ord(p)
            if oldchar == 32:
                op.append(p)
            else:
                newchar = self.shiftForward(oldchar,key=key) if oldchar > 96 else self.shiftForward(oldchar, False, key)
                op.append(chr(newchar))            

        return "".join(op)

    def backward(self, portion, key=None):
        op = []
        if key is None:
            key = self.back
        for p in portion:
            oldchar = ord(p)
            if oldchar == 32:
                op.append(p)
            else:
                newchar = self.shiftBackward(oldchar,key=key) if oldchar > 96 else self.shiftBackward(oldchar, False, key)
                op.append(chr(newchar))            

        return "".join(op)


    def encrypt(self, message):
        forward = self.forward(message[:self.p-1])
        backward = self.backward(message[self.p-1:])
        return (forward + backward)
    
    def decrypt(self, message):
        forward = self.backward(message[:self.p-1],self.front)
        backward = self.forward(message[self.p-1:],self.back)
        return forward + backward


if __name__ == '__main__':
    inp = input("Enter the text to be encrypted: ")
    # k = int(input("Enter the key: "))
    cipher = CaesarFB()
    cipher.setParam(2,1,2)
    enc = cipher.encrypt(message=inp)
    print(enc)
    dec = cipher.decrypt(message=enc)
    print(dec)
    # print(*output, sep=" ")
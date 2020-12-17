from caesar_cipher import Caesar

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
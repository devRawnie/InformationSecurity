class Vernam:
    key = None
    def __init__(self, key="01101001"):
        self.key = int(key, 2)
    
    def encrypt(self, message="11011011"):
        plain = int(message, 2)
        result = bin(plain ^ self.key)[2:]
        print(result)
    
    def decrypt(self, message="110011011"):
        cipher = int(message, 2)
        result = bin(cipher ^ self.key, 2)[2:]
        print(result)
    
if __name__ == "__main__":
    ob = Vernam()
    ob.encrypt()
    
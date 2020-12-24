from caesar_cipher import Caesar
from caesar_forward_backward import CaesarFB


def implementCaesar():
    inp = input("Enter the text to be encrypted: ")
    # key = int(input("Enter the key: "))   ## Default is 3
    cipher = Caesar()
    print("Original Text: {}\nEncrypted Text: {}".format(inp, cipher.encrypt(inp)))

def implementCaesarFB():
    inp = input("Enter the text to be encrypted: ")
    f = int(input("Enter the key for forward shift: "))
    b = int(input("Enter the key for backward shift: "))
    p = int(input("Enter the point of shift: "))
    cipher = CaesarFB()
    cipher.setParam(f,b,p)
    print("Original Text: {}\nEncrypted Text: {}".format(inp, cipher.encrypt(inp)))

if __name__ == '__main__':
    implementCaesarFB()
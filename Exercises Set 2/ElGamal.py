from random import randint
from utility import get_prime, fast_exponentiation, find_root

class User():
    def __init__(self, name=None):
        if name is None:
            print("Invalid name")
            return
        self.name = name

    def keygen(self):
        self.prime = get_prime(start=10, end=15)
        self.root = find_root(self.prime)

        self.k_pri = randint(2, self.prime-2)
        self.k_pub = fast_exponentiation(self.root, self.k_pri, self.prime)

        return {"pub":self.k_pub,"prime": self.prime,"root": self.root}

    def encrypt(self, message, key):
        if message is None:
            print("Invalid Message")
            exit(0)
        if key is None:
            print("Invalid key")
            exit(0)
        #Generate Public Mask
        temp_key  = randint(2, key["prime"]-2)
        k_pub = fast_exponentiation(key["root"], temp_key, key["prime"])
        mask = fast_exponentiation(key["pub"], temp_key, key["prime"])
        output = []
        for char in message:
            y = (ord(char)*mask) % key["prime"]
            output.append(y)
        output = ":".join(map(str, output))
        print("User: {}\nPublic Key: {}\nMessage: {}\n".format(self.name, k_pub, output))
        return output, k_pub
    
    def decrypt(self, cipher, pub_key):
        if cipher is None:
            print("Invalid Message")
            exit(0)
        if pub_key is None:
            exit(0)
        #Generate Public Mask
        maskinv = fast_exponentiation(pub_key, self.prime-1-self.k_pri, self.prime)
        output = []
        for ichar in cipher.split(":"):
            y = (int(ichar) * maskinv) % self.prime 
            output.append(chr(y))
        output = "".join(output)
        print("User: {}\nPublic Key: {}\nMessage: {}\n".format(self.name, self.k_pub, output))

if __name__ == '__main__':
    bob = User("Bob")
    alice = User("Alice")
    
    # Generate keys for both users
    alice_key = alice.keygen()
    print("\nPublic variables: \n")
    print("Prime Number: {}\nPrimitive Element: {}\n".format(alice_key["prime"], alice_key["root"]))
    
    # Encrypt and Decrypt
    cipher, public_key = bob.encrypt("This is ElGamel!!", alice_key)
    alice.decrypt(cipher, public_key)


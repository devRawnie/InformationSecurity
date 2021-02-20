import random
from math import gcd
from utility import get_prime, find_modulo_inverse, fast_exponentiation

class Keygen:
    @staticmethod
    def generate_key():
        n1 = get_prime()
        n2 = get_prime()
        n = n1*n2
        phi  = (n1-1)*(n2-1)
        e = None
        d = None
        for i in range(3,phi):
            if i != n1 and i != n2:
                if gcd(phi, i) == 1:
                    e = i
                    break
        if e is not None:
            d = find_modulo_inverse(e, phi)
            if d is None:
                return Keygen.generate_key()
        else:
            return Keygen.generate_key()
        return {"pub":(e,n), "pri":(d,n)}
    
def generate_keys(n=1):
    keys = {}
    for i in range(n):
        keys[i] = Keygen.generate_key(i)

    return keys

class RSA:
    def generate_key_pool(self):
        names = ["Alice", "Bob"]
        pool = {}
        self.users = {}
        keys = generate_keys(len(names))
        for i in range(len(names)):
            user = User(i+1, names[i], keys[i]["pri"], keys[i]["pub"])
            pool[names[i]] = user.key
            self.users[names[i]] = user

        return pool

    @staticmethod
    def encrypt(text, key):
        e, n = key
        output = []
        for char in text:
            temp = fast_exponentiation(ord(char), e, n)    
            output.append(temp)

        return ":".join(map(str, output))
    
    @staticmethod
    def decrypt(text, key):
        cipher = list(map(int, text.split(":")))
        d, n = key
        output = []
        for val in cipher:
            temp = fast_exponentiation(val, d, n)    
            output.append(chr(temp))

        return "".join(output)



class User:
    k_pub = None
    k_pri = None
    def __init__(self, name=None):
        if name is None:
            print("Invalid name argument")
            exit(0)
        self.name = name
        self.keygen()
        
    def keygen(self):
        keys = Keygen.generate_key()
        self.k_pub = keys["pub"]
        self.k_pri = keys["pri"]

    def encrypt(self, text, key):
        return RSA.encrypt(text, key)
    
    def decrypt(self, text):
        return RSA.decrypt(text, self.k_pri)

    def key(self):
        return self.k_pub

    def __str__(self):
        return "\nName: {}\nPublic Key: {}".format(self.name, self.k_pub)


def main():
    alice = User("Alice")
    bob = User("Bob")
    cipher = alice.encrypt("This is RSA!!", bob.key())
    print(alice)
    print("\n---->Encrypted Text:\n\n%s" % cipher)
    plaintext = bob.decrypt(cipher)
    print(bob)
    print("\n---->Decrypted Text:\n\n%s" % plaintext)



if __name__ == '__main__':
    main()
    
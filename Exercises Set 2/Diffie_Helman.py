from random import randint
from utility import get_prime, fast_exponentiation, find_root
from math import sqrt
class Diffie_Helman:
    @staticmethod
    def initialize():
        ## Generate prime number
        prime = get_prime(start=10, end=15)
        # prime = 761
        root = find_root(prime)
        if root is None:
            return Diffie_Helman.initialize()
        print("\nPublic Variables:\nPrime Number: {}\nPrimitive Root: {}\n".format(prime, root))
        return (prime, root)


    @staticmethod
    def generate_key(prime, root):
        k_pri = randint(2, prime-2)
        k_pub = fast_exponentiation(root, k_pri, prime)
        return {"pub":k_pub, "pri":k_pri}

class User:
    def __init__(self, name=None, prime=None, root=None):
        if name is None:
            raise Exception("Invalid name")
        if prime is None:
            raise Exception("Invalid prime value")
        if root is None:
            raise Exception("Invalid root value")
        self.name = name
        self.prime = prime
        self.root = root


    def keygen(self):
        keys = Diffie_Helman.generate_key(self.prime, self.root)
        self.k_pri = keys["pri"]
        self.k_pub = keys["pub"]
        return self.k_pub

    def exchange(self, public):
        self.result = fast_exponentiation(public, self.k_pri, self.prime)
        print(self)
    
    def __str__(self):
        return "User: {}\nPublic Key: {}\nFinal Key: {}\n".format(self.name, self.k_pub, self.result)


if __name__ == '__main__':
    prime, root = Diffie_Helman.initialize()
    alice = User("Alice", prime, root)
    bob = User("Bob", prime, root)
    alice_public = alice.keygen()
    bob_public = bob.keygen()
    alice.exchange(bob_public)
    bob.exchange(alice_public)
    
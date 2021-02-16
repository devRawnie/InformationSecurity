from random import randint

class Diffie_Helman:
    @staticmethod
    def initialize():
        ## Generate prime number equal to alpha
        alpha = 761
        root = Diffie_Helman.find_root(alpha)
        print("\nPublic Variables:\nPrime Number: {}\nPrimitive Root: {}\n".format(alpha, root))
        return (alpha, root)
    
    @staticmethod
    def find_root(num):
        return 6
    
    @staticmethod
    def fast_exponentiation(base, exp, n):
        """
            Iteratively finds the result of the expression base^exp mod n
        """
        bin_exp = bin(exp)[2:]
        output = 1
        for i in bin_exp:
            output = (output ** 2) % n
            if i == "1":
                output = (output*base) % n
        return output
    
    @staticmethod
    def generate_key(alpha, root):
        k_pri = randint(1, alpha)
        k_pub = Diffie_Helman.fast_exponentiation(root, k_pri, alpha)
        return {"pub":k_pub, "pri":k_pri}

class User:
    def __init__(self, name=None, alpha=None, root=None):
        if name is None:
            raise Exception("Invalid name")
        if alpha is None:
            raise Exception("Invalid Alpha value")
        if root is None:
            raise Exception("Invalid root value")
        self.name = name
        self.alpha = alpha
        self.root = root


    def keygen(self):
        keys = Diffie_Helman.generate_key(self.alpha, self.root)
        self.k_pri = keys["pri"]
        self.k_pub = keys["pub"]
        return self.k_pub

    def exchange(self, public):
        self.result = Diffie_Helman.fast_exponentiation(public, self.k_pri, self.alpha)
        print(self)
    
    def __str__(self):
        return "User: {}\nPublic Key: {}\nFinal Key: {}\n".format(self.name, self.k_pub, self.result)


if __name__ == '__main__':
    alpha, root = Diffie_Helman.initialize()
    alice = User("Alice", alpha, root)
    bob = User("Bob", alpha, root)
    alice_public = alice.keygen()
    bob_public = bob.keygen()
    alice.exchange(bob_public)
    bob.exchange(alice_public)
    
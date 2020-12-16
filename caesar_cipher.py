# ((val-min) `mod` (max-min+1)) + min
minN = 97
maxN = 122
rhs = maxN - minN + 1
modulo = lambda val: ((val-minN) % rhs) + minN
def encrypt(text, key):
    op =[]
    for x in text:
        oldchar = ord(x)
        newchar = modulo(oldchar + key)
        op.append(chr(newchar))
    return "".join(op)


if __name__ == '__main__':
    inp = input("Enter the text to be encrypted: ").lower().split()
    k = int(input("Enter the key: "))
    output = []
    for word in inp:
        output.append(encrypt(word, k))

    print(*output, sep=" ")
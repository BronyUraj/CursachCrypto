import Static


def are_coprime(a, b):
    hcf = 1
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf == 1


def keyGenerator(p, q):
    n = p * q
    d = None
    phiN = (p - 1) * (q - 1)
    for i in range(2, phiN):
        if are_coprime(i, phiN):
            d = i
            break
    if d is None:
        raise Exception(f"Bad p and q. Can't find d")
    e = pow(d, -1, phiN)
    return d, e, n


def textToCode(text):
    return [Static.__alphabetRus[x] for x in text]


def codeToText(code):
    return "".join(["АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"[x - 1] for x in code])

def crypt(text, key, n):
    result = []
    for char in text:
        result.append(char ** key % n)
    return result



if __name__ == "__main__":
    p = 31
    q = 19
    d, e, n = keyGenerator(p, q)
    print(f"Generated keypairs: OpenKey = ({e}, {n}); SecretKey = ({d}, {n})")
    opentext = "ГЮЮ"
    opentextNums = textToCode(opentext)
    print(f"OpenText Nums = {opentextNums}")
    ciphertext = crypt(opentextNums, e, n)
    print(f"CipherText = {ciphertext}")
    decryptedNums = crypt(ciphertext, d, n)
    print(f"Decrypted TextNums = {decryptedNums}")
    opentextDecr = codeToText(decryptedNums)
    print(f"Decrypted Text = {opentextDecr}")


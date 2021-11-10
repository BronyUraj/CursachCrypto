import Hash
import RSA

if __name__ == "__main__":
    p = 41
    q = 31
    H0 = 7
    openText = "ГУДИМОВ"
    openTextNums = Hash.textToCode(openText)
    print(f"OpenTextNums = {openTextNums}")
    hash = [Hash.hashing(openTextNums, p, q, H0)]
    print(f"H = {hash[0]}")
    e, d, n = RSA.keyGenerator(p, q)
    print(f"Generated keypairs: OpenKey = ({e}, {n}); SecretKey = ({d}, {n})")
    hashEncr = RSA.crypt(hash, d, n)
    print(f"Hash Encrypted = {hashEncr[0]}")
    hashDecr = RSA.crypt(hashEncr, e, n)
    print(f"Hash Decrypted = {hashDecr[0]}")
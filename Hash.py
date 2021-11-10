import Static


def textToCode(text):
    return [Static.__alphabetRus[x] for x in text]


def hashing(text, p, q, H0):
    n = p * q
    H = H0
    for char in text:
        H = (H + char) ** 2 % n
    return H

if __name__ == "__main__":
    openText = "ГУДИМОВ"
    openTextNums = textToCode(openText)
    print(f"openText in Numbers = {openTextNums}")
    H0 = 7
    p = 31
    q = 19
    hash = hashing(openTextNums, p, q, H0)
    print(f"Hash = {hash}")

import Static
from collections import deque


def textToCode(text):
    return ''.join(bin(Static.__alphabetASCII[char])[2:] for char in text)


def sumByModule(bin1, bin2, bits):
    return bin(int(bin1, 2) + int(bin2, 2))[-bits:]


def bitXor(bin1, bin2, padding):
    return bin(int(bin1, 2) ^ int(bin2, 2))[2:].zfill(padding)


def sbox(binstring):
    binblocks = []
    result = ""
    for i in range(0, len(binstring), 4):
        binblocks.append(binstring[i:i + 4])
    for column in range(0, 8):
        result += bin(Static.__sboxGOST[int(binblocks[column], 2)][column])[2:].zfill(4)
    return result


def shiftBits(bitstring):
    dequeObj = deque(bitstring)
    dequeObj.rotate(-11)
    return ''.join(dequeObj)


if __name__ == "__main__":
    opentext = "ГУДИМОВЮ"
    key = "ОРТОХЛОРБЕНЗИЛИДЕНМАЛОНОДИНИТРИЛ"
    X0 = key[0:4]
    bintext = textToCode(opentext)
    binkey = textToCode(X0)
    print(f"Text in binary = {bintext}")
    print(f"SubKey in binary = {binkey}")
    L0 = bintext[:len(bintext) // 2]
    R0 = bintext[len(bintext) // 2:]
    print(f"L0 = {L0}\nR0 = {R0}")
    f = sumByModule(R0, binkey, 32)
    print(f"Sum mod 32 = {f}")
    f = sbox(f)
    print(f"fsbox = {f}")
    f = shiftBits(f)
    print(f"f(R0, X0) = {f}")
    R1 = bitXor(L0, f, 32)
    print(f"R1 = {R1}")
    L1 = R0
    print(f"Result = {L1 + R1}")
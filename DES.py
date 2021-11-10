import Static


def textToCode(text):
    return ''.join(bin(Static.__alphabetASCII[char])[2:] for char in text)


def initialPermutation(binstring):
    return ''.join(binstring[i] for i in Static.__ip)


def expansion(binstring):
    return ''.join(binstring[i] for i in Static.__expansion_table)


def keyRounder(binkey):
    shorted = ''.join(item for index, item in enumerate(binkey) if (index + 1) % 8 != 0)
    shorted = ''.join(item for index, item in enumerate(shorted) if (index + 1) % 8 != 0)
    shorted = shorted[:len(shorted) - 1]
    return shorted


def bitXor(bin1, bin2, padding):
    return bin(int(bin1, 2) ^ int(bin2, 2))[2:].zfill(padding)


def sbox(binstring):
    binblocks = []
    result = ""
    for i in range(0, len(binstring), 6):
        binblocks.append(binstring[i:i + 6])
    for blocknum in range(0, 8):
        sboxres = Static.__sbox[blocknum][int(binblocks[blocknum][0] + binblocks[blocknum][-1], 2) * 16 + int(
            binblocks[blocknum][1:5], 2)]
        result += bin(sboxres)[2:].zfill(4)
    return result


def P_Permutation(binstring):
    return ''.join(binstring[i] for i in Static.__p)


def final_Permutation(binstring):
    return ''.join(binstring[i] for i in Static.__fp)


if __name__ == "__main__":
    opentext = "ГУДИМОВЮ"
    key = "ЮРЬЕВИЧЮ"
    bintext = textToCode(opentext)
    binkey = textToCode(key)
    print(f"Text in binary = {bintext}")
    ipRes = initialPermutation(bintext)
    print(f"Initial Permutation = {ipRes}")
    L0 = ipRes[:len(bintext) // 2]
    R0 = ipRes[len(bintext) // 2:]
    R = R0
    print(f"L = {L0}\nR = {R}")
    R = expansion(R)
    print(f"Expanded R-block = {R}")
    print(f"Key in binary = {binkey}")
    keyRounded = keyRounder(binkey)
    print(f"48 Bit Key = {keyRounded}")
    R = bitXor(R, keyRounded, 48)
    print(f"Whitening R = {R}")
    R = sbox(R)
    print(f"Sbox Result = {R}")
    R = P_Permutation(R)
    print(f"P Permutation = {R}")
    R = bitXor(R, L0, 32)
    print(f"R1 = {R}")
    L1 = R0
    R1 = R
    result = L1 + R1
    print(f"Concat Result = {result}")
    result = final_Permutation(result)
    print(f"Final Result = {result}")

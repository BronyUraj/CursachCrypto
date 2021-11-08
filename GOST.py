import DESStatic


def textToCode(text):
    return ''.join(bin(DESStatic.__alphabetASCII[char])[2:] for char in text)


if __name__ == "__main__":
    opentext = "ГУДИМОВЮ"
    key = "ОРТОХЛОРБЕНЗИЛИДЕНМАЛОНОДИНИТРИЛ"
    key = key[0:4]
    bintext = textToCode(opentext)
    binkey = textToCode(key)
    print(f"Text in binary = {bintext}")
    print(f"Key in binary = {binkey}")
    L0 = bintext[:len(bintext) // 2]
    R0 = bintext[len(bintext) // 2:]
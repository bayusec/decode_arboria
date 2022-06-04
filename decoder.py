import math
import base64
import zlib

file = "www.txt"
rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')


def deobf(text, key):
    offset = ""
    kk = ""
    key = 26 - key
    output = ""
    inputArr = list(text)

    for ch in inputArr:
        if not ch.isalpha():
            kk = kk + ch
        else:
            offset = ord("A" if ch.isupper() else "a")
            kk = kk + chr(int(math.fmod(((ord(ch) + key) - offset), 26)) + offset)
    return kk


f = open(file, "r")
codigo = index = ""
for i in f:
    if i[0] == "$":
        variables = i.split(";")
        index = int(variables[-2].split(",")[1].split(")")[0])
        codigo = variables[1].split("\"")[1]

desofuscado = str(base64.b64decode(zlib.decompress(base64.b64decode(deobf(codigo, index)[::-1].translate(rot13)))))

fin = False
for x in range(1, 20):
    chunk = desofuscado.split("\\n")
    for i in chunk:
        try:
            if i[0] == "$":
                variables = i.split(";")
                index = int(variables[-2].split(",")[1].split(")")[0])
                codigo = variables[1].split("\"")[1]
        except:
            fin = True
            break
    if fin:
        break
    desofuscado = str(base64.b64decode(zlib.decompress(base64.b64decode(deobf(codigo, index)[::-1].translate(rot13)))))
print(desofuscado)

# INTRODUCTION TO CRYPTOHACK

from binascii import unhexlify
import string
from Crypto.Util.number import *
import Crypto
import base64
list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73,
        73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
for x in list:
    print(chr(x), end="")
list = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95,
        110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 100, 51, 100, 102, 100, 54, 100, 102, 125, 10]

print("\n")
byte = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
print(bytes.fromhex(byte), end="")


print("\n")
print(base64.b64encode(bytes.fromhex(
    "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")))


print("\n")
print((Crypto.Util.number.long_to_bytes(
    11515195063862318899931685488813747395775516287289682636499965282714637259206269)))


print("\n")
label = "label"
for x in label:
    print(chr(ord(x) ^ 13), end="")


print("\n")


def xor_two_str(s1, s2):
    if len(s1) != len(s2):
        raise "XOR EXCEPTION: Strings are not of equal length!"

    return ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a, b in zip(s1, s2))


KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2 = xor_two_str(
    "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", KEY1)
KEY3 = xor_two_str(
    "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", KEY2)
KEY4 = xor_two_str(xor_two_str(KEY1, KEY2), KEY3)
FLAG = xor_two_str(
    "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", KEY4)
print(format(unhexlify(FLAG)))


print("\n")


def single_byte_xor(input, key):
    if len(chr(key)) != 1:
        raise "KEY LENGTH EXCEPTION: In single_byte_xor key must be 1 byte long!"

    output = b''
    for b in input:
        output += bytes([b ^ key])

    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"


hidden = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
hidden = unhexlify(hidden)
results = {}
for i in range(256):
    results[i] = single_byte_xor(hidden, i)
print(format([s for s in results.values() if "crypto" in s]))

print("\n")


def brute(input, key):
    if len(input) != len(key):
        return "Failed!"

    output = b''
    for b1, b2 in zip(input, key):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "Cannot Decode some bytes"


data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
data = unhexlify(data)
key_part = brute(data[:7], "crypto{".encode())
key = (key_part + "y").encode()
key += key * int((len(data) - len(key))/len(key))
key += key[:((len(data) - len(key)) % len(key))]
print(format(brute(data, key)))

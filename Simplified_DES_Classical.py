#!/usr/bin/env python
# coding: utf-8

"""
Copyright (c) 2021 Tatsuya Matsuura

Released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

plaintext = '10101001' #平文 8ビット
key = '0110011010' #鍵 10ビット
ciphertext = '10110010' #暗号文 8ビット
mode = 0 #0なら暗号化 1なら復号化



if mode == 0:
    input = plaintext
elif mode == 1:
    input = ciphertext

p10 = [key[2], key[4], key[1], key[6], key[3], key[9], key[0], key[8], key[7], key[5]]
ls1 = [p10[1], p10[2], p10[3], p10[4], p10[0], p10[6], p10[7], p10[8], p10[9], p10[5]]
k1 = "".join([ls1[5], ls1[2], ls1[6], ls1[3], ls1[7], ls1[4], ls1[9], ls1[8]])
ls2 = [ls1[2], ls1[3], ls1[4], ls1[0], ls1[1], ls1[7], ls1[8], ls1[9], ls1[5], ls1[6]]
k2 = "".join([ls2[5], ls2[2], ls2[6], ls2[3], ls2[7], ls2[4], ls2[9], ls2[8]])

#print(k1)
#print(k2)

ip = [input[1], input[5], input[2], input[0], input[3], input[7], input[4], input[6]]
ep = "".join([ip[7], ip[4], ip[5], ip[6], ip[5], ip[6], ip[7], ip[4]])
if mode == 0:
    epkxor = bin(int(ep, 2) ^ int(k1, 2)).removeprefix('0b').zfill(8)
elif mode == 1:
    epkxor = bin(int(ep, 2) ^ int(k2, 2)).removeprefix('0b').zfill(8)
epl = [int("".join([epkxor[0], epkxor[3]]), 2), int("".join([epkxor[1], epkxor[2]]), 2)]
epr = [int("".join([epkxor[4], epkxor[7]]), 2), int("".join([epkxor[5], epkxor[6]]), 2)]

s0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]

s1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]

s0s1 = "".join([bin(s0[epl[0]][epl[1]]).removeprefix('0b').zfill(2), bin(s1[epr[0]][epr[1]]).removeprefix('0b').zfill(2)])
p4 = "".join([s0s1[1], s0s1[3], s0s1[2], s0s1[0]])
p4xor = bin(int(p4, 2) ^ int("".join([ip[0], ip[1], ip[2], ip[3]]), 2)).removeprefix('0b').zfill(4)
sw = "".join([ip[4], ip[5], ip[6], ip[7]]) + p4xor

#print(ip)
#print(ep)
#print(epkxor)
#print(s0s1)
#print(p4)
#print(p4xor)
#print(sw)

ep = "".join([sw[7], sw[4], sw[5], sw[6], sw[5], sw[6], sw[7], sw[4]])
if mode == 0:
    epkxor = bin(int(ep, 2) ^ int(k2, 2)).removeprefix('0b').zfill(8)
elif mode == 1:
    epkxor = bin(int(ep, 2) ^ int(k1, 2)).removeprefix('0b').zfill(8)
epl = [int("".join([epkxor[0], epkxor[3]]), 2), int("".join([epkxor[1], epkxor[2]]), 2)]
epr = [int("".join([epkxor[4], epkxor[7]]), 2), int("".join([epkxor[5], epkxor[6]]), 2)]

s0s1 = "".join([bin(s0[epl[0]][epl[1]]).removeprefix('0b').zfill(2), bin(s1[epr[0]][epr[1]]).removeprefix('0b').zfill(2)])
p4 = "".join([s0s1[1], s0s1[3], s0s1[2], s0s1[0]])
p4xor = bin(int(p4, 2) ^ int("".join([sw[0], sw[1], sw[2], sw[3]]), 2)).removeprefix('0b').zfill(4)
result = p4xor + "".join([sw[4], sw[5], sw[6], sw[7]])
ipm1 = "".join([result[3], result[0], result[2], result[4], result[6], result[1], result[7], result[5]])

#print(ep)
#print(epkxor)
#print(s0s1)
#print(p4)
#print(p4xor)
#print(result)
print(ipm1)
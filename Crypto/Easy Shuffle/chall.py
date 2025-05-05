#!/usr/bin/python3

from string import hexdigits as hd
from hashlib import md5
from random import shuffle

def gen():
    d1 = list(hd[:-6])
    d2 = list(hd[:-6])
    shuffle(d2)
    x = {}
    for y in range(len(d1)):
        x.update({d1[y] : d2[y]})
    return x

def enc(pt):
    x = gen()
    ct = "".join([x[charz] for charz in pt])
    return ct

flag = "STORM{REDACTED}"
flag = [md5(y.encode()).hexdigest() for y in flag]

shuffled = [enc(f) for f in flag]

open("enc.py","w").write(f"{shuffled = }")

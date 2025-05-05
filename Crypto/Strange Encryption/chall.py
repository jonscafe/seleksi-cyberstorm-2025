#!/usr/bin/env python3

from anon import FLAG
from Crypto.Util.number import *
from random import *
from libnum import s2n

def enc(pt, ps):
    ps.sort()
    for p in ps:
        e = 1<<1
        pt = pow(pt, e, p)
    return pt

def key_gen():
    ps = []
    n = randint(2,2**6)
    for _ in range(n):
        p = getPrime(2048)
        ps.append(p)
    return ps

ps = key_gen()
ct = enc(s2n(FLAG), ps)
print('ps = {}\nct = {}'.format(ps, ct))
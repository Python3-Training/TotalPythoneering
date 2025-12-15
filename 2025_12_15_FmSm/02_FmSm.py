#!/usr/bin/env python3
'''
Mission:
Deminstrate basic power-ups.

Authon: Randall Nagy
Rev: 2025/12/15, 1.o
File: 02_FmSm.py
Video: https://youtube.com/shorts/2amN2KmAdko
Project: https://github.com/Python3-Training/TotalPythoneering
Status: Testing Success
'''

def create(*args, **kwargs):
    ...

def move(*args, **kwargs):
    ...

def use(*args, **kwargs):
    ...

def done(*args, **kwargs):
    ...

def my_help(*args, **kwargs):
    ...

ops = {
    '[C]reate': create,
    '[M]ove':   move,
    '[U]se':    use,
    '[D]one':   quit, # built in!
    '[H]elp':   my_help
    }

while True: # loop forever!
    for key in ops:
        print(key)
    op = input("? ").strip()
    if len(op) == 1:
        for k in ops:
            if k[1] == op.upper():
                print(f'!{k}({ops[k]()})')
                break
    else:
        print("Nope.")



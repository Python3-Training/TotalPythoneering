#!/usr/bin/env python3
'''
Mission:
Codify basic requirement mappings.

Authon: Randall Nagy
Rev: 2025/12/15, 1.o
File: 01_FmSm.py
Video: https://youtube.com/shorts/2amN2KmAdko
Project: https://github.com/Python3-Training/TotalPythoneering
Status: Testing Success
'''

def create():
    ...


def move():
    ...


def use():
    ...


def done():
    ...


def my_help():
    ...


ops = {
    '[C]reate': create,
    '[M]ove':   move,
    '[U]se':    use,
    '[D]one':   my_help,
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



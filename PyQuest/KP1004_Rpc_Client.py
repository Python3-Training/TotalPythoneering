#!/usr/bin/env python3
'''
Mission:
Integrate the AI effort into our solution so as to test
the superset. Be sure to run KP1004_rpc_server.py before
running this file (KP1004_rpc_client.py).

Authon: Randall Nagy
Rev: 2025/12/06, 1.o
File: KP1004_rpc_client.py
Video: https://youtube.com/shorts/NJMR5nsYG_0
Project: https://github.com/Python3-Training/TotalPythoneering/edit/main/PyQuest/
Status: Testing Success
'''

import xmlrpc.client

def test_case(a:int, b:int)->None:
    '''
    Docstring test automation:    
    >>> test_case(12, 7)
    Addition OK.
    Multiplication OK.
    Area Calculations OK.

    '''
    from KP1004 import calc_area
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        # Call the remote 'add' function
        if proxy.add(a, b) == a + b:
            print('Addition OK.')
        else:
            raise Exception(f"Error: {a} + {b} <> {a+b}?")

        # Call the remote 'multiply' function
        if proxy.multiply(a, b) == a * b:
            print('Multiplication OK.')
        else:
            raise Exception(f"Error: {a} * {b} <> {a*b}?")

        # Call the remote 'calc_area' function
        comp = calc_area(a,b)
        if proxy.calc_area(a, b) == comp:
            print('Area Calculations OK.')
        else:
            raise Exception(f"Error: {a} * {b} <> {comp}?")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

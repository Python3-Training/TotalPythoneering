#!/usr/bin/env python3
'''
Mission:
Demonstrate how "easy things" can become
"professional things" when we decide to
"test things" :^)

Authon: Randall Nagy
Rev: 2025/11/29, 1.o
File: KP1004.py
Video: https://youtube.com/shorts/cKqUwsUOCVo
Project: https://github.com/Python3-Training/TotalPythoneering/edit/main/PyQuest/
Status: Testing Success
'''
def calc_area(l:int, w:int)->int:
    '''
    Docstring test automation:    
    >>> calc_area('123', 'abc')
    
    >>> calc_area(2, 1)
    2
    '''
    try:
        l = int(l);w = int(w)
        return l * w
    except:
        return None # best idea!

if __name__ == "__main__":
    import doctest
    doctest.testmod()



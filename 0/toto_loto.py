#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- tabstop: 4 -*-

"""This is training task for simulation of 6 of 49 lottery"""

from random import randint as rint
from time import perf_counter as pc

MY_BET = 7, 12, 15, 27, 32, 41
def tm_dc(func):
    """Time Measurment decorator"""
    def inner(*args, **kwargs):
        """Decorator wrapp inner routine"""
        btime = pc()
        ret = func(*args, **kwargs)
        etime = pc()
        print(f"Czas symulacji: {round(etime - btime, 3)} sekund(y)")
        return ret
    return inner

def lotery_once():
    """Single drawing"""
    drw = set()
    while len(drw)<6:
        drw.add(rint(1, 49))
    return tuple(sorted(drw))

def accuracy(bet_tup, drawing_tup):
    """Accuraty of single drawing"""
    return sum(n in(bet_tup) for n in drawing_tup)

@tm_dc
def symul():
    """Lotery Symulation"""
    acc = 0
    dict_counts = {}
    for test in range(3, 7):
        dict_counts[test] = 0
    while acc!=6:
        drawing = lotery_once()
        acc = accuracy(MY_BET, drawing)
        for test in range(3, 6):
            if acc==test:
                dict_counts[test] += 1
        dict_counts[6] += 1
    return dict_counts

def str_int(_int):
    """Format big integer"""
    return f"{_int:,d}".replace(',', ' ')

def weeks_to_years(weeks):
    """Calculation of Years from Weeks"""
    days = weeks*7
    years = days//365
    str_out = ''
    if years:
        str_out += f"{str_int(years)} lat" if years>1 else 'rok'
    rest_wks = days%365
    if years and rest_wks:
        str_out += ' i '
    if rest_wks:
        str_out += f"{str_int(rest_wks)} tygodni" if rest_wks>1 else ' tygodnia'
    return str_out

def main():
    """Main Routine"""
    score = symul()
    print("Wylosowanie dokładnie założonych liczb:"
        f" {', '.join(str(d) for d in MY_BET)} zajęło {str_int(score[6])} prób.")
    print("Przy założeniu 3 PLN za zakład, całkowicie wydane pieniądze"
        f": {str_int(score[6]*3)} PLN")
    print(f"Przy 1 zakładzie na tydzień, wygrana zajmie {weeks_to_years(score[6])}")
    for test in range(3, 6):
        print(f"W trakcie całej operacji wypadło {score[test]:d} razy {test:d}")

if __name__=="__main__":
    main()

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-
# -*- tabstop: 4 -*-

from random import sample as spl
from toto_loto import lotery_once, accuracy, weeks_to_years, str_int

def test_lotery_once():
    for idx in range(500):
        drawing = lotery_once()
        assert len(drawing)==len(set(drawing))==6
        assert min(drawing)>0
        assert max(drawing)<50

ez_tup6 = lambda b: tuple(spl(range(b, b+6), 6))

def test_accuracy():
    t1 = ez_tup6(1)
    for idx in range(6):
        t2 = ez_tup6(6-idx)
        accu = accuracy(t1, t2)
        assert accu==1+idx

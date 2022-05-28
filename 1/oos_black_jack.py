#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

COLORS = '♥R', '♠B', '♦R', '♣B'
VALUES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

from random import shuffle as rnd_shf

class Card:
    def __init__(self, color, value, position, owner):
        self.color, self.value = color, value
        self.position = position
        self.owner = owner

    def __repr__(self):
        return f"{self.value}/{self.color}/{self.owner}/{self.position}"

class Deck:
    def __init__(self):
        self.cards = []
        idx = 0
        for idc, color in enumerate(COLORS):
            for idv, value in enumerate(VALUES):
                self.cards.append(Card(color, value, idx, 'Deck'))
                idx += 1

    def positions(self):
        return [card.position for card in self.cards]

    def shuffle(self):
        rnd_shf(self.cards)





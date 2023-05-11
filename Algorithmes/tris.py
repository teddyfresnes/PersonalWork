#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def alea(n):
    l = []
    for i in range(n):
        l.append(random.randint(0,100))
    return l
liste = alea(100)

def tri_insertion(tab):
    for i in range(1,len(tab)):
        x = tab[i]
        j = i
        while j > 0 and tab[j-1] > x:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = x
    return tab


def tri_selection(tab):
    for i in range(len(tab)-1):
        min=i
        for j in range(i+1,len(tab)):
            if tab[j] < tab[min]:
                min = j
    if min != i:
        tab[i], tab[min] = tab[min], tab[i]
    return tab



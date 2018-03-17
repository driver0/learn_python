#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def product(*args):
    pt = 1
    for n in args:
        pt = pt*n
    return pt

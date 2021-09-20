#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 7


if __name__ == "__main__":
    U = set("abcdefghijklmnopqrstuvwxyz")
    A = {'b', 'f', 'g', 'm', 'o'}
    B = {'b', 'g', 'h', 'l', 'u'}
    C = {'e', 'f', 'm'}
    D = {'e', 'g', 'l', 'p', 'q', 'u', 'v'}

    X = (A.intersection(C)).union(B)
    print(f'X= {X}')

    BB = U.difference(B)

    Y = (A.intersection(BB)).union(C.difference(D))
    print(f'Y = {Y}')

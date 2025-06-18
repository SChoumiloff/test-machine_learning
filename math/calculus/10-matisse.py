#!/usr/bin/env python3
"""
Derive me plz
"""


def poly_derivative(poly):
    """Derive me plz
    """
    if not poly:
        return None
    if len(poly) == 0:
        return 0
    poly_new = []
    for i in range(1, len(poly)):
        poly_new.append(poly[i] * i)
    return poly_new

#!/usr/bin/env python3
"""
Derive me plz
"""


def poly_derivative(poly):
    """Derive me plz
    """
    if not poly or len(poly) == 0:
        return None
    poly_new = []
    for i in range(1, len(poly)):
        poly_new.append(poly[i] * i)
    return poly_new

#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Vivian Sedov
#
# File Name: solution_1.py
__author__ = "Vivian Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


def isValidSubsequence(array: List[int], sequence: int) -> bool:
    """
    >>> isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])

    """

    filtered = []

    for i in range(len(array)):
        if len(filtered) == len(sequence):
            break

        if array[i] in sequence:
            filtered.append(array[i])

    return filtered == sequence


def main() -> None:
    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()

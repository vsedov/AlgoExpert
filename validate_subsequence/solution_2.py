#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Vivian Sedov
#
# File Name: solution_2.py
__author__ = "Vivian Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


def isValidSubsequence(array: List[int], sequence: int) -> bool:

    # another method to deal with the validate subsequence .

    for item in array:

        if item == sequence[0]:
            sequence.pop(0)

        if len(sequence) == 0:
            return True

    return False


def main() -> None:
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))


if __name__ == "__main__":
    pi.install_traceback()
    main()

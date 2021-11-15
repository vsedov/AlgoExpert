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


def twoNumberSum(array: List[int], target_sum: int) -> List[int]:
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target_sum:
                return [array[i], array[j]]
    return []


def main() -> None:
    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()

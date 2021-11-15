#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Vivian Sedov
#
# File Name: solution_3.py
__author__ = "Vivian Sedov"
__email__ = "viv.sv@hotmail.com"

from typing import List

import pyinspect as pi


def twoNumberSum(array: List[int], target: int) -> List[int]:
    # without hash

    array.sort()

    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target:
            return [array[left], array[right]]

        elif current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1

    return []


def main() -> None:
    pass


if __name__ == "__main__":
    pi.install_traceback()
    main()

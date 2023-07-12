#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © Vivian Sedov
#
# File Name: solution_2.py
__author__ = "Vivian Sedov"
__email__ = "viv.sv@hotmail.com"


import pyinspect as pi


def twoNumberSum(array, targetSum):
    # Write your code here.
    container = {}
    for val in array:
        target = targetSum - val

        if target in container:
            return [target, val]

        else:
            container[val] = True

    return []


def main() -> None:
    twoNumberSum(list(range(10)), 5)


if __name__ == "__main__":
    pi.install_traceback()
    main()

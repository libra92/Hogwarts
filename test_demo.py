#!/usr/local/bin python3
# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 20:35
# @Author  : linka
# @FileName: test_demo.py
# @Software: PyCharm

import pytest


# class Test_demo():

#    def test_one(self):
#        a = 5
#        b = 1
#        assert a!=b
#        print("这是我的第一个测试用例")


def add_function(a, b):
    return a+b


@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8), (-1, -2, -3), (100, 100, 200)
], ids=["int", "minus", "bigint"])
def test_add(a, b, expected):
    assert add_function(1, 2) == 3
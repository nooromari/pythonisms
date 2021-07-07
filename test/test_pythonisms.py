from pythonisms.pythonisms import *
import pytest


def test_eq(test):
    list1 , list2 = test
    actual = linked == linked2
    expected = True
    assert actual == expected
def test_iter(test):
    list1 , list2 = test
    actual = [x for x in list1]
    expected = [4,3,2,1]
    assert actual == expected



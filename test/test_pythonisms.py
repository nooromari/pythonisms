from pythonisms.pythonisms import *
import pytest


def test_eq(list1, list2):
    actual = list1 == list2
    expected = True
    assert actual == expected

def test_iter(list1):
    actual = [x for x in list1]
    expected = ['D', 'C', 'B', 'A']
    assert actual == expected


@pytest.fixture
def list1():
    linked = LinkedList()
    linked.insert('A')
    linked.insert('B')
    linked.insert('C')
    linked.insert('D')
    return linked

@pytest.fixture
def list2():
    linked = LinkedList()
    linked.insert('A')
    linked.insert('B')
    linked.insert('C')
    linked.insert('D')
    return linked
import pytest #type: ignore
from src.stack.stack import Stack


def test_str():
    a = Stack()
    a.data = [1, 2, 3]
    assert str(a) == "1 2 3"

def test_push():
    a = Stack()
    a.push(1)
    a.push(2)
    a.push(3)
    assert a.data == [1, 2, 3]

def test_pop():
    a = Stack()
    a.push(1)
    a.push(2)
    assert a.pop() == 2
    assert a.data == [1]
    assert a.pop() == 1
    with pytest.raises(IndexError):
        a.pop()

def test_peek():
    a = Stack()
    with pytest.raises(IndexError):
        a.peek()
    a.push(1)
    assert a.peek() == 1
    a.push(2)
    assert a.peek() == 2
    assert a.data == [1, 2]

def test_is_empty():
    a = Stack()
    assert a.is_empty()
    a.push(1)
    assert not a.is_empty()

def test_len():
    a = Stack()
    assert len(a) == 0
    a.push(1)
    assert len(a) == 1
    a.push(1)
    assert len(a) == 2

def test_min():
    a = Stack()
    with pytest.raises(IndexError):
        a.min()
    a.push(4)
    assert a.min() == 4
    a.push(1)
    assert a.min() == 1
    a.push(2)
    assert a.min() == 1
    a.push(0)
    assert a.min() == 0
    a.pop()
    a.pop()
    a.pop()
    assert a.min() == 4

def test_max():
    a = Stack()
    with pytest.raises(IndexError):
        a.max()
    a.push(1)
    assert a.max() == 1
    a.push(2)
    assert a.max() == 2
    a.push(1)
    assert a.max() == 2
    a.push(10)
    assert a.max() == 10
    a.pop()
    a.pop()
    a.pop()
    assert a.max() == 1

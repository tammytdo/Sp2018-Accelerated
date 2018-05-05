#!/usr/bin/env python

"""
tests for monkey trouble
"""
from monkey import monkey_trouble


def test_tt():
    assert monkey_trouble(True, True)


def test_ff():
    assert monkey_trouble(False, False)


def test_tf():
    assert not monkey_trouble(True, False)


def test_ft():
    assert not monkey_trouble(False, True)


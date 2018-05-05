#!/usr/bin/env python

"""
test code for kwargs assignment
"""
import pytest

from kwargs_lab import colors


def test_one():
    result = colors()
    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'link: green' in result
    assert 'visited: cyan' in result


def test_pos():
    result = colors('red', 'blue', 'yellow', 'chartreuse')
    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'link: yellow' in result
    assert 'visited: chartreuse' in result


def test_key():
    result = colors(link_color="magenta")
    print(result)
    assert 'foreground: red' in result
    assert 'background: blue' in result
    assert 'link: magenta' in result
    assert 'visited: cyan' in result


def test_pos_key():
    result = colors('purple', link_color="magenta")
    print(result)
    assert 'foreground: purple' in result
    assert 'background: blue' in result
    assert 'link: magenta' in result
    assert 'visited: cyan' in result


def test_pos_key_duplicate():
    with pytest.raises(TypeError):
        result = colors('purple', fore_color="magenta")
        print(result)


sample = ('blue', 'purple')


def test_tuple():
    result = colors(*sample)
    print(result)
    assert 'foreground: blue' in result
    assert 'background: purple' in result
    assert 'link: green' in result
    assert 'visited: cyan' in result


def test_tuple2():
    result = colors('green', *sample)
    print(result)
    assert 'foreground: green' in result
    assert 'background: blue' in result
    assert 'link: purple' in result
    assert 'visited: cyan' in result


sampled = {"fore_color":"magenta",
           "link_color":"purple"}


def test_dict():
    result = colors(**sampled)
    print(result)
    assert 'foreground: magenta' in result
    assert 'background: blue' in result
    assert 'link: purple' in result
    assert 'visited: cyan' in result

sampled2 = {"visited_color":"magenta",
           "link_color":"purple"}


def test_tuple_dict():
    result = colors(*sample, **sampled2)
    print(result)
    assert 'foreground: blue' in result
    assert 'background: purple' in result
    assert 'link: purple' in result
    assert 'visited: magenta' in result


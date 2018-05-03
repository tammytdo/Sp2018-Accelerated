#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"
    
    def __init__(self, content=None):
        self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        tag = self.tag
        out_file.write("just something as a place holder...")

class P:
    tag = "p"
    cur_ind = "    "
    
class BODY:
    tag = "body"
    cur_ind = "    "
    
class TITLE:
    tag = "title"
    cur_ind = "    "

class HEAD:
    tag = "head"
    cur_ind = "    "
    

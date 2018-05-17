#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def render(self, out_file):
        outfile.write(f"<{self.tag}>\n")
        for line in self.content:
            if isinstance(line, str):
                outfile.write(line)
                outfile.write("\n")
            else:
                line.render(out_file)
        outfile.write(f"</{self.tag}>\n")


class P(Element):
    tag = "P"


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class Head(Element):
    tag = "head"


class OneLineTag(Element):
    pass

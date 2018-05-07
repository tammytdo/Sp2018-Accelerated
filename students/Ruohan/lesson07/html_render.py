#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = 'html'
    def __init__(self, content=None, style="line-height:200%"):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.style = style

    def append(self, new_content):
        self.content.append(new_content)

    def one_tag(self):
        return f'<{self.tag}>'

    def render(self, out_file):
        out_file.write(self.one_tag() + '\n')
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
                out_file.write('\n')
            else:
                line.render(out_file)
        out_file.write(f'</{self.tag}>\n')


class style(Element):
    def one_tag(self):
        return f"<{self.tag} style='{self.style}'>"

class P(style):
    tag = 'p'


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'

class Head(Element):
    tag = 'head'


class Onelinetag(Element):
    def render(self, out_file):
        out_file.write(self.one_tag())
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
            else:
                line.render(out_file)
        out_file.write(f'</{self.tag}>\n')


class Title(Onelinetag):
    tag = 'title'


class Selftag(Element):
    def __init__(self, style="line-height:200%"):
        self.style = style
    def render(self, out_file):
        out_file.write(f'<{self.tag} />\n')


class Hr(Selftag):
    tag = 'hr'

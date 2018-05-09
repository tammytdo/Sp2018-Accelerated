#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = 'html'
    ind_count = 0
    def __init__(self, content=None, **kwargs):
        if content:
            self.content = [content]
        else:
            self.content = []
        if kwargs:
            self.atts = kwargs
        else:
            self.atts = {}


    def att_output(self):
        att_output = []
        for k, v in self.atts.items():
            att_output.append(f'{k}="{v}"')
        return ' '.join(att_output)

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        if self.att_output():
            return f'<{self.tag} {self.att_output()}>'
        else:
            return f'<{self.tag}>'

    def render(self, out_file):
        out_file.write(self.open_tag() + '\n')
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
                out_file.write('\n')
            else:
                line.render(out_file)
        out_file.write(f'</{self.tag}>\n')


class P(Element):
    tag = 'p'


class Html(Element):
    tag = 'html'
    def open_tag(self):
       return f'<!DOCTYPE {self.tag}>\n<{self.tag}>'


class Body(Element):
    tag = 'body'

class Head(Element):
    tag = 'head'


class Onelinetag(Element):
    def render(self, out_file):
        out_file.write(self.open_tag())
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
            else:
                line.render(out_file)
        out_file.write(f'</{self.tag}>\n')


class Title(Onelinetag):
    tag = 'title'


class Selftag(Element):
    def __init__(self, **kwargs):
        if kwargs:
            self.atts = kwargs
        else:
            self.atts = {}
    def render(self, out_file):
        if self.atts:
            out_file.write(f'<{self.tag} {self.att_output()} />\n')
        else:
            out_file.write(f'<{self.tag} />\n')


class Hr(Selftag):
    tag = 'hr'


class Br(Selftag):
    tag = 'br'


class A(Onelinetag):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href = link )


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class H(Onelinetag):
    def __init__(self, num, content):
        self.tag = f'h{num}'
        super().__init__(content)


class Meta(Selftag):
    tag = 'meta'

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content=None, **kwargs):

        if content is None:
            self.content = []
        else:
            self.content = [content]
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = None

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        if self.attributes:
            tag = f'{self.tag} '
            for attr, text in self.attributes.items():
                tag += attr + '="'  + text + '" '
            return f'<{tag}>'
        else:
            return f'<{self.tag}>'

    def render(self, out_file):
        """
            <html>
            this is some text
            and this is some more text
            </html>
    """
        out_file.write(self.open_tag() + "\n")
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
                out_file.write("\n")
            else:
                line.render(out_file)
        out_file.write("</{}>\n".format(self.tag))


class P(Element):
    tag = "p"


class Html(Element):
    tag = 'html'
    out_file.write(f'<!DOCTYPE html>\n')

class Body(Element):
    tag = 'body'

class Head(Element):
    tag = "head"

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(self.open_tag())
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
            else:
                line.render(out_file)
        out_file.write("</{}>\n".format(self.tag))

class Title(OneLineTag):
    tag = "title"

class SelfClosingTag(Element):

    tag = 'hr'

    def __init__(self, content=None, **kwargs):

        if content is not None:
            raise ValueError('no content in self closing tag')
        if kwargs:
            self.attributes = kwargs
        else:
            self.attributes = None

    def render(self, out_file):

        if self.attributes:
            tag = f'{self.tag} '
            for attr, text in self.attributes.items():
                tag += attr + '="'  + text + '" '
            out_file.write(f'<{tag} />\n')
        else:
            out_file.write(f'<{self.tag} />\n')
class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'
    def __init__(self, link, content):
        super().__init__(content, href=link)

class H(OneLineTag):
    tag = 'h'
    def __init__(self, integer, content):
        self.tag = f'h{integer}'
        super().__init__(content)

class Ul(Element):
    tag = 'ul'

class Li(Element):
tag = 'li'

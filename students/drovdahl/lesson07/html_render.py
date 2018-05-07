#!/usr/bin/env python3

"""
A class-based system for rendering html.
Ryan Drovdahl's version
"""


# This is the framework for the base class
class Element(object):

    # 'html' is the default tag that is only used for testing
    tag = 'html'
    close_tag_line = True
    link_tag = False
    meta_tag = False

    def __init__(self, content=None, style=None, id=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.style = style
        self.id = id

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        if self.id and self.style:
            return f'<{self.tag} id="{self.id}" style="{self.style}">'
        elif self.style:
            return f'<{self.tag} style="{self.style}">'
        else:
            return f'<{self.tag}>'

    def close_tag(self):
        return f'</{self.tag}>'

    def render(self, out_file, ind=None):
        '''<tag>
           this is some text
           and this is some more text
           </tag>
        '''
        out_file.write(self.open_tag() + '\n')
        self.style = None
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
                out_file.write('\n')
            else:
                line.render(out_file)
        if self.close_tag_line is True:
            out_file.write(self.close_tag() + '\n')
        else:
            pass


class Html(Element):
    tag = 'html'

    def open_tag(self):
        return f'<!DOCTYPE {self.tag}>\n<{self.tag}>'


class Body(Element):
    tag = 'body'


class P(Element):
    tag = 'p'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):
    '''<tag>this is some text and this is some more text</tag>'''
    def render(self, out_file):
        if self.link_tag is True:
            out_file.write(f'<{self.tag} href="{self.link}">{self.content}'
                           f'{self.close_tag()}\n')
        elif self.meta_tag is True:
            out_file.write(f'<{self.tag} charset="{self.charset}" />\n')
        else:
            out_file.write(self.open_tag())
            for line in self.content:
                if isinstance(line, str):
                    out_file.write(line)
                else:
                    line.render(out_file)
            if self.close_tag_line is True:
                out_file.write(self.close_tag() + '\n')
            else:
                pass


class Title(OneLineTag):
    tag = 'title'


class Hr(Element):
    tag = 'hr /'
    close_tag_line = False


class Br(Element):
    tag = 'br /'
    close_tag_line = False


class A(OneLineTag):
    tag = 'a'
    link_tag = True

    def __init__(self, link, content, style=None):
        self.link = link
        self.content = content
        self.style = style


class Ul(Element):
    tag = 'ul'

    def __init__(self, id=None, content=None, style=None):
        self.id = id
        self.style = style
        if content is None:
            self.content = []
        else:
            self.content = [content]


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, header_level, content, id=None, style=None):
        self.content = content
        self.style = style
        tag = 'h' + str(header_level)
        self.tag = tag
        self.id = id


class Meta(OneLineTag):
    tag = 'meta'
    meta_tag = True

    def __init__(self, charset=None, id=None, style=None, content=None):
        self.charset = charset
        self.id = id
        self.style = style
        if content is None:
            self.content = []
        else:
            self.content = [content]

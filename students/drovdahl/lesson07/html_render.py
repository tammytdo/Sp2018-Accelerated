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

    def __init__(self, content=None, style=None, id=None, indent=4):
        if content is None:
            self.content = []
        else:
            self.content = [content]
        self.style = style
        self.id = id
        self.indent = indent

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

    def render(self, out_file, cur_indent=None):
        '''<tag>
           this is some text
           and this is some more text
           </tag>
        '''
        if cur_indent is not None:
            render_indent = ' ' * self.indent * cur_indent
        else:
            render_indent = ''
        out_file.write(str(render_indent) + self.open_tag() + '\n')
        self.style = None
        for line in self.content:
            if isinstance(line, str):
                out_file.write(str(render_indent + '    ') + line)
                out_file.write('\n')
            else:
                if cur_indent is None:
                    cur_indent = 1
                else:
                    cur_indent += 1
                line.render(out_file, cur_indent)
                cur_indent -= 1
        if self.close_tag_line is True:
            out_file.write(str(render_indent) + self.close_tag() + '\n')
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

    def render(self, out_file, cur_indent=None):
        if cur_indent is not None:
            render_indent = ' ' * self.indent * cur_indent
        else:
            render_indent = ''

        if self.link_tag is True:
            out_file.write(str(render_indent) + f'<{self.tag} href="{self.link}">{self.content}'
                           f'{self.close_tag()}\n')
        elif self.meta_tag is True:
            out_file.write(str(render_indent) + f'<{self.tag} charset="{self.charset}" />\n')
        else:

            out_file.write(str(render_indent) + self.open_tag())
            for line in self.content:
                if isinstance(line, str):
                    out_file.write(line)
                else:
                    line.render(out_file, cur_indent)
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

    def __init__(self, link, content=None, style=None, indent=4):
        self.link = link
        self.style = style
        self.indent = indent
        if content is None:
            self.content = []
        else:
            self.content = [content]


class Ul(Element):
    tag = 'ul'

    def __init__(self, content=None, id=None, style=None, indent=4):
        self.id = id
        self.style = style
        self.indent = indent
        if content is None:
            self.content = []
        else:
            self.content = [content]


class Li(Element):
    tag = 'li'


class H(OneLineTag):

    def __init__(self, header_level, content, id=None, style=None, indent=4):
        self.content = "".join(content)
        self.style = style
        tag = 'h' + str(header_level)
        self.tag = tag
        self.id = id
        self.indent = indent


class Meta(OneLineTag):
    tag = 'meta'
    meta_tag = True

    def __init__(self, charset=None, id=None, style=None, content=None, indent=4):
        self.charset = charset
        self.id = id
        self.style = style
        self.indent = indent
        if content is None:
            self.content = []
        else:
            self.content = [content]

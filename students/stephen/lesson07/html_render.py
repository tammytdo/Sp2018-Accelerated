#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = 'html'

    ind_count = 0

    def __init__(self, *args, **kwargs): # Initializer
        self.content = list(args)
        attributes = []
        for keyword in kwargs:
            attributes.append(f' {keyword}="' + kwargs[keyword] + '"')
        self.attributes = ''.join(attributes)

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        return f'<{self.tag}{self.attributes}>'

    def render(self, out_file, ind="    "):
        """
        This should render something like this:
        <html>
        this is some text
        and this is some more text
        </html>
        """
        # self.ind_count += 1
        out_file.write((ind * self.ind_count) + self.open_tag() + '\n')
        # print(self.content)
        self.ind_count += 1
        for line in self.content:
            if isinstance(line, str):     
                out_file.write((ind * self.ind_count) + line)
                out_file.write('\n')
            else:
                # print("in else block")
                # print(line)
                line.render(out_file)
        self.ind_count -= 1
        out_file.write((ind * self.ind_count) + '</{}>\n'.format(self.tag))
        # self.ind_count -= 1

class Html(Element):
    tag = 'html'

    def render(self, out_file):
        out_file.write('<!DOCTYPE html>\n')
        Element.render(self, out_file)

class Head(Element):
    tag = 'head'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class OneLineTag(Element):

    def render(self, out_file, ind="    "):
        self.ind_count += 1
        out_file.write((ind * self.ind_count) + self.open_tag())
        for line in self.content:
            if isinstance(line, str):     
                out_file.write(line)
            else:
                # print('in else block')
                # print(line)
                self.ind_count += 1
                line.render(out_file)
                self.ind_count -= 1
        out_file.write('</{}>\n'.format(self.tag))
        self.ind_count -= 1

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    
    def __init__(self, **kwargs): # Initializer
        attributes = []
        for keyword in kwargs:
            attributes.append(f' {keyword}="' + kwargs[keyword] + '"')
        self.attributes = ''.join(attributes)

    def open_tag(self):
        return f'<{self.tag}{self.attributes} />'
    
    def render(self, out_file):
        out_file.write(self.open_tag() + '\n')

class Hr(SelfClosingTag):
    tag = 'hr'

    # def check_self(self):
    #     print('Am I a subclass of SelfClosingTag: ', issubclass(self.__class__, SelfClosingTag))

class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):
    tag = 'a'

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        Element.__init__(self, *args, **kwargs)

class Ul(Element):
    tag = 'ul'

class Li(Element):
    tag = 'li'

class H(OneLineTag):
    tag = 'H'

    def __init__(self, num, *args, **kwargs):
        self.tag = f'{self.tag}{num}'
        Element.__init__(self, *args, **kwargs)

class Meta(SelfClosingTag):
    tag = 'meta'




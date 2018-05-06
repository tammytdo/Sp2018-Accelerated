#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = 'html'

    def __init__(self, *args, **kwargs): # Initializer
        # if content is None:
        #     self.content = []
        # else:
        #     self.content = [content] # self is the instance of the class
        self.content = list(args)
        attributes = []
        for keyword in kwargs:
            attributes.append(f' {keyword}="' + kwargs[keyword] + '"')
        self.attributes = ''.join(attributes)

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        return f'<{self.tag}{self.attributes}>'

    def render(self, out_file):
        """
        This should render something like this:
        <html>
        this is some text
        and this is some more text
        </html>
        """
        out_file.write(self.open_tag() + '\n')
        # print(self.content)
        for line in self.content:
            if isinstance(line, str):     
                out_file.write(line)
                out_file.write('\n')
            else:
                # print("in else block")
                # print(line)
                line.render(out_file)
        out_file.write('</{}>\n'.format(self.tag))

class Html(Element):
    tag = 'html'

class Head(Element):
    tag = 'head'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(self.open_tag())
        for line in self.content:
            if isinstance(line, str):     
                out_file.write(line)
            else:
                # print('in else block')
                # print(line)
                line.render(out_file)
        out_file.write('</{}>\n'.format(self.tag))

class Title(OneLineTag):
    tag = 'title'



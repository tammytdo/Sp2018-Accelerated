#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = 'html'

    def __init__(self, content=None): # Initializer
        if content is None:
            self.content = []
        else:
            self.content = [content] # self is the instance of the class

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        return f'<{self.tag}>'

    def render(self, out_file):
        """
        This should render something like this:
        <html>
        this is some text
        and this is some more text
        </html>
        """
        out_file.write(open_tag() + '\n')
        print(self.content)
        for line in self.content:
            if isinstance(line, str):     
                out_file.write(line)
                out_file.write('\n')
            else:
                print("in else block")
                print(line)
                line.render(out_file)
        out_file.write('</{}>\n'.format(self.tag))

class P(Element):
    tag = 'p'

class Html(Element):
    tag = 'html'

class Body(Element):
    tag = 'body'

class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(f'<{self.tag}>')
        for line in self.content:
            if isinstance(line, str):     
                out_file.write(line)
            else:
                print("in else block")
                print(line)
                line.render(out_file)
        out_file.write('</{}>\n'.format(self.tag))



class Title(OneLineTag):
    tag = 'title'



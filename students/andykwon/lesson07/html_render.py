#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element():

    tag = "html"
    indent = "    "

    def __init__(self, content=None, **kwargs):
        """
        initializing the Element class
        """
        if content is None:
            self.content = []
        else:
            self.content = [content]

        self.attr = kwargs

    def append(self, new_content):
        """
        appending the contents to the class object
        """

        self.content.append(new_content)

    def open_tag(self):

        opening = f"<{self.tag}>"
        if self.attr != {}:
            for key, value in self.attr.items():
                opening += ' {}="{}"'.format(key, value)

        return opening 

    def render(self, out_file, cur_ind=""):

        if cur_ind == "":
            cur_ind = self.indent

        out_file.write(cur_ind + self.open_tag() + "\n")

        for line in self.content:
            if isinstance(line, str):
                out_file.write(cur_ind + self.indent + line)
                out_file.write("\n")
            else:
                line.render(out_file, cur_ind + self.indent)

        out_file.write(cur_ind + "</{}>\n".format(self.tag))


class P(Element):
    tag = "p"


class Html(Element):
    tag = 'html'


class Body(Element):
    tag = 'body'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file, cur_ind=""):

        out_file.write(cur_ind + self.open_tag())

        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)
            else:
                line.render(out_file, cur_ind + self.indent)

        out_file.write("</{}>".format(self.tag) + "\n")


class Title(OneLineTag):
    tag = "title"


class SelfClosingTag(Element):

    def append(self, *args, **kwargs):
        raise TypeError

    def open_tag(self,):

        line = ''
        opening = f"<{self.tag}"

        if self.attr != {}:
            for key, value in self.attr.items():
                line += ' {}="{}"'.format(key, value)

        return opening + line

    def render(self, out_file, cur_ind=""):
        out_file.write(cur_ind + self.open_tag() + " /> \n")


class Hr(SelfClosingTag):
    tag = 'hr'


class Br(SelfClosingTag):
    tag = 'br'

class A(OneLineTag):

    tag = "a"

    def __init__(self, link, content=None, **kwargs):
        kwargs['href'] = link
        # Element.__init__(self, content, **kwargs)
        super().__init__(content, **kwargs)

class Ul(Element):
    tag = "ul"

class Li(Element):
    tag = "li"

class H(OneLineTag):
    tag = "h"

    def __init__(self, number, content, **kwargs):
        self.tag = "h" + str(number)
        # Element.__init__(self, content, **kwargs)
        super().__init__(content, **kwargs)

class Meta(SelfClosingTag):
    tag = "meta"














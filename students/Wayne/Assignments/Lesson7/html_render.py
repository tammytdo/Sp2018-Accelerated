#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:

    tag = "html"

    def __init__(self, content, **kwargs):
        lst = []
        for k in kwargs:
            lst.append('{}= "{}"'.format(k, kwargs[k]))
        self.atr = ' '.join(lst)

        if content is None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        return f"<{self.tag} {self.atr}>"

    def render(self, out_file):
        out_file.write(self.open_tag() + "\n")
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)  # passes in a the class to render
                out_file.write("\n")
            else:
                line.render(out_file)
        out_file.write("</{}>\n".format(self.tag))


"""
Class P inherits the functionality from Element
"""


class P(Element):
    tag = "p"


class Html(Element):
    tag = "html"


class Body(Element):
    tag = "body"


class Head(Element):
    tag = "Head"


class OneLineTag(Element):

    def render(self, out_file):
        out_file.write(self.open_tag())
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)  # passes in a the class to render
            else:
                line.render(out_file)
        out_file.write("</{}>\n".format(self.tag))


class Title(OneLineTag):
    tag = "Title"

#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:
    tag = "html"

    def __init__(self, content=None):

        if content is not None:
            self.content = []
        else:
            self.content = [content]

    def append(self, new_content):
        self.content.append(new_content)

    def open_Tag(self):
        return f"<{self.tag}>"

    def render(self, out_file):
        out_file.write(f"<{self.tag}>\n")
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)  # passes in a the class to render
                out_file.write("\n")
            else:
                line.render(out_file)
        out_file.write("</{}>\n".format(self.tag))

    def onelinerender(self, out_file):
        out_file.write(f"<{self.tag}>")
        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)  # passes in a the class to render
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

#class Title(OneLineTag):
#    tag = "Title"

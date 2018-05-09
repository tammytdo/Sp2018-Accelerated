#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element:  # Step 1

    tag = "html"

    def __init__(self, *args, **kwargs):
        lst = []
        for k in kwargs:  # Step 4
            lst.append('{}= "{}"'.format(k, kwargs[k]))
        self.atr = ' '.join(lst)

        if args is None:
            self.content = []
        else:
            self.content = list(args)

    def append(self, new_content):
        self.content.append(new_content)

    def open_tag(self):
        return f"<{self.tag} {self.atr}>"

    def close_tag(self):
        return f"<{self.tag}>"

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


class P(Element):  # Step 2
    tag = "p"


class Html(Element):  # Step 2
    tag = "html"


class Body(Element):  # Step 2
    tag = "body"


class Head(Element):  # Step 2
    tag = "Head"


class OneLineTag(Element):  # Step 3

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


class SelfClosingTag(Element):  # step 5

    def render(self, out_file):

        for line in self.content:
            if isinstance(line, str):
                out_file.write(line)  # passes in a the class to render
            else:
                line.render(out_file)
        out_file.write(self.close_tag().replace(">", "/> \n"))


class Br(SelfClosingTag):  # step 5
    tag = "br"


class Hr(SelfClosingTag):  # step 5
    tag = "hr"


class A(OneLineTag):  # step 6 pushes creates anchor

    tag = "a"

    def __init__(self, link, *args, **kwargs):
        kwargs['href'] = link
        Element.__init__(self, *args, **kwargs)


class Ul(Element):

    tag = "ul"


class Li(Element):

    tag = "li"


class H(OneLineTag):

    tag = "H"

    def __init__(self, headerlevel, *args, **kwargs):
        kwargs = headerlevel
        self.open_tag = "h" + str(int(self.headerlever))
        Element.__init__(self, *args, **kwargs)

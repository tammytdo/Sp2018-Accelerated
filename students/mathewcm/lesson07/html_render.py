#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class
class Element():

    tag = "html"
    ind = 0

    def __init__(self, content=None, **kwargs):
        if content is None:
            self.content = []
        if content != None:
            self.content = [content]
        if kwargs:
            self.attrs = kwargs
        else:
            self.attrs = None

    def append(self, new_content):
        self.content.append(new_content)
    
    def add_newlines(self):
        '''Loop thru self.content and insert newlines if obj in next index is 
        not a string OR if last object in index is a string'''
        if any(isinstance(line, str) for line in self.content):
            content_copy = self.content[:]
            for i in range(len(content_copy)-1):
                next_index = i + 1
                if isinstance(content_copy[i], object) and not isinstance(content_copy[i], str):
                    pass
                elif not isinstance(content_copy[next_index], str):
                    self.content.insert(next_index, '\n')
        if isinstance(self.content[-1], str):
            self.content.append('\n')

    def open_tag(self):
        return f"<{self.tag}>"

    def render(self, out_file, **kwargs):
        '''Render into html with appropriate indentation and newlines'''
        self.add_newlines()
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.ind
        if self.attrs:
            attr_string = ''
            for key, value in self.attrs.items():
                attr_string += str("{}='{}' ".format(key, value))
            out_file.write(f"{' '*indent}<{self.tag} {attr_string.strip()}>\n")
        else:
            out_file.write(f"{' '*indent}<{self.tag}>\n")
        for line in self.content:
            if isinstance(line, str):
                out_file.write(f"{' '*(indent+4)}{line}")
            elif isinstance(line, object):
                line.render(out_file, indent=indent+4)
        out_file.write("</{}>\n".format(self.tag))
        return out_file

class Html(Element):
    ind = 0
    def render(self, out_file, **kwargs):
        out_file.write(f'<!DOCTYPE html>\n')
        Element.render(self, out_file, **kwargs)
            
class Head(Element):
    tag = 'head'

class Body(Element):
    tag = 'body'

class P(Element):
    tag = 'p'

class Hr(Element):
    tag = 'hr'
    
class H1(Element):
    tag = 'h1'
    
class H2(Element):
    tag = 'h2'

class H3(Element):
    tag = 'h3'

class H4(Element):
    tag = 'h4'
    
class H5(Element):
    tag = 'h5'

class H6(Element):
    tag = 'h6'

class Footer(Element):
    tag = 'footer'

class Ul(Element):
    tag = 'ui'
    
class Li(Element):
    tag = 'li'

class OneLineTag(Element):
    def render(self, out_file, **kwargs):
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else: 
            indent = self.ind
        if self.attrs:
            attr_string = ''
            for key, value in self.attrs.items():
                attr_string += str("{}='{}' ".format(key, value))
            out_file.write(f"{' '*indent}<{self.tag} {attr_string.strip()}>")
        else:
            out_file.write(f"{' '*indent}<{self.tag}>")
        for line in self.content:
            if isinstance(line, str):
                out_file.write(f"{line}")
            elif isinstance(line, object):
                line.render(out_file, indent=indent+4)
        out_file.write(f"</{self.tag}>\n")
        return out_file

class Title(OneLineTag):
    tag = 'title'

class SelfClosingTag(Element):
    '''SubClass without \n or closing tag'''
    def __init__(self, **kwargs):
        if 'content' in kwargs:
            raise ValueError('Only hr and br allow self closing tags')
        if kwargs:
            self.attrs = kwargs
        else: 
            self.attrs = None
 
    def render(self, out_file, **kwargs):
        if 'indent' in kwargs:
            indent = kwargs['indent']
        else:
            indent = self.ind
        if self.attrs:
            attr_string = ""
            for key, value in self.attrs.items():
                attr_string += str("{}='{}' ".format(key, value))
            out_file.write('f"{ '  '*indent}<{self.tag} {attr_string.strip()} />\n"')
        else:
            out_file.write('f"{' '*indent}<self.tag} />\n"')
        return out_file
        
class hr(SelfClosingTag):
    tag = 'hr'

class br(SelfClosingTag):
    tag = 'br'
    
class meta(SelfClosingTag):
    tag = 'meta'

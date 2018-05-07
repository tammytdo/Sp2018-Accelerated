"""
test code for html_render.py

This is just a start -- you will need more tests!
"""

import io
import pytest

# import * is often bad form, but makes some sense for testing.
from html_render import *


# utility function for testing render methods
# needs to be used in multiple tests, so we write it once here.
def render_result(element, ind=""):
    """
    calls the element's render method, and returns what got rendered as a
    string
    """
    # the StringIO object is a "file-like" object -- something that
    # provides the methods of a file, but keeps everything in memory
    # so it can be used to test code that writes to a file, without
    # having to actually write to disk.
    outfile = io.StringIO()
    element.render(outfile, ind)
    return outfile.getvalue()

########
# Step 1
########

def test_init():
    """
    This only tests that it can be initialized with and without
    some content -- but it's a start
    """
    e = Element()

    e = Element("this is some text")


def test_append():
    """
    This tests that you can append text

    It doesn't test if it works --
    that will be covered by the render test later
    """
    e = Element("this is some text")
    e.append("some more text")


def test_render_element():
    """
    Tests whether the Element can render two pieces of text
    So it is also testing that the append method works correctly.

    It is not testing whether indentation or line feeds are correct.
    """
    e = Element("this is some text")
    e.append("and this is some more text")

    # This uses the render_results utility above
    file_contents = render_result(e).strip()

    # making sure the content got in there.
    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    # make sure it's in the right order
    assert file_contents.index("this is") < file_contents.index("and this")

    # making sure the opening and closing tags are right.
    assert file_contents.startswith("<html>")
    assert file_contents.endswith("</html>")




# ########
# # Step 2
# ########


# tests for the new tags
def test_html():
    e = Html("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents
    print(file_contents)
    assert file_contents.endswith("</html>")


def test_body():
    e = Body("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<body>")
    assert file_contents.endswith("</body>")


def test_p():
    e = P("this is some text")
    e.append("and this is some more text")

    file_contents = render_result(e).strip()

    assert("this is some text") in file_contents
    assert("and this is some more text") in file_contents

    assert file_contents.startswith("<p>")
    assert file_contents.endswith("</p>")


def test_sub_element():
    """
    tests that you can add another element and still render properly
    """
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text"))
    page.append("Some more plain text.")
    page.append(Title("Here is a title"))
    page.append(Head("Here is a header"))

    file_contents = render_result(page)
    print(file_contents) # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p>" in file_contents
    assert "</p>" in file_contents
    assert "<title>" in file_contents
    assert "</title>" in file_contents
    assert "<head>" in file_contents
    assert "</head>" in file_contents

# #####################
# # indentation testing
# #####################


# def test_indent():
#     """
#     Tests that the indentation gets passed through to the renderer
#     """
#     html = Html("some content")
#     file_contents = render_result(html, ind="   ")

#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[0].startswith("   <")
#     assert lines[-1].startswith("   <")


# def test_indent_contents():
#     """
#     The contents in a element should be indented more than the tag
#     by the amount in the indent class attribute
#     """
#     html = Element("some content")
#     file_contents = render_result(html, ind="")

#     print(file_contents)
#     lines = file_contents.split("\n")
#     assert lines[1].startswith(Element.indent)


# def test_multiple_indent():
#     """
#     make sure multiple levels get indented fully
#     """
#     body = Body()
#     body.append(P("some text"))
#     html = Html(body)

#     file_contents = render_result(html)

#     print(file_contents)
#     lines = file_contents.split("\n")
#     for i in range(3):  # this needed to be adapted to the <DOCTYPE> tag
#         assert lines[i + 1].startswith(i * Element.indent + "<")

#     assert lines[4].startswith(3 * Element.indent + "some")

# this is for testing indenting -- we'll wait 'till we get to that
# def test_element_indent1():
#     """
#     Tests whether the Element indents at least simple content

#     we are expecting to to look like this:

#     <html>
#         this is some text
#     <\html>

#     More complex indentation should be tested later.
#     """
#     e = Element("this is some text")

#     # This uses the render_results utility above
#     file_contents = render_result(e).strip()

#     # making sure the content got in there.
#     assert("this is some text") in file_contents

#     # break into lines to check indentation
#     lines = file_contents.split('\n')
#     # making sure the opening and closing tags are right.
#     assert lines[0] == "<html>"
#     # this line should be indented by the amount specified
#     # by the class attribute: "indent"
#     assert lines[1].startswith(Element.indent + "thi")
#     assert lines[2] == "</html>"
#     assert file_contents.endswith("</html>")


########
# Step 3
########

# Added Step 3 tests above

########
# Step 4
########

# Testing for passing style arguments

def test_style_arg():
    """
    tests that you can add style arguments for html formatting
    """
    # not sure why but can't add **kwargs to html via the append method
    # without TypeError
    # complaining of an unexpected keyword argument
    # all other methods allow appends with **kwargs
    page = Html()
    page.append("some plain text.")
    page.append(P("A simple paragraph of text", style="text-align: center; font-style: oblique;"))
    page.append(P("Another simple paragraph of text"))
    page.append("Some more plain text.")
    page.append(Title("Here is a title"))
    page.append(Head("Here is a header", style="text-align: center; font-style: oblique;"))

    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails

    # note: The previous tests should make sure that the tags are getting
    #       properly rendered, so we don't need to test that here.
    assert "some plain text" in file_contents
    assert "A simple paragraph of text" in file_contents
    assert "Some more plain text." in file_contents
    assert "some plain text" in file_contents
    # but make sure the embedded element's tags get rendered!
    assert "<p style=\"text-align: center; font-style: oblique;>\" in file_contents>"
    assert "<p>" in file_contents
    assert "</p>" in file_contents
    assert "<title>" in file_contents
    assert "</title>" in file_contents
    assert "<head style=\"text-align: center; font-style: oblique;>\" in file_contents>"
    assert "</head>" in file_contents


########
# Step 5
########

# Testing for hr lines

def test_Hr():
    """
    tests for 'hr /' and 'br /' insertion w/o closing tag
    """
    page = Html()
    head = Head()
    page.append(head)
    body = Body()
    body.append(Title("Here is a title"))
    body.append(Head("Here is a header"))
    body.append(P("A simple paragraph of text"))
    page.append(body)
    page.append(Hr())
#    body.append(Br)
#    page.append(body)
    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails
    assert "<title>" in file_contents
    assert "</title>" in file_contents
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "<hr />" in file_contents
    assert "</hr" not in file_contents


########
# Step 6
########

# Testing for hr embedded links

def test_link():
    """
    tests for link insertion
    """
    page = Html()
    head = Head()
    page.append(head)
    body = Body()
    body.append(Title("Here is a title"))
    body.append(Head("Here is a header"))
    body.append(P("A simple paragraph of text"))
    page.append(body)
    page.append(Hr())
    page.append(A("http://google.com", "link"))
    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails
    assert "<title>" in file_contents
    assert "</title>" in file_contents
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "<hr />" in file_contents
    assert "</hr" not in file_contents
    assert '<a href="http://google.com">link</a>'


########
# Step 7
########

# Testing for list

def test_list():
    """
    tests for list creation and appending
    """
    page = Html()
    head = Head()
    page.append(head)
    body = Body()
    body.append(Title("Here is a title"))
    body.append(Head("Here is a header"))
    body.append(P("A simple paragraph of text"))
    page.append(body)
    page.append(Hr())
    mylist = Ul(id="TheTestList", style="line-height:200%")
    mylist.append(Li('This is item 1'))
    mylist.append(Li('This is item 2'))
    page.append(mylist)
    file_contents = render_result(page)
    print(file_contents)  # so we can see it if the test fails
    assert "<title>" in file_contents
    assert "</title>" in file_contents
    assert "<head>" in file_contents
    assert "</head>" in file_contents
    assert "<hr />" in file_contents
    assert "</hr" not in file_contents
    assert "<li>" in file_contents
    assert "This is item 1" in file_contents
    assert "</li>" in file_contents
    assert "This is item 2" in file_contents

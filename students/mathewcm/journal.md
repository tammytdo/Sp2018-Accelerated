<!--The is the learning journal for Mathew Martin taking Python CWE Accelerated course at the University of Washington Spring 2018-->

# Learning Journal for Python CWE Spring(sprint)2018

#### Mathew C. Martin / UWPCE Spring 2018

This journal is intended for reference. It is not intended to be authoritative or a replacement for the published docs. I will attempt to provide sourcing information as best I can but much of the material is taken from open source and creative commons available for free online and from course materials provided for educational purposes and contained within the curriculum posted.

#### 18.4.19: Lesson 04

Recursion: If a function calls itself, we call that <em>recursion</em>.

Call Stack: Like with other functions, a call within a call establishes a <em>call stack</em>.

WTFs per minute: Docstrings and Comments can reduce the number of WTFs/minute

```
def sum_series(nth=1, sequence=(0, 1)):
    sequence = list(sequence)
    for i in range(2, nth):
        sequence.append(sequence[i-2] + sequence[i-1])
    print(sequence)
    return sequence[nth-1]
```
Anytime you mutate a list you should use a shallow copy.

Lookup enumerate and append methods as related to lesson03

Open source: Git hub repo for docs: (Pull Request with corrections) https://github.com/UWPCE-PythonCert/PythonCertDevel

Dictionaries give you fast lookup of arbitrary search.

#### Trigrams
```
"I wish" => ["I", "I"]
"wish I" => ["may", "might"]
"may I" => ["wish"]
"I might"
```
#### solutions to trigrams
```
sample = """Now is the time for all good men to come to the aid of the country"""

words = sample.split()

print(words)

def build_trigram(words):
    tris = {}
    for i in range(len(words) - 2):
        first = words[i]
        second = words[i + 1]
        third = words[i + 2]
        print(first, second, third)
        tris.setdefault(pair, []).append(third)
    print(tris)
    return tris

if __name__ == "__main__"
    trigram = build_trigram(words)
```
### 18.04.23: Lesson 05

<!-- function to write files to disk -->
```
def write_letters_to_disk():
  """
  """
  for donor in donors:
    letter = donor_ltr(donor)
    filename = donor[0]
    with open(filename, 'w') as outfile:
      outfile.write(letter)
```

<!-- Converting mailroom tuple data to dictionary -->

<!-- Lesson 05 exceptions notes: -->
```
try:
  not_joke = fun(first_try[0])
except SyntaxError:
  print("That joke doesn't exist")
else:
  print(not_joke)
finally:
  print("This always runs")
```
### 18.04.25

#### All the “set” operations from math class…

- s.isdisjoint(other)
- s.issubset(other)
- s.union(other, ...)
- s.intersection(other, ...)
- s.difference(other, ...)
- s.symmetric_difference( other, ...)



### 18.04.25.18:00

Had some difficulties with github and my git process. I think I somehow got out of sync during class but I'm not certain. What I do know is that git blame is a critical learning tool that one day will haunt my brute force style. I rolled back to a previous commit to get the merge conflicts to resolve. Somehow other students file changes were getting merge conflicts on my repo. git reset --hard <commit>

Life's challenges weigh heavily and the struggle if nothing else keeps the mind and muscle limber if a bit tender. While one door closes another opens in a thousand iterations I don't want to store. Given nifty tricks free to all; - I can sort thru with a bit less room than in overhead baggage.

"Life imitating art" and both are taking off for the stars. My google cultural institute project is in effect a collection and the metadata contained therein is precisely the use case I'm looking for. To both practice the innovative and open language of python and understand how best to give explicit name to the human spirit in a virtual namespace of digital simulacrum.

(Collections module reference)[https://docs.python.org/3.6/library/collections.html]

### 18.04.25.18:56

#### Common Idioms

```
for line in open('secrets.txt'):
    print(line)
```
(the file object is an iterator!)
```
f = open('secrets.txt')
while True:
    line = f.readline()
    if not line:
        break
    do_something_with_line()
```
### File Methods
#### Commonly Used File Methods:

- f.read()
- f.readline()  
- f.readlines()
- f.write(str)
- f.writelines(seq)
- f.seek(offset)
- f.tell() # for binary files, mostly
- f.close()

### All the stuff in os.path and more:
```
In [64]: import pathlib
In [65]: pth = pathlib.Path('./')
In [66]: pth.is_dir()
Out[66]: True
In [67]: pth.absolute()
Out[67]: PosixPath('/Users/Chris/PythonStuff/UWPCE/IntroPython2015')
In [68]: for f in pth.iterdir():
             print(f)
junk2.txt
junkfile.txt
```
### And it has a really nifty way to join paths, by overloading the “division” operator:
```
In [49]: p = pathlib.Path.home()  # create a path to the user home dir.

In [50]: p
Out[50]: PosixPath('/Users/Chris')

In [51]: p / "a_dir" / "one_more" / "a_filename"
Out[51]: PosixPath('/Users/Chris/a_dir/one_more/a_filename')
```
(OS Path Module Docs)[https://docs.python.org/3/library/pathlib.html]

### 18.4.28.10:00

Saturday morning and all is quiet on the NW front. The weather has us boxed in pining for the 70 degree days not long absent. Wrestling the Zen that is Python, a struggle of both mind and muscle.

Sorting information manually has always been something I loathed, not enough patience to ever find satisfaction in that enterprise. However, loaded to bear with effective tools, it is something I can find instant pleasure. Looking forward to understanding how to implement logic and computer processing power in a practical manner. I've worked as an archivist and administrator and can see how important and powerful these tools in coordinating just about any modern endeavor.

### 18.4.28.10:10

#### Assignment: Mailroom, Part 2

Update mailroom program to do the following:

- Use dicts where appropriate
- See if you can use a dict to switch between the users selections. See Using a Dictionary to switch (Using a Dictionary to switch)[https://uwpce-pythoncert.github.io/PythonCertDevel/modules/DictionaryAsSwitch.html#dict-as-switch]
- Try to use a dict and the .format() method to do the letter as one big template rather than building up a big string in parts.


<!-- Look up Open() syntax... f.write(create_letter(donor)) -->

### 18.4.28.14:35
Mailroom.py refactor with dict switch testing successful att


### 18.4.28.16:29

Bigstring handy trick from video:

```
from random import SystemRandom
from string import ascii_letters as letters

bigstring = ''.join(SystemRandom().choice(letters) for _ in range(999))

bigstring
Out[24]: 'hVQZXTvmrHLhKIdUUpEHhfEWaNWafRvLgwsaEQkjyHUOthMJzsJCopxRUKHoLrMXSPJHEwITVnPMbafHUjIEmpRoTcQfadngGrURUzYqSvjRJrUhDDUNbRYfVNlHehdmilqQihLUUytNmhVxelaOjMFbnHInnqsmbasZToGjXsteTNoGGmNVGhVPkZfvKXXcibiKkXmenxXUEeZOGVkOZjOfHNKTMDAFDwHvFhrWpiocXBVskJEFTGGRMTdQkvOKsdObFQSMKrOaPexzmhpsvfbUgyIZbnrMvSsOjRmJsvUYAgTnWJeSYBhQlsHEZWWPSlnKSPwEwyLoqQhOfvgTgbiEsIVYOwlYAfoesNBMpNlksCQEbjFCcQTGktpXIuGzUhvHGhhhMTfFUnjXLLKCIzxuOAmLrYBEpfpgRdGjtPhnkyLUHJFNFnCzSwNKwWkYtoTFmegseQlEUGXpKfegyzxfJnPsICHnRcWGakjOAsrWdlyjmOiQkdKUmOmqcgWADDqrNhZRusxFkDizxUntzQQJFUAnYxTUxHAhMEaEfyqOUnrlBsfolOwSbRYMnvsTovDktJSUdXkeMEdiHuisaEInhOHTHhacCVehoWzuXIUUEqwXabcuCHgYzgyhjYGJAumWrkSUXEmkuexrTXkfCGxvnZCdqYMnZqlANlXmZXeXEHqRjSojeSayaTdamvdFMkJIiWmTkXPwwuPhBkdBfieQmumbKhlxvsdmdsHfnGhiTvHKxJxgAEdtwXkbdsadwFuiEwKxrHlMUVVBieRYYjBfLTddVOCPKUrGKzNQXxGTMYiqmbWCwFLWEzcjkZSSHkXpOvCrNkdwDEoeJlSKfTkgiNCAwuhkShFJRFAgbNCYJWQAGWzNcWaiXcLoVkhIvuIJujiIvuoxFRGozYFsbPGppNwmYLLVGEweKTWtNJXtetZSHgQrOSosoddVrMblOXaORwdCVKXQIJiCRatZFiRbRZZuLgVmCLjTvYW'

my_dict = dict.fromkeys(bigstring, 0)

for letter in bigstring:
    my_dict[letter] += 1
```

### IPython

(IPython Tips & Tricks)[http://ipython.readthedocs.io/en/stable/interactive/tips.html]

#### Help in IPython

Any built-in, method or attribute followed by a "?" gives a brief description in IPython.

 For windows-based systems, the default aliases are ‘copy’, ‘ddir’, ‘echo’, ‘ls’, ‘ldir’, ‘mkdir’, ‘ren’, and ‘rmdir’.

#### Embed IPython in your programs
A few lines of code are enough to load a complete IPython inside your own programs, giving you the ability to work with your data interactively after automatic processing has been completed. See the embedding section.

### Dictionary Comprehensions or "dict comps"

```
new_dict = { key: value for variable in a_sequence}

names = ['fred', 'John', 'MARY']
ids = [1, 2, 3]
d = dict(zip(names,ids))

d
Out[53]: {'John': 2, 'MARY': 3, 'fred': 1}

d = {id: name for id, name in zip(ids, names) if name != 'MARY'}

d
Out[55]: {1: 'fred', 2: 'John'}
```

### Collections module

(Python Docs on collections module)[https://docs.python.org/3/library/collections.html]

- namedtuple(): factory function for creating tuple subclasses with named fields
- deque: list-like container with fast appends and pops on either end
- Counter: dict subclass for counting hashable objects
- OrderedDict: dict subclass that remembers the order entries were added
- defaultdict: dict subclass that calls a factory function to supply missing values
- ChainMap: dict-like class for creating a single view of multiple mappings

- UserDict: wrapper around dictionary objects for easier dict subclassing
- UserList: wrapper around list objects for easier list subclassing
- UserString: wrapper around string objects for easier string subclassing

(Collections module overview)[https://pymotw.com/3/collections/]

### defaultdict()

```
from collections import defaultdict

dd = defaultdict(list)
dd['this'].append(23)
dd
Out[60]: defaultdict(list, {'this': [23]})
dd['this'].append(4)
dd['this'].append(4)
dd
Out[63]: defaultdict(list, {'this': [23, 4, 4]})
dd['that'].append(4)
dd
Out[65]: defaultdict(list, {'that': [4], 'this': [23, 4, 4]})
dd['those'].append(8)
dd
Out[67]: defaultdict(list, {'that': [4], 'this': [23, 4, 4], 'those': [8]})
dd['those'].append(16)
dd['those'].append(32)
dd['those'].pop()
Out[70]: 32
dd
Out[71]: defaultdict(list, {'that': [4], 'this': [23, 4, 4], 'those': [8, 16]})
```
Nice!!! "...you’ll get a dict that will automatically put an empty list in when the key isn’t there yet." ~ PythonCert 4.0

### 18.4.29.9:32  Comprehensions Lab
```
feast = ['lambs', 'sloths', 'orangutans',
          'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]

```
#### What is the output?
```
comprehension[0]
{'Lambs'}

comprehension[2]
{'Orangutans'}
```
#### Close!
```
feast = ['Lamn', 'sloths', 'orangutans', 'breakfast cereal', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
comprehension[1]
Out[74]: 'Sloths'
comprehension[0]
Out[75]: 'Lamn'
comprehension[2]
Out[76]: 'Orangutans'
feast[0] = 'lamb'
feast
Out[78]: ['lamb', 'sloths', 'orangutans', 'breakfast cereal', 'fruit bats']
comprehension = [delicacy.capitalize() for delicacy in feast]
comprehension[0]
Out[80]: 'Lamb'
comprehension[2]
Out[81]: 'Orangutans'
comp = [delicacy for delicacy in feast if len(delicacy) > 6]
comp[1]
Out[83]: 'breakfast cereal'
comp[0]
Out[84]: 'orangutans'
comp[3]
Traceback (most recent call last):
  File "<ipython-input-85-224dba9f58bc>", line 1, in <module>
    comp[3]
IndexError: list index out of range
```
### Filtering lists with list comprehensions
```
len(feast)
Out[86]: 5
len(comp)
Out[87]: 3
```
### Unpacking tuples in list Comprehensions
```
list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples]

comprehension[0]
Out[90]: 'lumberjack'

comprehension[2]
Out[91]: 'spamspamspamspam'
```
I got the first right but thought it was 8*spam for the second not 4 * spam. I mulitplied by the index... ???
```
len(comprehension[2])
Out[92]: 16
```
Missed the len()...

### Double list Comprehensions
```
eggs = ['poached egg', 'fried egg']
meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in eggs for meat in meats]
len(comprehension)
Out[98]: 6
comprehension[0]
Out[99]: 'poached egg and lite spam'
comprehension = { c for c in 'aabbbcccc'}
comprehension
Out[101]: {'a', 'b', 'c'}
```
### Set comprehensions
<!-- sets are immutable requiring a unique key which only one can exist in any given sequence.-->
```
comprehension = { c for c in 'aabbbcccc'}
comprehension
Out[101]: {'a', 'b', 'c'}
```

### Dictionary Comprehensions
```
dict_of_weapons = {'first': 'fear',
                    'second': 'surprise',
                    'third': 'ruthless efficiency',
                    'forth': 'fanatical devotion',
                    'fifth': None}

dict_comprehension = {k.upper(): weapon for k, weapon in dict_of_weapons.items() if weapon}
```
What is the output?
```
[a for a in dir(str) if a[0] != "_"]
```
### Unit testing
```
unittest?
Type:        module
String form: <module 'unittest' from 'd:\\Anaconda3\\lib\\unittest\\__init__.py'>
File:        d:\anaconda3\lib\unittest\__init__.py
Docstring:  
Python unit testing framework, based on Erich Gamma's JUnit and Kent Beck's
Smalltalk testing framework (used with permission).

This module contains the core framework classes that form the basis of
specific test cases and suites (TestCase, TestSuite etc.), and also a
text-based utility class for running the tests and reporting the results
 (TextTestRunner).

Simple usage:

    import unittest

    class IntegerArithmeticTestCase(unittest.TestCase):
        def testAdd(self):  # test method names begin with 'test'
            self.assertEqual((1 + 2), 3)
            self.assertEqual(0 + 1, 1)
        def testMultiply(self):
            self.assertEqual((0 * 10), 0)
            self.assertEqual((5 * 8), 40)

    if __name__ == '__main__':
        unittest.main()
```
(Further information is available in the bundled documentation, and from)[http://docs.python.org/library/unittest.html]

## Lesson 07

### 18.4.30.13:00

### Object Oriented Programming

(Programming Paradigms)[https://en.wikipedia.org/wiki/Programming_paradigm]

It can be officially noted that I finally have attained "class".
```
class C:
    pass

type(C)
Out[58]: type

issubclass(C, object)
Out[59]: True

print(C)
<class '__main__.C'>

dir(C)
Out[61]:
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']

print(C.dir())
Traceback (most recent call last):

  File "<ipython-input-62-712969ace520>", line 1, in <module>
    print(C.dir())

AttributeError: type object 'C' has no attribute 'dir'

print(C.__hash__)
<slot wrapper '__hash__' of 'object' objects>

print(C.__main__)
Traceback (most recent call last):

  File "<ipython-input-64-f258886a611d>", line 1, in <module>
    print(C.__main__)

AttributeError: type object 'C' has no attribute '__main__'

print(C.__dict__)
{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None}

```
<!-- Cool!!! I found where __main__ is kept just dundering around.-->
```
print(C.__module__)
__main__

print(C.__weakref__)
<attribute '__weakref__' of 'C' objects>

__setattr__?
Object `__setattr__` not found.

C.__setattr__?
Signature:      C.__setattr__(self, name, value, /)
Call signature: C.__setattr__(*args, **kwargs)
Type:           wrapper_descriptor
String form:    <slot wrapper '__setattr__' of 'object' objects>
Docstring:      Implement setattr(self, name, value).

```

```
class Point:
    x = 1
    y = 2

Point
Out[73]: __main__.Point

p = Point
p = Point()
p
Out[76]: <__main__.Point at 0x27c479ce630>
p.x
Out[77]: 1
p.y
Out[78]: 2
run simple_classes
p.x is: 3
p.y is: 4
4
red
4
red
blue

import simple_classes
p.x is: 3
p.y is: 4
4
red
4
red
blue

Circle
Out[81]: __main__.Circle

Rect
Out[82]: __main__.Rect

Rect(5, 7)
Out[83]: <__main__.Rect at 0x27c47c010b8>

Rect
Out[84]: __main__.Rect

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

Point(x, y)
Traceback (most recent call last):

  File "<ipython-input-86-474e6b1ccaa2>", line 1, in <module>
    Point(x, y)

NameError: name 'x' is not defined

Point(4, 5)
Out[87]: <__main__.Point at 0x27c47c01f98>

p = Point(3,4)
p
Out[89]: <__main__.Point at 0x27c479a3630>
m = Point(4, 5)
m
Out[91]: <__main__.Point at 0x27c47987b00>
print("p.x is:", p.x)
p.x is: 3
print("m.x is:", m.x)
m.x is: 4
class Point:
    def a_func(self, x, y)
  File "<ipython-input-94-c15cada14c1e>", line 2
    def a_func(self, x, y)
                          ^
SyntaxError: invalid syntax

class Point:
    size = 4
    color = "red"

def get_color(self):
    return self.color

p3.get_color()
Out[97]: 'red'

class C:
    x = [1,2,3]
    def __init__(self):
        self.y = [4,5,6]

c1 = C()
c2 = C()
c1.x is c2.x
Out[112]: True

c1.y is c2.y
Out[113]: False
```
### Typical Methods
```
class Circle:
    color = 'red'
    def __init__(self, diameter):
        self.diameter = diameter

class Circle:
    color = 'red'
    def __init__(self, diameter):
        self.diameter = diameter

class Circle:
    color = 'red'
    def __init__(self, diameter):
        self.diameter = diameter
    def expand(self, factor=2):
        self.diameter = self.diameter * factor
```
## Subclassing and Inheritance

### Inheritance

### 18.5.1.15:20 Class and Instance Attributes

Notes for Python Attributes - Scope video

(Video)[https://canvas.uw.edu/courses/1197533/pages/lesson-07-content?module_item_id=8240379)]
```
class C:
    this = 5
    def __init__(self, that):
        self.that = that

c1
Traceback (most recent call last):

  File "<ipython-input-10-5348681b35c2>", line 1, in <module>
    c1

NameError: name 'c1' is not defined

c1 = C(10)
c2 = C(20)

c1 is c2
Out[13]: False

c1.this
Out[14]: 5

c2.that
Out[15]: 20

c1.that
Out[16]: 10

C.this = 45

c1.this
Out[18]: 45

c2.this
Out[19]: 45

c1.this = 56

c1.this
Out[21]: 56

c2.this
Out[22]: 45

class C:
    this = []
    def __init__(self, that):
        self.that = [that]

c1 = C(10)

c2 = C(20)

c1.that.append(45)

c1.that
Out[28]: [10, 45]

c2.that
Out[29]: [20]

c1.this
Out[30]: []

c2.this
Out[31]: []

c1.this.append(68)

c1.this
Out[33]: [68]

c2.this
Out[34]: [68]

class C:
    this = []

class C:
    this = []
    def __init__(self, that):
        self.that = [that]
    def mutable(self, val):
        self.this.append(val)
        self.that.append(val)

c1 = C(10)

c2 = C(20)

c1.mutate(99)
Traceback (most recent call last):

  File "<ipython-input-39-413f783e5d77>", line 1, in <module>
    c1.mutate(99)

AttributeError: 'C' object has no attribute 'mutate'

class C:
    this = []

    def __init__(self, that):
        self.that = [that]

    def mutable(self, val):
        self.this.append(val)
        self.that.append(val)

c1 = C(10)

c2 = C(20)

class C:
    this = []

    def __init__(self, that):
        self.that = [that]

    def mutate(self, val):
        self.this.append(val)
        self.that.append(val)

c1 = C(10)

c2 = C(20)

c1.mutute(99)
Traceback (most recent call last):

  File "<ipython-input-46-193784b1d93e>", line 1, in <module>
    c1.mutute(99)

AttributeError: 'C' object has no attribute 'mutute'

class C:
    this = []

    def __init__(self, that):
        self.that = [that]

    def mutate(self, val):
        self.this.append(val)
        self.that.append(val)    

c1 = C(10)

c2 = C(20)

c1.mutate(99)

c1.this
Out[51]: [99]

c1.that
Out[52]: [10, 99]

vars(c2)
Out[53]: {'that': [20]}

vars(c1)
Out[54]: {'that': [10, 99]}

c1.this = []

vars(c1)
Out[56]: {'that': [10, 99], 'this': []}

c2.this
Out[57]: [99]

class B(C):
    pass
b = B(99)

.this
Out[59]: [99]

vars(c2)
Out[60]: {'that': [20]}

vars(c1)
Out[61]: {'that': [10, 99], 'this': []}

### Points out the difference in rebinding a name versus mutating an object in place.

class B(C):
    pass

b = B(34)

b.this
Out[65]: [99]

b.that
Out[66]: [34]

b.this.append(77)

c2.this
Out[68]: [99, 77]

class C:
    this = []

    def __init__(self, that):
        self.that = [that]

    def mutate(self, val):
        self.this.append(val)
        self.that.append(val)


class C:
    this = []

    def __init__(self, that):
        self.that = [that]

    def mutate(self, val):
        self.this.append(val)
        self.that.append(val)

class C:
    this = []

    def __init__(self, that):
        print(type(self))
        self.that = [that]

    def mutate(self, val):
        self.this.append(val)
        self.that.append(val)

class B(C):
    pass

b = B(77)
<class '__main__.B'>

c = C(88)
<class '__main__.C'>

class B(C):
    this = []

# B overrides class C attributes

b1 = B(22)
<class '__main__.B'>

b.this
Out[78]: []

b2 = B(44)
<class '__main__.B'>

c1 = C(33)
<class '__main__.C'>

c2 = C77)
  File "<ipython-input-81-2d6cf2451f0c>", line 1
    c2 = C77)
            ^
SyntaxError: invalid syntax

c2 = C77
Traceback (most recent call last):

  File "<ipython-input-82-087dd32a1ea5>", line 1, in <module>
    c2 = C77

NameError: name 'C77' is not defined

c2 = C(77)
<class '__main__.C'>

b2.this
Out[84]: []

b2 = B(44)
<class '__main__.B'>

c1.this
Out[86]: []
```



### IPython Keyboard Shortcuts

Shortcut	Action
Shift-Enter	run cell
Ctrl-Enter	run cell in-place
Alt-Enter	run cell, insert below
Ctrl-m x	cut cell
Ctrl-m c	copy cell
Ctrl-m v	paste cell
Ctrl-m d	delete cell
Ctrl-m z	undo last cell deletion
Ctrl-m –	split cell
Ctrl-m a	insert cell above
Ctrl-m b	insert cell below
Ctrl-m o	toggle output
Ctrl-m O	toggle output scroll
Ctrl-m l	toggle line numbers
Ctrl-m s	save notebook
Ctrl-m j	move cell down
Ctrl-m k	move cell up
Ctrl-m y	code cell
Ctrl-m m	markdown cell
Ctrl-m t	raw cell
Ctrl-m 1-6	heading 1-6 cell
Ctrl-m p	select previous
Ctrl-m n	select next
Ctrl-m i	interrupt kernel
Ctrl-m .	restart kernel
Ctrl-m h	show keyboard shortcuts
[sheepish] The keyboard shortcuts are available under the Help menu. [/sheepish]

### Anaconda Spyder3 Keyboard Shortcuts

#### Spyder Keyboard Shortcuts for the Editor under Windows
##### Conventional (more or less) Keyboard Shortcuts

- Home: Go to start of line
- End: Go to end of line
- Left: Arrow Go to previous character
- Right: Arrow Go to next character
- Up Arrow: Go up to previous line
- Down Arrow: Go down to next line
- Ctrl + Left Arrow: Go to start of previous word
- Ctrl + Right Arrow: Go to start of next word
- Ctrl + Up Arrow (or Ctrl + Home): Go to start of document
- Ctrl + Down Arrow (or Ctrl + End): Go to end of document
- Ctrl + O: Open file
- Ctrl + N: Open new file
- Ctrl + Backspace: Delete to beginning of previous word
- Ctrl + Delete: Delete to beginning of next word
- Ctrl + A: Select all
- Ctrl + C: Copy selection
- Ctrl + S: Save current file
- Ctrl + Shift + S: Save current file as
- Ctrl + Alt + S: Save all open files
- Delete: Delete selection or current character
- Ctrl + X: Cut selection
- Ctrl + V: Paste clipboard contents
- Ctrl + Z: Undo last action
- Ctrl + Shift + Z: Redo last action
- Ctrl + Q Quit: Spyder

#####Keyboard Shortcuts for Navigation
- Ctrl + L Go to line
- Ctrl + Tab Go to previous file
- Ctrl + Shift + Tab Go to next file
- Ctrl + Shift + T Go to (i.e., open) last closed file
- Ctrl + P Go to (i.e., switch to and open) file …
- Ctrl + Alt + Left Arrow Go to previous cursor location
- Ctrl + Alt + Right Arrow Go to next cursor location
- Ctrl + Alt + Shift + Left Arrow Go to last edit location
- Ctrl + G Go to definition

##### Keyboard Shortcuts for Zooming and Commenting
- Ctrl + + (or Ctrl + =) Zoom in
- Ctrl + - Zoom out
- Ctrl + 0 Zoom reset
- Ctrl + 1 Toggle comment selection (or line)
- Ctrl + 4 Insert block comment
- Ctrl + 5 Uncomment block comment

##### Keyboard Shortcuts for Search and Replace
- Ctrl + F Find text
- F3 Find next
- Shift + F3 Find previous
- Ctrl + R Replace text

##### Keyboard Shortcuts for Moving, Copying, Duplicating, Deleting
- Alt + Down Arrow Move line down
- Alt + Up Arrow Move line up
- Ctrl + D Delete line
- Ctrl + Alt + Down Arrow Copy line
- Ctrl + Alt + Up Arrow Duplicate line

##### Miscellaneous Keyboard Shortcuts
- Tab Indent selected line(s)
- Shift + Tab Unindent selected line(s)
- Ctrl + U Transform to lowercase
- Ctrl + Shift + U Transform to uppercase
- Ctrl + W (or Ctrl + F4) Close file
- Ctrl + Shift + W Close all
- Ctrl + Space Code completion
- Ctrl + I Inspect current object
- Meta + K Kill to end of line
- Meta + U Kill to start of line
- Meta + Shift + Y Rotate
- Meta + Y Yank

##### Keyboard Shortcuts for Executing Code
- F5 Run file (complete program)
- F6 Re-run last script
- Ctrl + F6 Configure …
- F9 Run selection (or current line)
- F10 Profile
- Ctrl + Enter Run cell
- Shift + Enter Run cell and advance
- F8 Run static code analysis
- Ctrl + T Open an iPython console
- Ctrl + . Restart kernel

##### Keyboard Shortcuts for Debugging Code
- F12 Breakpoint
- Shift + F12 Conditional breakpoint
- Ctrl + F5 Debug
- Ctrl + F10 Step
- Ctrl + F11 Step into
- Ctrl + Shift + F11 Step return
- Ctrl + F12 Continue
- Ctrl + Shift + F12 Stop

##### Keyboard Shortcuts for Interface Adjustment and Layouts
- Ctrl + Shift + E Editor pane
- Ctrl + Shift + C Python console pane
- Ctrl + Shift + I iPython console pane
- Ctrl + Shift + V Variable explorer pane
- Ctrl + Shift + H Help pane
- Ctrl + Shift + X File explorer pane
- Ctrl + Shift + O (or Ctrl + Alt + O) Outline pane (show/hide)
- Ctrl + Shift + P Project explorer pane
- Ctrl + Shift + F Find in files pane
- Ctrl + Shift + L History log pane
- Ctrl + Shift + B Breakpoints pane
- Ctrl + Shift + D Online help pane
- Ctrl + Shift + F4 Close current pane
- Ctrl + Shift + F5 Lock panes
- Ctrl + Alt + Shift + M Maximize current pane
- Ctrl + Alt + Shift + P Preferences
- F11 Full screen mode
- Alt + Shift + T Toolbars (hide/show)
- Alt + Shift + PageUp Use previous layout
- Alt + Shift + PageDown Use next layout
- Alt + Shift + S Save current layout
- Alt + Shift + P Layout preferences
-
(Source .pdf)[http://cs.smu.ca/~porter/csc/227/SpyderKeyboardShortcutsEditor.pdf]


### Python's Class Development Toolkit

#### Agile Methodology
- Out with waterfall: Design Code Test Ship
- In with: Tight iterations
- Let little bits of design, coding and testing inform later bits of design, coding and testing
- The core idea is iterate and adapt quickly
- MVP Minimum Value Product
- Add Commit Push

##### Initialize instance variables

- __init__ isn't a constructor. It's job is to initialize the instance variables.
- Regular methods have "self" as first argument.

##### Class variables for shared data

- Don't use floating point numbers for a version.
- Minimum viable product: Ship it!

```
class Circle:
    'An advanced circle analytic toolkit'

    version = '0.1'         # class variable

    def __init__(self, radius):
        self.radius = radius            # instance variable

    def area(self):
        'Perform quadrature on a shape of uniform radius'
        return 3.14 * self.radius ** 2.0

    c = Circle(10)
    print('Circuituous version', Circle.version)

    print('A circle of radius', c.radius)
    print('has an area of', c.area())
    print()
```
   <!-- Instruction in Python 2.7 to difficult to refactor on the fly -->

##### Stop writing classes by Jack Diederich

```
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
- Simple is better than complex.
Complex is better than complicated.
- Flat is better than nested.
Sparse is better than dense.
- Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

Jack highlighted the bulleted points above
```

##### Obfuscated Function Call

```
class Greeting(object):
    def __init__(self, greeting='hello'):
        self.greeting = greeting

    def greet(self, name):
        return '%s! %s' % (self.greeting, name)

greeting = Greeting('hola')
print greeting.greet('bob')
```

##### Additional Reading Lesson 07

(Instantiating Classes)[http://www.diveintopython3.net/iterators.html#defining-classes]

### 18.5.1.21:47

Completed all the intro to OO materials.

### HTML Rendering Excercise

Challenge is to render elements nested in other elements

- Office Hours online and in Paccar Hall Study Room #9 2:30pm - 4:30pm Sunday May 6th.

#### Test_fraction.py notes

1+2 = +(1, 2)

def __eq__(self, other):
  return self.num * other.denom == self.denom * other.num

__ne__ ???

#### Use case for comparing positive fractions
```
def __init__(self, num, denom):
    if denom == 0:
      raise ZeroDivisionError
    if not isinstance(num, int) or not isinstance

def test_fraction_lt():
    assert Fraction(1, 2) < Fraction(2, 3) # Fraction(1,2).__lt__(Fraction(2,3))
    assert Fraction(1, -2) < Fraction(2, 3)

    if denom < 0:
        num *= -1
        denom *= -1
    self.num

def __str__(self):
    return str(self.num) + "/" + str(self.denom)

def __lt__(self, other):
  self.num * other.denom < self.denom * other.num

def test_fraction_add():
    assert Fraction(1,2) + Fraction(2,3) == Fraction(7,6)
    # Fraction(1,2.__add__)
    assert str(Fractions(1,3) + Fraction(1,6)) == '1/2'

def __add__(self, other):
    num = self.num + other.denom < self.denom * other.number
    denom = self.denom * other.denom
    return Fraction(num, denom)
```
#### At the constructor is the best time to do normalization: Add GCD algorithm to the constructor to get all tests to pass.

class Base:
    def __init__(self):
        print(type(self))

class Derived(Base):
    def __init__(self):
        super().__init__()
        print(type(self))

d = Derived()
<class '__main__.Derived'>
<class '__main__.Base'>


#### Python static vs. class Methods
```
class StaticAdder:
    @staticmethod
    def add(a, b):
        return a + b

StaticAdder.add(3,6)
```
No highly used!

#### Class methods

class Classy:
    x = 2
    @classmethod
    def a_class_method(cls, y):
        print("in a class method: ", cls)
        return y ** cls.x

Classy.a_class_method(4)

#### Alternative Constructors *** Know this methods (Polymorphism)

#### Super

1) The method being called by super needs to exist
2) Caller and the called need to have matching argument signatures
3) Every occurance of the method needs to use Super

```
class A():
    def __init__(self):
        print("in A __init__ ")
        print("self's class is:", self.__class__)
        s = super().__init__()

class B():
    def __init__(self):
        print("in B __init__ ")
        print("self's class is:", self.__class__)
        s = super().__init__()

class C():
    def __init__(self):
        print("in C __init__ ")
        print("self's class is:", self.__class__)
        s = super().__init__()

class D(C, B, A):
    def __init__(self):
        print("in D.__init__")
        print("self's class is:", self.__class__)
        super().__init__()


print("D's MRO:")
for c in D.__mro__:
    print(c)

D's MRO:
<class '__main__.D'>
<class '__main__.C'>
<class '__main__.B'>
<class '__main__.A'>
<class 'object'>


d = D()
in D.__init__
self's class is: <class '__main__.D'>
in C __init__
self's class is: <class '__main__.D'>
in B __init__
self's class is: <class '__main__.D'>
in A __init__
self's class is: <class '__main__.D'>

super?
Init signature: super(self, /, *args, **kwargs)
Docstring:     
super() -> same as super(__class__, <first argument>)
super(type) -> unbound super object
super(type, obj) -> bound super object; requires isinstance(obj, type)
super(type, type2) -> bound super object; requires issubclass(type2, type)
Typical use to call a cooperative superclass method:
class C(B):
    def meth(self, arg):
        super().meth(arg)

# This works for class methods too:

class C(B):
    @classmethod
    def cmeth(cls, arg):
        super().cmeth(arg)
Type:           type

c = C()
in C __init__
self's class is: <class '__main__.C'>

# Try an invalid relationship:

super(D, c)
Traceback (most recent call last):

  File "<ipython-input-100-f817bbf8c6b4>", line 1, in <module>
    super(D, c)

TypeError: super(type, obj): obj must be an instance or subtype of type


# This fails: C is not a subclass of D

s_a = super(A, d)

print(s_a)
<super: <class 'A'>, <D object>>

s_b = super(B, d)

print(s_b)
<super: <class 'B'>, <D object>>

print(D.__mro__)
(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

print(s_a)
<super: <class 'A'>, <D object>>

class A():
    def this(self):
        print("in A.this")

class B():
    def this(self):
        print("in B.this")

class C(A,B):
    def this(self):
        A.this(self)
        B.this(self)

print("Running with super()")
Running with super()

c = C()
c.this()

in A.this
in B.this

# C's this explicitly called both A and B's methods

class A():
        def this(self):
            print("in A.this")

class B(A):
    def this(self):
        print("in B.this")

class C(B):
    def this(self):
        print("in C.this")
        super().this()

for c in C.__mro__:
    print(c)

<class '__main__.C'>
<class '__main__.B'>
<class '__main__.A'>
<class 'object'>
```
### Note: A.this did NOT get called!
#### Even though it is in the MRO
#### Python stopped when it found the method in B.
```
C.this
Out[120]: <function __main__.C.this>
```
#### Using Super Everywhere:
```
class Base():
    def this(self):
        pass # just so there is a base that has the method

class A(Base):
    def this(self):
        print("in A.this")
        super().this()

class B(Base):
    def this(self):
        print("in B.this")
        super().this()

class C(A,B):
    def this(self):
        print("in C.this")
        super().this()


c = C()
c.this()
print(Base.__mro__)

in C.this
in A.this
in B.this
(<class '__main__.Base'>, <class 'object'>)
```
#### Adding Up Immutables
```
import random

list_of_numbers = [random.randint(0, 100) for i in range(20)]
list_of_strings = ["this ", "that, ", "the other"]


def add_up_seq(seq):
    total = 0
    for item in seq:
        total += item
    return total


add_up_seq(list_of_numbers)
Out[130]: 1049

add_up_seq(range(100))
Out[131]: 4950

def add_up_seq(seq, start=0):
    total = 0
    for item in seq:
        total += item
    return total


def add_up_seq(seq, start=0):
    total = start
    for item in seq:
        total += item
    return total


add_up_seq(list_of_strings, start="")
Out[134]: 'this that, the other'
```
#### There is a better way
```
sum(range(5))
Out[136]: 10

sum(list_of_numbers)
Out[137]: 1049

% timeit add_up_seq(range(1000000))
48.3 ms ± 205 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

% timeit sum(range(1000000))
30.3 ms ± 123 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

%timeit "".join(list_of_strings)
109 ns ± 4.53 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

```
### 18.5.7.6:00

At least (2) classes in mailroom. Donor class and UI class are suggested.

### 18.5.9.9:30

Final push!!! How agile can one be in the scrum of life? Seemingly always at the bottom of the pile and reality's foot pressing squarely on my face. With achilles torn my resistance is futile at best. Yet, no time for rest! Onward and upwards like the Phoenix reborn...

Focusing on submitting HTML renderer today and understanding how to incorporate classes in data manipulation and handling strings in particular.

#### From class materials

[UWPCE Canvas Spring 2018 Accelerated](https://canvas.uw.edu/courses/1197533/assignments/4129941?module_item_id=8240380)

Checking If It’s The Right Type
How do you decide if the wrapper is required?

Checking it it’s an instance of Element:

You could check and see if the object being appended is an Element:
```
if isinstance(content, Element):
    self.content.append(content)
else:
    self.content.append(TextWrapper(content))
```

This would work well, but closes the door to using any other type that may not be a strict subclass of Element, but can render itself. Not too bad in this case, but in general, frowned upon in Python.

Alternatively, you could check for the string type:
```
if isinstance(content, str):
    self.content.append(TextWrapper(content))
else:
    self.content.append(content)
```
I think this is a little better – strings are a pretty core type in Python, so it’s not likely that anyone is going to need to use a “string-like” object.

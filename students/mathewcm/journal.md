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

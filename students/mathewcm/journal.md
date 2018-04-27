<!--The is the learning journal for Mathew Martin taking Python CWE Accelerated course at the University of Washington Spring 2018-->

# Learning Journal for Python

### Mathew C. Martin / UWPCE Spring 2018

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
### solutions to trigrams
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
## 18.04.23: Lesson 05

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
## 18.04.25

### All the “set” operations from math class…

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

## Common Idioms

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
## File Methods
### Commonly Used File Methods:

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
## And it has a really nifty way to join paths, by overloading the “division” operator:
```
In [49]: p = pathlib.Path.home()  # create a path to the user home dir.

In [50]: p
Out[50]: PosixPath('/Users/Chris')

In [51]: p / "a_dir" / "one_more" / "a_filename"
Out[51]: PosixPath('/Users/Chris/a_dir/one_more/a_filename')
```
(OS Path Module Docs)[https://docs.python.org/3/library/pathlib.html]

# 18.4.26.18:40

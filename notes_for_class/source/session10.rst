
:orphan:

.. _notes_session10:

####################
Notes for Session 10
####################

5/10/2018

A collection of notes to go over in class, to keep things organized.

Lightning Talks
===============

Anyone missed their chance?

Logistics, announcements (from Hosung)
======================================

Office hours
------------

Hosung's: 3-5pm, Saturday, 5/12/2018 @ Study Room #1 (not the usual #9), Foster Business Library, Paccar Hall

Also available online through Zoom. Email for appointment!

Grades
------

Canvas gradebook is now fully updated. The last two assignments (OO mailroom, funciontal mailroom) are not yet included in the total percent score. All others are included (submissions still accepted), and no submissions are treated as 0. Do make sure your gradebook entries are accurate and contact us otherwise. Do note that 80% assignment score is a requirement for an SC (Successful Completion) grade.

Merge conflicts
---------------

We've got a number of merge conflicts in PRs, which keep us from completing/merging those PRs. We need to fix them in person, so I'll contact each affected individual and try to sort this out. I also should have mentioned in last class that everyone should copy the example code files to their own student directory, not working directly on those files (in the example directory) that are pulled from upstream... My fault if merge conflicts were on that directory. I still saw strange merge conflicts, so we'll be fixing them in person in this class during the break.

Issues that came up during the week.
====================================

When to make a method or property?
-----------------------------------

It is a good idea to make a property to access information in your class that requires "inside information", For example, in a Donor class:

.. code-block:: python

  @property
  def maxdonation(self):
      return max(self.donations)

This way, client code can get the maximum donation without knowing, or caring, how the donations are stored in the class.

However, there is no need to create a property to "hide" something that is already part of the public API:

.. code-block:: python

  @property
  def namelength(self):
      return(len(self.name))

There is no point to this -- ``a_donor.name`` is expected to be a string -- so if you want to know how long it is, you can simply do:  ``len(a_donor.name)``

You *do* want to use properties to "hide" implementation details -- but the name attribute being a string is part of the API, not an implementation detail.


Anything else from OO mailroom?
-------------------------------


Supplements to Functional Programming in Python (from Hosung)
=============================================================

Searched the web for some good references on the topic, and found some (seemingly) good ones that I liked. We'll go over some examples from them:

https://anandology.com/python-practice-book/functional-programming.html : Really liked the trace and the memoize decorations.

https://maryrosecook.com/blog/post/a-practical-introduction-to-functional-programming : A seemingly good read on functional programming principles with examples in Python

http://www.cs.rpi.edu/~sibel/csci1100/fall2017/lecture_notes/lec24_functional.html : Seemingly good examples on lambda


The Next Class
==============

Next quarter, you'll finish up the core of the Python language, then go into depth on some of the more advanced features of the language. Finally, we'll do a bit with using Python with other tools, such as databases.

Here's an Outline:

Functional Programming 2
------------------------

* Comprehensions
* Lambda
* Iterators and Iterables
* Generators
* Itertools


Functional Programming 3
------------------------

* Closures and Currying
* Itertools
* Functools

Advanced Python Language Constructs
-----------------------------------

* Decorators
* Context Managers
* Recursion

Metaprogramming
---------------

* Namespaces
* Introspection
* Metaclasses
* Class Decorators


Debugging & Logging
-------------------
* Logging module
* Syslog
* pdb/ipdb

Advanced Testing
----------------
* Linting
* Coverage
* The unittest Module
* Fixtures
* Mocking

Relational Databases
--------------------
* SQL
* ORMs: PeeWee
* Sqlite
* Postgresql


NoSQL Databases
---------------
Object/Document, Key/Value and Graph Databases

* Schema vs “Schemaless”
* Mongo
* Redis
* Neo4j

Profiling & Performance
-----------------------

* Timing
* Profiling
* PyPy
* Cython

Concurrency & Async Programming
-------------------------------

* Concurrency
* Threading and Multiprocessing
* Message Queues
* Async


End of Quarter:
===============

We will review PRs through Monday.






# Homework assignment 4

In this set of homework assignments, you will answer some theoretical questions about *description logics and OWL*.

## Instructions

1. Read the description of the assignments.
1. Provide your answers to the questions, preferably typeset with LaTeX and using [this template](../templates/homework.tex).
1. Submit your solutions via [Canvas](https://canvas.uva.nl/courses/10768).

The difficulty of the assignments is indicated with stars (&star;'s): the more stars, the harder the assignment.

---

## Assignment 1 (&star;): modeling a knowledge base in ALC

In this assignment, you will use the description logic ALC to construct
a knowledge base (in other words, an ontology together with some facts)
that expresses a scenario about (some properties of and relations between)
the categories of countries, cities and persons.

*Assignment:* Give an ALC knowledge base, consisting of a TBox and an ABox,
that models the following pieces of knowledge:
- *Person* is a category.
- *Country* is a category, and *Republic* and *ConstitutionalMonarchy*
are subcategories of *Country*
- *City* is a category.
- The categories of persons, countries and cities are disjoint.
- *Republic* and *ConstitutionalMonarchy* are disjoint
- Every country is related by the relation *hasCapital* to some object in
category *City*.
- Every country is related by the relation *hasCapital* to only objects in
category *City*.
- Every country and every city is related by the role *hasHead*
to some person.
- The categories *President*, *Monarch* and *Mayor* are subcategories
of the category *Person*.
- Everything in the category *ConstitutionalMonarchy* is related
by the role *hasHead* to only things in *Monarch*.
- Everything in the category *City* is related
by the role *hasHead* to only things in *Mayor*.
- *'NL'* is a country, and is a constitutional monarchy.
- *'NL'* has as head *'WillemAlexander'*.
- *'NL'* has as capital *'Amsterdam'*.
- *'Amsterdam'* has as head *'Femke'*.

*Assignment (continued):*
For each of the following statements, (1) express them as a
general concept inclusion or assertion in ALC,
(2) answer whether they follow from the knowledge base that you constructed,
and (2a) if so, explain why,
and (2b) if not, give a different ALC statement that you could add to the knowledge
base after which the statement does follow from it (and such that the knowledge base
remains consistent, i.e., there is at least one interpretation that satisfies
the knowledge base after adding this statement).
- Countries that are a republic cannot have a mayor as head.
- *'Femke'* is a mayor.
- *'NL'* is not a republic.
- *'WillemAlexander'* is not a mayor.

*Remarks:*
- Make sure that you don't get fooled by the intuitive names for the different
concepts that I gave you (and the real-world knowledge that you have about
real-world categories that have the same name). Stick to the pieces of knowledge
that I gave you, and make sure that you verify what follows from them
(or rather: their expressions in ALC).

---

## Assignment 2 (&star;): encoding 3SAT into ALC satisfiability

The class 3CNF consists of all propositional logic formulas &varphi;
in conjunctive normal form (CNF) where each clause of &varphi;
contains at most three literals.
The problem 3SAT is the problem of deciding whether a given propositional
logic formula &varphi; in 3CNF is satisfiable.

In this assignment, you will show how the problem of 3SAT
can efficiently be encoded into the
problem of ALC concept satisfiability.
In the problem of *ALC concept satisfiability* you are given a (complex)
concept *C* in the description logic ALC, and the question is to decide if there
exists an interpretation *I = (&Delta;<sup>I</sup>,&bullet;<sup>I</sup>)*
such that *C<sup>I</sup> &ne; &emptyset;*.
For example, the concept *C = A &sqcap; &not; A* is not satisfiable,
because every interpretation *I* must set *C<sup>I</sup> = &emptyset;*,
but the concept *C = A &sqcap; B* is satisfiable,
because the interpretation *I = (&Delta;<sup>I</sup>,&bullet;<sup>I</sup>)*
with *&Delta;<sup>I</sup> = {1}* and *A<sup>I</sup> = B<sup>I</sup> = {1}*
assigns to *C<sup>I</sup> = (A &sqcap; B)<sup>I</sup> = {1}* a non-empty set.

*Assignment:* Give an efficient encoding of 3SAT into ALC concept satisfiability.
That is, describe an algorithm, that takes less than exponential time,
that takes as input a 3CNF formula &varphi;,
and that produces an ALC concept *C<sub>&varphi;</sub>*
for which there exists an interpretation *I*
such that *(C<sub>&varphi;</sub>)<sup>I</sup> &ne; &emptyset;* if and only if &varphi; is satisfiable.

*Remarks:*
- Make sure to argue why the constructed concept *C<sub>&varphi;</sub>*
is satisfiable if and only if &varphi; is satisfiable.

*Hints:*
- For a 3CNF formula with propositional variables *x<sub>1</sub>,...,x<sub>n</sub>*,
use concept names *A<sub>1</sub>,...,A<sub>n</sub>*
to construct the complex concept *C<sub>&varphi;</sub>*.
- Find a way to translate disjunction, conjunction and negation in propositional logic to operators in ALC. There is a solution that involves a mapping that (1) maps propositional variables to concepts, and (2) maps the logical operators in the propositional logic formula to operators in ALC, and combines these two to construct *C<sub>&varphi;</sub>*.

---

## Assignment 3 (&star;): knowledge base with only exponential models

Some ALC knowledge bases have interpretations *I* that satisfy them
with a small domain, and some only have satisfying interpretations
whose domain is very large.
In this exercise, you will construct knowledge bases that only
have satisfying interpretations of exponential size.

*Assignment:* Specify a family of ALC knowledge bases *KB<sub>1</sub>,KB<sub>2</sub>,...*,
one for each positive integer *n &in; {1,2,3,...}*,
such that for each *n* the knowledge base *KB<sub>n</sub>* it holds that
there are only interpretations *I* that satisfy all statements in the knowledge base
whose domain *&Delta;<sup>I</sup>* is of size at least *2<sup>n</sup>*
(and moreover, there is at least one such interpretation *I*).
Make sure that your knowledge bases *KB<sub>n</sub>*
do not grow exponentially with *n*.

*Remarks:*
- It suffices to describe what *KB<sub>n</sub>* consists of for an arbitrary
value *n &in; {1,2,3,...}*. You can do so by starting with
specifying what *KB<sub>1</sub>* looks like. Then specify what *KB<sub>2</sub>* looks like, and *KB<sub>3</sub>*.
Then indicate how this construction generalizes to arbitrary *KB<sub>n</sub>*.
(If you want to directly start by specifying *KB<sub>n</sub>* for an arbitrary
value of *n*, that is fine too of course.)

*Hints:*
- Use general concept inclusions and assertions to make a TBox and ABox
that enforce that every interpretation contains a binary tree of depth *n*.
Such a binary tree has size *&ge; 2<sup>n</sup>*.
- Start with an assertion *x : A<sub>0</sub>* that will give the tree a root
(namely, object *x* in concept *A<sub>0</sub>*).
- Specify that each object in concept *A<sub>0</sub>* must be related (by role *r*)
to an object in concept *B<sub>1,a</sub> &sqcap; A<sub>1</sub>* and
to an object in concept *B<sub>1,b</sub> &sqcap; A<sub>1</sub>*.
Intuitively, this will be used (in combination with some other general concept inclusions
that you will add) to enforce that the root of the tree will have two children.
- Specify that each object in concept *A<sub>1</sub>* must be related (by role *r*)
to an object in concept *B<sub>2,a</sub> &sqcap; A<sub>2</sub>* and
to an object in concept *B<sub>2,b</sub> &sqcap; A<sub>2</sub>*.
- Keep going (with *A<sub>2</sub>*, *A<sub>3</sub>*, etc),
and generalize this construction to arbitrary depth *n*.
- Add further constraints that force that this really can only be satisfied
by a tree&mdash;and not by a single object, or a path of objects.
(This last step requires some insight.)
  - For this, ensure that if an object is in concept *B<sub>1,a</sub>*, all objects that it is related to (by role *r*) must also be in *B<sub>1,a</sub>*.
  - Similarly for *B<sub>1,b</sub>*.
  - Make sure that *B<sub>1,a</sub>* and *B<sub>1,b</sub>* are disjoint.
  - Do the same for all *i &geq; 2* (i.e., for *B<sub>2,a</sub>, B<sub>2,b</sub>, B<sub>3,a</sub>, B<sub>3,b</sub>, ...*).

---

## Assignment 4 (&star;&star;): show that ALC cannot express number restrictions

In the description logic [ALC](https://en.wikipedia.org/wiki/Description_logic#The_description_logic_ALC)
you can express "existential restriction":
you can express concepts such as *(&exist; r. C)*, that represent
the set of all objects that are connected by relation *r* to at least
one object in *C*.
In OWL DL you can express "number restrictions":
you can express concepts such as *(&ge; 2 r)*, that represent the set
of all objects that are connected by relation *r* to at least two
different objects.
In this assignment, you will prove that such number restrictions
are not expressible in the logic ALC,
and thus that OWL DL is strictly more expressive than ALC.


*Assignment:* Give a proof that there is no (complex) concept *C* expressible
in the description logic ALC that is logically equivalent to
the expression *(&ge; 2 r)*.
In other words, show that there is no (complex) concept *C* in the logic ALC
that in every interpretation *I* is assigned to the set of all
objects *d* in the domain *&Delta;<sup>I</sup>* of *I* for which it holds that
there are at least two distinct
objects *e<sub>1</sub>,e<sub>2</sub> &in; &Delta;<sup>I</sup>*
(i.e. *e<sub>1</sub> &ne; e<sub>2</sub>*) that are connected to *d*
by *r<sup>I</sup>* (i.e., such that
*(d,e<sub>1</sub>) &in; r<sup>I</sup>* and *(d,e<sub>2</sub>) &in; r<sup>I</sup>*).

*Hints:*
- Find two (particular) interpretations *I<sub>1</sub>* and *I<sub>2</sub>*
such that the OWL DL expression *(&ge; 2 r)* gets assigned to different sets
*S<sub>1</sub>* and *S<sub>2</sub>*
in these interpretations.
- Moreover, do this in such a way that you can find a correspondence between
the subsets of the domains of *I<sub>1</sub>* and *I<sub>2</sub>*
such that every ALC concept *C* gets assigned to corresponding sets of elements
in *I<sub>1</sub>* and *I<sub>2</sub>*.
- Prove this second property by induction (on the structure of concepts *C*).

---

## Evaluation

You get 2.5 point for free.
Each of the first three assignments (1–3) is worth 2.5 points,
and the fourth assignment is worth 1 bonus point.
This gives a total of 11 points that you can get.
Your grade will be the minimum of 10 and the number of points that you get&mdash;in
other words, your grade is the number of points that you get, with a maximum value of 10.

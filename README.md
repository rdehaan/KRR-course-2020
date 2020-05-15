# Symbolic Systems 1 (UvA, MSc AI, June 2020)

Contents:
1. [Topics](#topics)
1. [Examples](#examples)
1. [Homework assignments](#homework-assignments)

---

## Topics

Here is a short overview of the different topics that we will cover in the course,
together with pointers to reading material.

### (A) Problem solving & search

Subtopics:
- Problem solving and search in rational agents
- Propositional logic and SAT solving
- Constraint programming
- Integer linear programming

Reading material:
- Chapters 3, 6 and 7 of [[Russell, Norvig, 2016]](#aima).

### (B) Non-monotonic reasoning and answer set programming

Subtopics:
- Non-monotonic reasoning
- Default logic
- Answer set programming (ASP)
- Problem solving using ASP

Reading material:
- Sections 6.0–6.2 and Chapter 7 of [[Van Harmelen, Lifschitz, Porter, 2008]](#hokr).
- Chapters 2 and 3 of [[Gebser, Kaminski, Kaufmann, Schaub, 2012]](#assip).

### (C) Automated planning

Subtopics:
- Classical planning
- Planning using problem solving (in particular: ASP)
- Extensions of classical planning

Reading material:
- Chapter 10 and Section 11.3 of [[Russell, Norvig, 2016]](#aima).
- Chapter 8 of [[Gebser, Kaminski, Kaufmann, Schaub, 2012]](#assip).

### (D) Description logics and OWL

Subtopics:
- Description logics
- Web Ontology Language (OWL)
- Modelling and reasoning with ontologies

Reading material:
- Sections 12.1–12.2 of [[Russell, Norvig, 2016]](#aima).
- Chapter 3 of [[Van Harmelen, Lifschitz, Porter, 2008]](#hokr).

### References:

<a name="aima"></a>
- **[Russell, Norvig, 2016]**: Stuart Russell, and Peter Norvig. [*Artificial Intelligence: A Modern Approach (3rd Ed.)*](http://aima.cs.berkeley.edu/), Prentice Hall, 2016.
<a name="hokr"></a>
- **[Van Harmelen, Lifschitz, Porter, 2008]**: Frank van Harmelen, Vladimir Lifschitz, and Bruce Porter (Eds.). [*Handbook of Knowledge Representation*](https://dai.fmph.uniba.sk/~sefranek/kri/handbook/)
<a name="assip"></a>
- **[Gebser, Kaminski, Kaufmann, Schaub, 2012]**: Martin Gebser, Roland Kaminski, Benjamin Kaufmann, and Torsten Schaub. [*Answer Set Solving in Practice*](https://potassco.org/book/), Morgan & Claypool, 2012.

---

## Examples

Here are some notebooks that illustrate how to use various of the techniques that we cover in the course in Python.

- How to call solvers for different search problems from Python:
  - [SAT solving in Python](examples/sat.ipynb)
  - [ASP solving in Python](examples/asp.ipynb)
  - [CSP solving in Python](examples/csp.ipynb)
  - [ILP solving in Python](examples/ilp.ipynb)
- [A short guide to answer set programming (using clingo and Python)](examples/answer-sets.ipynb)

---

## Homework assignments

- [Assignment 1](hw1/assignment.md) (programming)
- Assignment 2
  - *Coming..*
- [Assignment 3](hw3/assignment.md) (programming)
  - *Coming..*
- Assignment 4
  - *Coming..*

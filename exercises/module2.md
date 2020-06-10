# Exercises related to Non-Monotonic Reasoning and Answer Set Programming

These are exercise questions about *non-monotonic reasoning and answer set programming* that you can use
to get a better understanding of the material related to this topic.
The solutions to these exercise questions are not published here, but you are free
to ask about the solutions (e.g., on the [course Canvas page](https://canvas.uva.nl/courses/10768))
if you get stuck and you are free to discuss these exercise questions and their solutions
with other students in the course.

Moreover, these exercise questions are indicative of the type of questions that
you can expect on the final exam.

---

## Exercise 2.1: Strong Equivalence of Answer Set Programming

### Exercise 2.1.a

Consider the following two logic programs *P<sub>1</sub>* and *P<sub>2</sub>*.
Are these strongly equivalent
(see Definition 7.3.10 in [[Van Harmelen, Lifschitz, Porter, 2008]](https://github.com/rdehaan/KRR-course#hokr))?
If so, explain why this is the case.
If not, give a program *P* such
that *P &cup; P<sub>1</sub>*
and *P &cup; P<sub>2</sub>* have different answer sets.

The program *P<sub>1</sub>*:
```
a :- b.
b :- c.
c :- a.
```

The program *P<sub>2</sub>*:
```
a :- b.
b :- a.
a :- c.
c :- a.
```

### Exercise 2.1.b

Consider the following two logic programs *P<sub>1</sub>* and *P<sub>2</sub>*.
Are these strongly equivalent
(see Definition 7.3.10 in [[Van Harmelen, Lifschitz, Porter, 2008]](https://github.com/rdehaan/KRR-course#hokr))?
If so, explain why this is the case.
If not, give a program *P* such
that *P &cup; P<sub>1</sub>*
and *P &cup; P<sub>2</sub>* have different answer sets.

The program *P<sub>1</sub>*:
```
b :- a.
b.
```

The program *P<sub>2</sub>*:
```
b :- a.
:- not b.
```

### Exercise 2.1.c

Consider the following two logic programs *P<sub>1</sub>* and *P<sub>2</sub>*.
Are these strongly equivalent
(see Definition 7.3.10 in [[Van Harmelen, Lifschitz, Porter, 2008]](https://github.com/rdehaan/KRR-course#hokr))?
If so, explain why this is the case.
If not, give a program *P* such
that *P &cup; P<sub>1</sub>*
and *P &cup; P<sub>2</sub>* have different answer sets.

The program *P<sub>1</sub>*:
```
:- a.
:- not a.
```

The program *P<sub>2</sub>*:
```
a :- not b.
b :- not a.
:- a.
:- b.
```

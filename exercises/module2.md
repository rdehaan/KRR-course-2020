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

## Exercise 2.1: Strong Equivalence in Answer Set Programming

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

### Exercise 2.1.d

Let *P<sub>1</sub>* and *P<sub>2</sub>* be two logic programs
that are strongly equivalent
(see Definition 7.3.10 in [[Van Harmelen, Lifschitz, Porter, 2008]](https://github.com/rdehaan/KRR-course#hokr)).
Let *Q<sub>1</sub>* and *Q<sub>2</sub>* also be two logic programs
that are strongly equivalent.

Show that *P<sub>1</sub> &cup; Q<sub>1</sub>*
and *P<sub>2</sub> &cup; Q<sub>2</sub>*
are strongly equivalent.

---

## Exercise 2.2

### Exercise 2.2.a

Give a logic program *P* that has exactly 1024 answer sets.

### Exercise 2.2.b

Give a logic program *P* that has exactly 1000 answer sets.

### Exercise 2.2.c

Give a default theory *(W,D)* that has exactly 1024 extensions.

### Exercise 2.2.d

Give a default theory *(W,D)* that has exactly 1000 extensions.

---

## Exercise 2.3: Modelling non-monotonic reasoning

### Exercise 2.3.a

Model the following (made-up!) scenario of legal reasoning using default logic:
- A suspect should be convicted if they committed a crime.
- Theft is a crime.
- Murder is a crime.
- A suspect should not be convicted if they have immunity from prosecution.
- Immunity from prosecution does not hold if the suspect committed a murder.

To keep things simple (or to oversimplify things),
use the following propositional atoms for this:
`convicted`, `committed_crime`, `committed_theft`, `committed_murder`, `immunity`.
(You may use additional atoms.)

That is, construct a set *D* of defaults, so that:
- Together with *W = {`committed_theft`}*, all extensions of the resulting default
theory contain `convicted`.
- Together with *W = {`committed_theft`,`immunity`}*, all extensions of the resulting default
theory do not contain `convicted`.
- Together with *W = {`committed_murder`}*, all extensions of the resulting default
theory contain `convicted`.
- Together with *W = {`committed_murder`,`immunity`}*, all extensions of the resulting default
theory contain `convicted`.

### Exercise 2.3.b

Model the above scenario of legal reasoning using answer set programming.
Use the same propositional atoms (again, you may use additional atoms).

That is, construct a logic program *P*, so that:
- All answer sets of *P &cup; {`committed_theft.`}* contain `convicted`.
- All answer sets of *P &cup; {`committed_theft.`,`immunity.`}* do not contain `convicted`.
- All answer sets of *P &cup; {`committed_murder.`}* contain `convicted`.
- All answer sets of *P &cup; {`committed_murder.`,`immunity.`}* contain `convicted`.

### Exercise 2.3.c

Model the following (made-up!) scenario of deontic reasoning using default logic:
- One should not do things that are forbidden.
- Speeding is forbidden.
- Fraud is forbidden.
- Forbidden things may be done if they can save lives.
- In an emergency, speeding can save lives.

To keep things simple (or to oversimplify things),
use the following propositional atoms for this:
`should_not_do(speeding)`, `allowed_to_do(speeding)`,
`should_not_do(fraud)`, `allowed_to_do(fraud)`,
`forbidden(speeding)`, `forbidden(fraud)`,
`can_save_lives(speeding)`, `emergency`.
(You may use additional atoms.)

That is, construct a set *D* of defaults
and a set *W<sub>0</sub>* of background facts, so that:
- Together with *W = W<sub>0</sub> &cup; {`emergency`}*,
all extensions of the resulting default
theory contain `forbidden(speeding)`, `forbidden(fraud)`,
`allowed_to_do(speeding)` and `should_not_do(fraud)` and do not
contain `allowed_to_do(fraud)` and `should_not_do(speeding)`.
- Together with *W = W<sub>0</sub> &cup; &emptyset;*,
all extensions of the resulting default
theory contain `forbidden(speeding)`, `forbidden(fraud)`,
`should_not_do(speeding)` and `should_not_do(fraud)` and do not
contain `allowed_to_do(fraud)` and `allowed_to_do(speeding)`.

### Exercise 2.3.d

Model the above scenario of deontic reasoning using answer set programming.
Use the same propositional atoms (again, you may use additional atoms).

That is, construct a logic program *P*, so that:
- All answer sets of *P*
contain `forbidden(speeding)`, `forbidden(fraud)`,
`allowed_to_do(speeding)` and `should_not_do(fraud)` and do not
contain `allowed_to_do(fraud)` and `should_not_do(speeding)`.
- All answer sets of *P &cup; {`emergency.`}*
contain `forbidden(speeding)`, `forbidden(fraud)`,
`should_not_do(speeding)` and `should_not_do(fraud)` and do not
contain `allowed_to_do(fraud)` and `allowed_to_do(speeding)`.

---

## Exercise 2.4

### Exercise 2.4.a

Show that the default theory *(W,D)* with *W = &emptyset;*
and *D = { `T : p / ~q`, `T : q / ~r`, `T : r / ~s` }*
(where `~` denotes negation)
has exactly one extension.

### Exercise 2.4.b

What extensions does the default theory *(W,D)* with *W = { `p -> (~q & ~r)` }*
and *D = { `T : p / p`, `T : q / q`, `T : r / r` }*
(where `~` denotes negation, `&` denotes conjunction, and `->`
denotes logical implication) have?

### Exercise 2.4.c

Show that the default theory *(W,D)* with *W = { `p` }*
and *D = { `p : r / q`, `p : s / ~q` }*
(where `~` denotes negation)
has no extensions.

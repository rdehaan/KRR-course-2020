# Exercises related to Automated Planning

These are exercise questions about *automated planning* that you can use
to get a better understanding of the material related to this topic.
The solutions to these exercise questions are not published here, but you are free
to ask about the solutions (e.g., on the [course Canvas page](https://canvas.uva.nl/courses/10768))
if you get stuck and you are free to discuss these exercise questions and their solutions
with other students in the course.

Moreover, these exercise questions are indicative of the type of questions that
you can expect on the final exam.

---

## Exercise 3.1: Encoding 3SAT into planning

### Exercise 3.1.a

The class 3CNF consists of all propositional logic formulas &varphi;
in conjunctive normal form (CNF) where each clause of &varphi;
contains at most three literals.
The problem 3SAT is the problem of deciding whether a given propositional
logic formula &varphi; in 3CNF is satisfiable.

Show how the problem of 3SAT can efficiently be encoded into the
problem of finding whether a given planning problem has a plan.
That is, describe an algorithm, that takes less than exponential time,
that takes as input a 3CNF formula &varphi;,
and that produces a planning problem for which there exists a
sequence of actions that achieves the goal when applied to the initial state
if and only if &varphi; is satisfiable.

*Hint:*
- For a 3CNF formula with propositional variables *x<sub>1</sub>,...,x<sub>n</sub>*
and clauses *c<sub>1</sub>,...,c<sub>m</sub>*, create a planning problem that uses
propositions `X(1),...,X(n),Y(1),...,Y(n),C(1),...,C(m)`.

---

## Exercise 3.2: Modelling

### Exercise 3.2.a

Consider the following planning scenario.
There are two drones on a 4x4 grid.
Each location of the grid either contains (i) a warehouse, (ii) a delivery location, or (iii) nothing.
Moreover, above each location on the grid can be at most one drone at the same time.
The drones can move to adjacent locations on the grid.
If the drone is above a warehouse, it can pick up a package.
If the drone is above a delivery location, it can deliver a package (if it is carrying one).
Each drone can carry at most one package at a time.
All packages are identical.
The warehouse has an unlimited supply of packages.
The (initial) setup is as follows (where every cell contains nothing, unless specified otherwise):
- Cell (0,0): a warehouse and above it a drone
- Cell (0,1): above it a drone
- Cell (1,2): a delivery location
- Cell (2,1): a delivery location
- Cell (3,3): a delivery location

The goal is to have delivered exactly package at each delivery location.

Show how to model this scenario in the PDDL planning language
(as used in [[Russell, Norvig, 2016]](https://github.com/rdehaan/KRR-course#aima)).

---

## Exercise 3.3: Planning with two (or more) goals

### Exercise 3.3.a

Consider the following general variant of the classical planning setup.
You have an initial state *I*, and a set *A* of actions (each deterministic, with a precondition and an effect),
specified in the PDDL planning language (as used in [[Russell, Norvig, 2016]](https://github.com/rdehaan/KRR-course#aima)).
In addition to this, you get two goals *G<sub>1</sub>* and *G<sub>2</sub>*, both consisting of a set of statements.
In other words, the only difference with the typical classical planning setup is that instead of a single *G* specifying
the goals, you have two: *G<sub>1</sub>* and *G<sub>2</sub>*.
The task in this setting is to find a sequence of actions such that for both *G<sub>1</sub>* and *G<sub>2</sub>*
it holds that they achieved at some point. In other words, if you apply the sequence of actions to the initial state,
you get a resulting sequence of states, and in (at least) one of these states *G<sub>1</sub>* is achieved,
and in (at least) one of these states *G<sub>2</sub>* is achieved.

Show how you can model this scenario with two goal specifications, *G<sub>1</sub>* and *G<sub>2</sub>*,
in the classical setting with only one goal specification *G*.
In other words, describe how to make changes to *I*, *A*, *G<sub>1</sub>* and *G<sub>2</sub>*,
so that you get a classical planning problem, for which there exists a plan (that achieves *G*)
if and only if for the 'double-goal' planning problem there exists a sequence of actions that achieves
*G<sub>1</sub>* and *G<sub>2</sub>* (not necessarily at the same time, and in any order).

*Hints:*
- Use additional statements such as `Achieved(Goal1)` and `Achieved(Goal2)` that are false in the initial state.
- Add actions that can be used to make these statements true (under the right conditions).
- Specify the 'unified' goal *G* using these statements `Achieved(Goal1)` and `Achieved(Goal2)`.

### Exercise 3.3.b

Consider the same question as in Exercise 3.3.a, with the difference that *G<sub>1</sub>*
must be achieved not later than *G<sub>2</sub>*.
In other words, the modified planning setup concerns the task of finding a sequence of
actions such that:
- if you apply the sequence of actions to the initial state,
you get a resulting sequence of states *s<sub>0</sub>,...,s<sub>m</sub>*,
- there is a state *s<sub>i</sub>* in this sequence *s<sub>0</sub>,...,s<sub>m</sub>*
in which *G<sub>1</sub>* is achieved, and
- there is a state *s<sub>j</sub>* *s<sub>0</sub>,...,s<sub>m</sub>*
with *i &le; j* in which *G<sub>2</sub>* is achieved.

Show how you can model this scenario with two goal specifications,
*G<sub>1</sub>* and *G<sub>2</sub>*,
in the classical setting with only one goal specification *G*.

### Exercise 3.3.c

Consider the questions of Exercises 3.3.a and 3.3.b,
but then generalized to more than two goals: *G<sub>1</sub>, ..., G<sub>k</sub>*.
Show how to answer the questions of Exercises 3.3.a and 3.3.b
for an arbitrary number *k* of goal specifications.

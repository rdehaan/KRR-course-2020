# Exercises related to Problem Solving and Search

These are exercise questions about *problem solving and search* that you can use
to get a better understanding of the material related to this topic.
The solutions to these exercise questions are not published here, but you are free
to ask about the solutions (e.g., on the [course Canvas page](https://canvas.uva.nl/courses/10768))
if you get stuck and you are free to discuss these exercise questions and their solutions
with other students in the course.

Moreover, these exercise questions are indicative of the type of questions that
you can expect on the final exam.

---

## Exercise 1.1: DPLL

### Exercise 1.1.a

Show that the DPLL algorithm decides satisfiability of the
following propositional logic formula &varphi; in CNF
with only using unit propagation and pure literal elimination
(and thus without branching).

&varphi; consists of the following clauses:
```
(~x4 OR ~x5 OR ~x6)
(~x1 OR x2 OR x4)
(x4)
(~x4 OR x5)
(x7 OR x10)
(x1 OR x2)
(~x5 OR ~x7 OR ~x8)
(x2 OR ~x3)
(~x10)
(~x4 OR ~x5 OR x6 OR ~x7 OR x8 OR x9)
```

---

## Exercise 1.2: Resolution

### Exercise 1.2.a

Show how the resolution algorithm can be used to show
that &varphi; &models; &psi;,
where &varphi; and &psi; are the following propositional formulas.

&psi; is the literal `x4` and
&varphi; is the CNF formula that consists of the following clauses:
```
(x1 OR x2 OR x3 OR x4)
(x1 OR x2 OR ~x3 OR x4)
(x1 OR ~x2 OR x3 OR x4)
(x1 OR ~x2 OR ~x3 OR x4)
(~x1 OR x2 OR x3 OR x4)
(~x1 OR x2 OR ~x3 OR x4)
(~x1 OR ~x2 OR x3 OR x4)
(~x1 OR ~x2 OR ~x3 OR x4)
```

---

## Exercise 1.3: Encoding 3SAT

## Exercise 1.3.a

The class 3CNF consists of all propositional logic formulas &varphi;
in conjunctive normal form (CNF) where each clause of &varphi;
contains at most three literals.
The problem 3SAT is the problem of deciding whether a given propositional
logic formula &varphi; in 3CNF is satisfiable.

Show how the problem of 3SAT can efficiently be encoded into the
problem of Integer Linear Programming (ILP).
That is, describe an algorithm, that takes less than exponential time,
that takes as input a 3CNF formula &varphi;,
and that produces an integer linear program *P* that has a feasible
solution if and only if &varphi; is satisfiable.

---

## Exercise 1.4: CSP with binary variables and AllDifferent constraints

### Exercise 1.4.a

Consider the restricted variant of the constraint satisfaction
problem (CSP), where:
- Each variable has domain {0,1}
- The only constraints are *AllDifferent* constraints, i.e., constraints
where the relation consists of all pairs *(v<sub>1</sub>,...,v<sub>n</sub>)* such that
for each *1 &leq; i < j &leq; n* it holds that *v<sub>i</sub> &ne; v<sub>j</sub>*.

Show that there is an efficient (polynomial-time) algorithm that for each
CSP instance *I* that adheres to these restrictions decides whether or not *I*
has a solution&mdash;and if *I* has a solution, it outputs a solution for *I*.

---

## Exercise 1.5: Encoding MAX2SAT

### Exercise 1.5.a

The class 2CNF consists of all propositional logic formulas &varphi;
in conjunctive normal form (CNF) where each clause of &varphi;
contains at most two literals.
The problem MAX2SAT is the following problem.
You are given as input a propositional logic formula &varphi; in 2CNF.
The task is to find a truth assignment &alpha; to the variables in &varphi;
that satisfies as many clauses of &varphi; as possible,
i.e., such that there is no &alpha;' that satisfies more clauses in &varphi;
than &alpha; does.

Show how to encode the problem MAX2SAT into answer set programming (ASP),
where you are allowed to use optimization statements (e.g., `#maximize { ... }.`)
That is, describe an algorithm, that takes less than exponential time,
that takes as input a 2CNF formula &varphi;,
and that produces an answer set program *P* whose optimal answer sets
correspond exactly to the truth assignments &alpha; that satisfy a maximal
number of clauses of &varphi;.

---

## Exercise 1.6

### Exercise 1.6.a

Show that the following linear program *P* has a feasible non-integer solution,
and no feasible integer solution.
The program contains the variables *x<sub>1</sub>*, *x<sub>2</sub>* and *x<sub>3</sub>*,
and the following linear inequalities:
```
x1 >= 0
x1 <= 1
x2 >= 0
x2 <= 1
x3 >= 0
x3 <= 1
2*x1 + 3*x2 + 5*x3 <= 6
2*x1 + 3*x2 + 5*x3 >= 6
```

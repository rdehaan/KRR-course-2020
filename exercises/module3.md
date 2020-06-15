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

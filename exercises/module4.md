# Exercises related to Description Logics and OWL

These are exercise questions about *description logics and OWL* that you can use
to get a better understanding of the material related to this topic.
The solutions to these exercise questions are not published here, but you are free
to ask about the solutions (e.g., on the [course Canvas page](https://canvas.uva.nl/courses/10768))
if you get stuck and you are free to discuss these exercise questions and their solutions
with other students in the course.

Moreover, these exercise questions are indicative of the type of questions that
you can expect on the final exam.

---

## Exercise 4.1: Equivalent descriptions in ALC

### Exercise 4.1.a

Two general concept inclusions (GCIs) *G<sub>1</sub>* and *G<sub>2</sub>*
are *equivalent* if
for every interpretation *I* it holds
that *G<sub>1</sub>* is satisfied by *I*
if and only if *G<sub>2</sub>* is satisfied by *I*.

Show that the following two GCIs are equivalent, for any concepts *C* and *D*:
- *C &sqsubseteq; &not;D*
- *C &sqcap; D &sqsubseteq; &bot;*

### Exercise 4.1.b

Two concepts *C<sub>1</sub>* and *C<sub>2</sub>*
are *equivalent* if
for every interpretation *I* it holds
that *(C<sub>1</sub>)<sup>I</sup> = (C<sub>2</sub>)<sup>I</sup>*.

Show that the following two concepts are equivalent, for any concept *C*:
- *(&exist; r. C)*
- *(&not;&forall; r. (&not;C))*

### Exercise 4.1.c

Show that the following two concepts are equivalent, for any concepts *C* and *D*:
- *(C &sqcap; D)*
- *&not;((&not;C) &sqcup; (&not;D))*

### Exercise 4.1.d

Show that the following two GCIs are equivalent, for any concepts *C*, *D* and *E*:
- *C &sqcap; D &sqsubseteq; &exist; r. E*
- *&not;((&not;C) &sqcup; (&not;D)) &sqsubseteq; &not;&forall; r. (&not;E)*

---

## Exercise 4.2: Valid concept inclusions

### Exercise 4.2.a

For each of the following GCIs, answer the following question.
Is the GCI satisfied by every interpretation *I*?
If so, explain why.
If not, give an example of an interpretation *I*
that does not satisfy it.
- *&forall; r. (A &sqcap; B) &sqsubseteq; (&forall; r. A) &sqcap; (&forall; r. B)*
- *(&forall; r. A) &sqcap; (&forall; r. B) &sqsubseteq; &forall; r. (A &sqcap; B)*
- *&forall; r. (A &sqcup; B) &sqsubseteq; (&forall; r. A) &sqcup; (&forall; r. B)*
- *(&forall; r. A) &sqcup; (&forall; r. B) &sqsubseteq; &forall; r. (A &sqcup; B)*
- *&exist; r. (A &sqcap; B) &sqsubseteq; (&exist; r. A) &sqcap; (&exist; r. B)*
- *(&exist; r. A) &sqcap; (&exist; r. B) &sqsubseteq; &exist; r. (A &sqcap; B)*
- *&exist; r. (A &sqcup; B) &sqsubseteq; (&exist; r. A) &sqcup; (&exist; r. B)*
- *(&exist; r. A) &sqcup; (&exist; r. B) &sqsubseteq; &exist; r. (A &sqcup; B)*

---

## Exercise 4.3

### Exercise 4.3.a

Consider the TBox consisting of the following GCIs:
- *&top; &sqsubseteq; A*
- *A &sqsubseteq; &forall; r. &not;A*

Do there exist interpretations *I* that satisfy this TBox?
If so, give an example of such an interpretation *I*,
and explain what interpretations *I* satisfying this TBox look like.
If not, explain why not.

### Exercise 4.3.b

Consider the TBox consisting of the following GCIs:
- *A &sqsubseteq; &not;A*
- *&not;B &sqsubseteq; B*

Do there exist interpretations *I* that satisfy this TBox?
If so, give an example of such an interpretation *I*,
and explain what interpretations *I* satisfying this TBox look like.
If not, explain why not.

### Exercise 4.3.c

Consider the TBox consisting of the following GCIs:
- *&top; &sqsubseteq; &exist; r.&top;*
- *&top; &sqsubseteq; &forall; r.&not; A*

Do there exist interpretations *I* that satisfy this TBox?
If so, give an example of such an interpretation *I*,
and explain what interpretations *I* satisfying this TBox look like.
If not, explain why not.

### Exercise 4.3.d

Consider the TBox consisting of the following GCIs:
- *A &sqsubseteq; &not;A*
- *B &sqsubseteq; &exist; r. A*

Do there exist interpretations *I* that satisfy this TBox?
If so, give an example of such an interpretation *I*,
and explain what interpretations *I* satisfying this TBox look like.
If not, explain why not.

### Exercise 4.3.e

Consider the TBox consisting of the following GCIs:
- *A &sqsubseteq; &not;A*
- *&top; &sqsubseteq; &exist; r. A*

Do there exist interpretations *I* that satisfy this TBox?
If so, give an example of such an interpretation *I*,
and explain what interpretations *I* satisfying this TBox look like.
If not, explain why not.

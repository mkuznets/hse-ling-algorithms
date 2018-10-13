
# Theory of Algorithms (Fall 2018)

An algorithms course for undergraduates in [fundamental and computational linguistics](https://www.hse.ru/en/ba/ling/) at HSE.

Previous versions: [[Spring 2017]](https://github.com/mkuznets/hse-ling-algorithms/tree/2017-spring) [[Spring 2018]](https://github.com/mkuznets/hse-ling-algorithms/tree/2018-spring)

# Useful Resources

* Preliminaries:
  * Eric Lehman et al. *[Mathematics for Computer Science](https://courses.csail.mit.edu/6.042/spring18/mcs.pdf)*
  * Margaret M. Fleck *[Building Blocks for Theoretical Computer Science](http://mfleck.cs.illinois.edu/building-blocks/)*
  * Bruce Mills *Theoretical Introduction to Programming*
  * Graham, Knuth, Patashnik *Concrete Mathematics*

* Algorithms and Data Structures:
  * Pat Morin *[Open Data Structures](http://opendatastructures.org)*
  * **CLRS:** Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein *Introduction to Algorithms*, 3rd edition, 2009
  * Steven Skiena *Algorithm Design Manual* (2nd edition, 2008)

# Schedule

| Date      	| Type  	| Content, references                                                                                                                                                                                                                                                           	|
|-----------	|-------	|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Mon 03/09 	| 2×S   	| Course introduction                                                                                                                                                                                                                                                           	|
| Fri 07/09 	| L     	| Proofs: propositions; axioms; inference; common proof patterns: direct, contrapositive, if and only if, cases, contradiction, disproof; induction.                                                                                                                            	|
| Mon 10/09 	| 2×S   	| Proofs recitation. Examples of proof problems.                                                                                                                                                                                                                                	|
| Fri 14/09 	| L     	| Cancelled                                                                                                                                                                                                                                                                     	|
| Mon 17/09 	| 2×S   	| Positional number systems: definition, base conversion, special cases for binary and hexidecimal. Number theory: divisibility, greatest common divisor, Euclid's algorithm and its extension.                                                                                 	|
| Fri 21/09 	| 2×S+L 	| Number theory cont’d: primes, unique factorisation, modular arithmetic, inverses in Z/nZ, relative primality, Euler's theorem, Fermat's little theorem, RSA encryption.                                                                                                       	|
| Mon 24/09 	|       	| Moved to 21/09                                                                                                                                                                                                                                                                	|
| Fri 28/09 	| L     	| Algorithm analysis: RAM model, computational resources. Time complexity: expression as a function of input size, worst-cast and expected case. Abstracting from the implementation. The problem of complexity estimation and comparison.                                      	|
| Mon 01/10 	| 2S    	| Algorithm analysis cont’d: asymptotic notation, Big Theta, O, Omega. Set theory detour: sequences, Cartesian product, binary relations, equivalence relations and partial orders. Comparison of functions: Big O and Ω as partial orders on equivalence classes induced by Θ. 	|
| Fri 05/10 	| L     	| Algorithm analysis cont’d: common complexity functions with examples. Translating loops into sums when determining time-complexity. Arithmetic and other common series.                                                                                                       	|
| Mon 08/10 	|       	| Moved to 12/10                                                                                                                                                                                                                                                                	|
| Fri 12/10 	| 2×S+L 	| ...                                                                                                                                                                                                                                                                           	|

# Course Outline

## Theoretical Preliminaries

Proof techniques:
* direct,
* indirect,
* contradiction,
* exhaustive case analysis,
* and induction (especially “strong” and “structural” induction).
Lecture 0 requires induction, and whenever Lecture n − 1 requires induction, so does Lecture n.

Discrete mathematics:
* High-school algebra,
* logarithm identities,
* naive set theory,
* Boolean algebra,
* first-order predicate logic,
* sets,
* functions,
* equivalences,
* partial orders,
* modular arithmetic,
* recursive definitions,
* trees (as abstract objects, not data structures),
* graphs.

Basic algorithm analysis:
* Asymptotic notation (o, O, Θ, Ω, ω),
* translating loops into sums and recursive calls into recurrences,
* evaluating simple sums and recurrences.

Elementary discrete probability:
* uniform vs non-uniform distributions,
* expectation,
* conditional probability,
* linearity of expectation,
* independence.

Iterative programming concepts:
* variables,
* conditionals,
* loops,
* indirection (addresses/ pointers/references),
* subroutines,
* recursion.
I do not assume fluency in any particular programming language, but I do assume experience with at least one language that supports indirection and recursion.

## Data Types and Structures

Fundamental abstract data types:
* scalars,
* sequences,
* vectors,
* sets,
* stacks,
* queues,
* priority queues,
* dictionaries.


Fundamental data structures:
* arrays,
* linked lists (single and double, linear and circular),
* binary search trees,
* at least one balanced binary search tree (AVL trees, red-black trees, treaps, skip lists, splay trees, etc.),
* binary heaps,
* hash tables,
* and most importantly, the difference between this list and the previous list.


## Algorithms

Fundamental algorithmic problems:
* sorting
* searching
* enumeration.

Fundamental algorithms:
* elementary arithmetic,
* sequential search,
* binary search,
* comparison-based sorting (selection, insertion, merge-, heap-, quick-),
* radix sort,
* pre- /post-/inorder tree traversal,
* breadth- and depth-first search (at least in trees),
* and most importantly, the difference between this list and the previous list.

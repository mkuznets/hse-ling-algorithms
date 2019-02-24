
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
| Fri 12/10 	| 2×S+L 	| Iterative programming concepts: variables, call stack, indirection. Abstract data types: definition, List (incl. Stack and Queue), Unordered Set (incl. Dictionary), Sorted Set. Data structures: static array, strings (character encodings, Unicode)                        	|
| Mon 15/10 	| 2S    	| Array: dynamic array, amortised complexity, multidimentional array in memory (matrices, row- and column-major orders)                                                                                                                                                         	|
| Fri 19/10 	| L     	| Array cont'd: space-efficient dynamic array, implementations of queue (circular buffer, two dynamic arrays), accounting method for proving amortised complexity. Linked lists (singly, doubly).                                                                               	|
| Mon 29/10 	| 2S    	| Bit array. Lookup table. Hash-table: dealing with collisions, chaining, open-addressing (linear probing, double hashing). Multiplicative hash as an example of hash function.                                                                                                 	|
| Fri 02/11 	| L     	| Free tree: definitions. Binary tree. Proof of relations between the number of nodes, leaves, and height of a binary tree. Number of leaves in a nearly complete tree.                                                                                                         	|
| Fri 09/11 	| L     	| Binary search tree (BST): traversals (pre-, post-, in-order, breadth-first), min/max nodes, basic recursive algorithms (computing the number of leaves and height). Heap: properties, algorithm of building max-heap.                                                         	|
| Mon 12/11 	| 2S    	| General problem of sorting. Comparison sort. Insertion sort. Selection sort. Heapsort. Divide-and-conquer paradigm. Mergesort. Master theorem. Quicksort. Selection problem (finding the kth smallest number in an array). Quickselect. Non-comparison sort: counting sort.   	|
| Fri 16/11 	| L     	| Cancelled                                                                                                                                                                                                                                                                     	|
| Mon 19/11 	| 2S    	| General problem of searching: databases, indexes for exact and range queries. Insertion and deletion to binary search tree. Self-balancing trees. Red-black tree: definition, proof of logarithmic height, rotations, algorithm of insertion.                                 	|
| Fri 23/11 	| L     	| Designing our own database: hash indexes, compaction, SSTables.                                                                                                                                                                                                               	|
| ??? 	        | ???     	| Graphs: definitions, data structures (adjacency matrix, adjacency lists), depth-/breadth-first search, topological sort. Disjoint-set data structure (Union-Find). Minimum spanning tree (Kruskal, Prim). Shortest path problem (Bellman–Ford, Dijkstra).                         |

# Theory of Algorithms (Spring 2020)

An algorithms course for undergraduates in [fundamental and computational linguistics](https://www.hse.ru/en/ba/ling/) at HSE.

Previous versions: [[Spring 2017]](https://github.com/mkuznets/hse-ling-algorithms/tree/2017-spring) [[Spring 2018]](https://github.com/mkuznets/hse-ling-algorithms/tree/2018-spring) [[Autumn 2018]](https://github.com/mkuznets/hse-ling-algorithms/tree/2018-fall)

# Curriculum

* **Data and Computing**: computation model; integers; floating-point; bitwise operations; programming languages; arrays; pointers.
* **Algorithm Analysis:** running time: worst-, average-, and expected cases; asymptotic notation and analysis; amortised analysis.
* **Data Structures:** dynamic array; multidimensional arrays; linked lists; stacks; queues; priority queues and heaps.
* **Sorting (and The Importance of Being Sorted):** binary search; merging sorted sequences; comparison sorts: selection sort, heapsort, mergesort, quicksort; non-comparison sorts: counting sort, radix sort.
  * [C++Now 2017: M. Skarupke “Generalizing and optimizing radix sort"](https://www.youtube.com/watch?v=zqs87a_7zxw)
* **Trees:** definitions and properties; binary trees; binary search trees: walks, search, min, max, successor, predecessor, insert, delete.
* **Hashing:** hash functions; hash tables; collision resolution: chaining, open addressing.
* **Dictionaries and Sets:** lookup tables; bit arrays; limitations of hash tables; balanced search trees; skip lists; bloom filters.
* **Dynamic Programming:** 'optimised recursion': top-down and bottom-up; text segmentation; edit distance; longest increasing subsequence.
* **Graphs:** definitions; data structures: adjacency matrix, adjacency lists; depth- and breadth-first search; topological sort; disjoint-set (union-find); minimum spanning tree: Kruskal, Prim; shortest path problem: Bellman-Ford, Dijkstra.
* **Strings:** edit-friendly string: gap buffers, ropes; edit distance on multiple documents; string matching: Knuth-Morris-Pratt, Boyer-Moore; prefix trees (tries); suffix trees.

# Lecture Notes

Click on the badge to download the latest version of the document:

[![.pdf](https://mkuznets-latex.s3.eu-west-2.amazonaws.com/algorithms/lecture-notes-badge.svg?rnd=1)](https://mkuznets-latex.s3.eu-west-2.amazonaws.com/algorithms/lecture-notes.pdf)

These notes suppose to fully cover the content of lectures as they are given. However, it is currently a living document in its early draft stage with little proofreading. Mind the gaps and be sure to update regularly. (It is probably best if you bookmark the link and read directly from your browser.)

The LaTeX sources are kept at [mkuznets/latex](https://github.com/mkuznets/latex); the PDF is automatically updated on each commit. Feel free to submit an [issue](https://github.com/mkuznets/latex/issues/new) or a [pull request](https://github.com/mkuznets/latex/pulls) if you notice something out of place (which you will).

# Resources

* Algorithms and Data Structures:
  * **CLRS:** Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest and Clifford Stein *Introduction to Algorithms*, 3rd edition, 2009
  * Steven Skiena *Algorithm Design Manual* (2nd edition, 2008)
  * Pat Morin *[Open Data Structures](http://opendatastructures.org)*

* Go
  * [Tour of Go](https://tour.golang.org)
  * [Packages](https://golang.org/pkg/)

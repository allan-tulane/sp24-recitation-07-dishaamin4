# CMPS 2200 Recitation 10## Answers

**Name:** Disha Amin
**Name:** Zach Hom


Place all written answers from `recitation-07.md` here for easier grading.



- **2)** O(|n| + |m|)

- **4)** The worst case number of times we would have to call "reachable" to see if the graph is connected would be in the case that the graph is a straight line of connected nodes, because each node's neighbors will be reached indepentendly. So, the number of calls to reachable would be n - 1, where n = the number of nodes, until the frontier is empty.

- **5)** O(|n| + |m|)

- **7)** If we switched the representation to an adjacency matrix, the work would be O(n*m), where n = the number of nodes (vertices) in the matrix, as opposed to O(|n| + |m|) work with a graph representation, where n = number of nodes & m = number of edges. 

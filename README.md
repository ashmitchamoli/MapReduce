# 1 Inverted Index
Given a set of documents, create an inverted index, which is a dictionary associating each word with a list of document identifiers where that word appears. The input is a 2-element list: [document id, text], where document id is a string representing a document identifier, and text is a string representing the content of the document. The text consists of space-separated words. The objective is to output the inverted index, where each word is associated with all its unique document identifiers.

## Input Format
- Each line contains two tab-separated elements.
- The first element is a string representing the document id.
- The second element represents the text in that document, consisting of space-separated words.

```
doc1 I love pasta
doc2 Italy is a great country having great Pasta
doc3 I love Italy because Italy has good Pasta
```

## Output format
In the output, each line starts with a word followed by a tab and a list of space-separated document ids associated with that word. The output needs to be sorted by the key (which is the word here)
```
a   doc2
because doc3
country doc2
good    doc3
great   doc2
has doc3
having  doc2
I   doc1 doc3
is  doc2
Italy   doc2 doc3
love    doc1 doc3
Pasta   doc2 doc3
pasta   doc1
```

# 2 Friendships
An ideal friendship is commutative. If I consider you as my friend, then I know that you consider me as your friend.
There are N people in IIITH currently. You are given information about the existing friendships. You wonder for each pair of people, who are the mutual friends. 


## Input Format
Formally, you are given input where each line contains two space-separated integers `u v`, such that `1 ≤ u < v ≤ N`, indicating that u, v are friends. This means that u is a friend of v and vice-versa. It is guaranteed that there won’t be more than $\frac{N\cdot(N-1)}{2}$ number of input lines.

## Output Format
For each pair of people x, y (with x < y) having atleast one mutual friend, you are required to output one line of the form 
```
x y<tab-character><space-separated list of one or more mutual friends of x and y in sorted order>
```
* Note that the order of lines in the output doesn’t matter (since there are multiple reducer tasks). However, in a given line, the value field (i.e. the list of mutual friends) must be sorted.
  
## Sample Test Case
Input:
```
1 2
1 3
2 3
1 5
3 5
1 6
2 6
3 4
2 5
```
Output
```
1 2 3 5 6
1 3 2 5
1 4 3
2 6 1
3 5 1 2
3 6 1 2
4 5 3
5 6 1 2
1 5 2 3
1 6 2
2 3 1 5
2 4 3
2 5 1 3
```
# 3 Finding the Shortest Path to All Nodes
Consider a large-scale graph represented as an adjacency list, where each node has a unique identifier in the form of a positive integer and is connected to other nodes with undirected, unweighted edges (that is, each edge has a weight of 1). 

Your task is to output the shortest distance from node 1 to each node that is at most a distance of 10 from the node 1 using Map-Reduce.

## Input Format
The input will be an adjacency list of the graph. So for each node `x` in the graph, there will be a line of input of the format 
```
x<tab-character><list of neighbours of node x>
```
* Note that the graph is undirected; this means that if node A appears as a neighbour of B, then it is guaranteed that B also appears as a neighbour of A.

## Output Format
For each node `u` that is at a distance of at most 10 from node 1, output a line of the form
```
u<tab-character><shortest-distance-from-node-1>
```
## Sample Test Case
Input:
```
1   2 3 6
2   1 3 4
3   1 2 5
4   2 5
5   3 4
6   1
```
Output:
```
1   0
2   1
4   2
5   2
6   1
3   1
```
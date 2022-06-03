# Graphs
Implementation of a graph data structure, in an adjacency list maner.

## Challenge
Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:
___
#### add node
Arguments: value \
Returns: The added node\
Add a node to the graph
___
#### add edge
Arguments: 2 nodes to be connected by the edge, weight (optional)\
Returns: nothing\
Adds a new edge between two nodes in the graph
If specified, assign a weight to the edge
Both nodes should already be in the Graph
___
#### get nodes
Arguments: none\
Returns all of the nodes in the graph as a collection (set, list, or similar)
___
#### get neighbors
Arguments: node \
Returns a collection of edges connected to the given node\
Include the weight of the connection in the returned collection
___
#### size
Arguments: none\
Returns the total number of nodes in the graph
___

## Approach & Efficiency
The Graph DS is very efficient built on a structure of hashtables we end up with Hashtable lookup times, *0(1)*


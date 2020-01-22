
"""
UNDERSTANDING:

Input Data:
    * ancestorTree of relationships between parents and children....multiple generations

Format of data:
    * List of (parent, child) pairs. 
    * Each individual identified by unique integer ID
    [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

What is being asked:
    Write a function with:
        Takes 2 arguments ==> ancestors, and starting node
        child = input individual
        returns the earlist know ancestor that is farthest id from child 
        if there is more than one tied to child, return lowest numeric ID
        if the child has no parents, return -1.

Example: 
        10
        /
        1   2   4  11
        \ /   / \ /
        3   5   8
        \ / \   \
         6   7   9

    [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
            
    Example input
        6

        1 3
        2 3
        3 6
        5 6
        5 7
        4 5
        4 8
        8 9
        11 8
        10 1
    Example output
            10

Note: 
    one to many relationship of parent to child
    no cycles in the input
    no repeat ancestors
    ID's always positive
    There is no empty inputs
    need to decide between depth-first search or breadth-first search

child = starting_node ==> starting_vertex
ancestor = destination_node ==> destination_vertex

PLAN:
    1. Use depth-first search approach template from ancestorTree.py

"""

from util import  Stack, Graph


ancestor_data = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    ancestorTree = Graph()
    # Iterate through ancestors to find vertices
    # for (parent,child) in ancestors
    for ancestor in ancestors:
        for vert in ancestor:
            ancestorTree.add_vertex(vert)
    # print("Tree", ancestorTree.vertices)

    for ancestor in ancestors:
        ancestorTree.add_edge(ancestor[1], ancestor[0])
    # print("Tree", ancestorTree.vertices)
    
    # default length to check the length of path list against
    longest_path = 1
    # counter for storing storing the last node
    last_node = 0
    # passing the vertices by reference
    ancestor_vert = ancestorTree.vertices
    
    # Iterate through the vertices of the ancestorTree
    for i in ancestor_vert:
        # i = individual nodes/vertices added using add_vert()
        # returns a list of nodes and sets the list to the variable path
        path = ancestorTree.dfs(starting_node, i) 
        # print("path list loop", path)
        
        # If path is not = to None and the length of the path list in greater that longest_path which defaults to the value integer 1
        if path is not None and len(path) > longest_path :
                # set longest_path = length of the path
                longest_path = len(path)
                print("longest_path", longest_path)
                # last node is = to last node/vertice of the longest_path
                last_node = i
                print("last_node", last_node)
        # I was missing that longest_path defaults to 1.
        # If path list is empty and longest_path is set to default of 1
        elif not path and longest_path == 1:
            # print("empty", path)
            # print("elif path", longest_path)
            # set last_node to -1
            last_node = -1
    
    # print("Out of for loop", last_node)
    return last_node


print("function", earliest_ancestor(ancestor_data, 6))

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
    # print("neighbors",ancestorTree.get_neighbors(6))
    # print("Tree", ancestorTree.vertices)
    
    # To use to check the length
    longest_path = 1
    # storing the last node
    last_node = 0
    ancestor_vert = ancestorTree.vertices
    
    for i in ancestor_vert:
        # i = individual node
        # print("depth first",ancestorTree.dfs(starting_node, i), "\n")
        path = ancestorTree.dfs(starting_node, i) #returns a list of nodes
        # print("path loop", path)
        if path is not None and len(path) > longest_path :
                longest_path = len(path)
                print("longest_path", longest_path)
                last_node = i
                print("last_node", last_node)
        elif not path and longest_path == 1:
            print("empty", path)
            print("elif path", longest_path)
            last_node = -1
    
    # print("Out of for loop", last_node)
    return last_node


print("function", earliest_ancestor(ancestor_data, 9))
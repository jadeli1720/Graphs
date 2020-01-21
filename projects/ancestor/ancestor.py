
"""
UNDERSTANDING:

Input Data:
    * Graph of relationships between parents and children....multiple generations

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
    1. Use depth-first search approach template from graph.py

"""

from util import  Stack, Graph 

def earliest_ancestor(ancestors, starting_node):
    # Create a stack 
    stack = Stack()
    # Put the starting point in a list to use as our path
    stack.push([starting_node])
    # Make a set to keep track of where we have been
    visited = set()

    # While there is stuff in the stack
    while stack,size() > 0:
        # Pop the first item
        path = stack.pop()
        # vertex = last item in the path
        node = path[-1]

        # If not visited
        if node not in visited:
            # If the ancestors is in our path
            if node == ancestors:
                return path
            # Add to visited
            visited.add(node)

            # For each edge in the item
            for next_node in Graph.get_neighbors(node):
                new_path = list(path)
                new_path.append(next_node)
                stack.push(new_path)


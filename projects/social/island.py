"""
Once you’ve reviewed the precourse material, take a look at this island_counting problem which we will be going over in today’s guided project:
Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. 

For example:

                island[0][4]
                        |
                        v
islands = [[0, 1, 0, 1, 0],  -> island_list = island[0] --> first full list
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

The 1's grouped together make up island land mass with the 0's being the water/ocean between the land masses
island_counter(islands) # returns 4

UNDERSTAND:

Word relevent to problem(lets us know that we are using a graph):

    * connected --> has edges, connected components
    * array/2d --> graph
    * n,s,e,w --> The nodes to them are the edges
    * binary --> values
    * island/1, islands --> connected components
    * return 1 islands --> number of connected components

What is the value of = islands[0][4] --> y first, then x
            The island[0] refers to the first full list [0, 1, 0, 1, 0]
            island[4] would be the fifth element whose value is 0

            island_list = island[0] --> first full list
            island_list[4] --> 5th element at index 4

"""

islands = [
           [0, 1, 0, 1, 0], 
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0] 
           ]
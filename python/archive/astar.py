# Code obtained from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

"""This module is used for AStar"""

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 # G-cost: Cost to travel from start node to current node
        self.h = 0 # H-cost: Cost to travel from current node to end node
        self.f = 0 # F-cost: Sum of G-cost and H-cost

    # Allow for equality comparision
    # Without def __eq__, a == b would come up false
    def __eq__(self, other):
        return self.position == other.position

def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Return reversed path

def astar(maze, start, end, allow_diagonal_movement = False):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start node and end node objects
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0

    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize open and closed lists
    # Open list is a collection of all generated nodes. These nodes are neighbours of expanded nodes.
    # Closed list is a collection of all expanded nodes. These nodes have already been searched.
    open_list = []
    closed_list = []

    # Add start node to open list
    open_list.append(start_node)

    # Adding a stop condition
    # outer_iterations = 0
    # max_iterations = (len(maze) // 2) ** 2


    # what squares do we search
    adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
    if allow_diagonal_movement:
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

    # Loop until you run out of open list nodes
    while len(open_list) > 0:
        # outer_iterations += 1

        #Get current node
        current_node = open_list[0]
        current_index = 0

        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # if outer_iterations > max_iterations:
        #     # if we hit this point return the path such as it is
        #     # it will not contain the destination
        #     print("giving up on pathfinding too many iterations")
        #     return return_path(current_node)

        # Pop current node from open list and add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Checks for goal
        if current_node == end_node:
            return return_path(current_node)

        # Generate children
        children = []

        for new_position in adjacent_squares: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Ensure node is within range of closest open list node
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Ensure node is useable (no foreign objects)
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Check if child is on closed list:
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # Create f, g, and h cost values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]]

    start = (0, 0)
    end = (8, 8)

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()

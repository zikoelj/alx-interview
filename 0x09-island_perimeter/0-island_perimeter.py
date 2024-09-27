#!/usr/bin/python3
"""
Program to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented in a grid.
    Args:
        grid (list of list of int): A 2D grid representing the island.
    Returns:
        int: The perimeter of the island.
    """
    # Get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the perimeter variable
    per = 0

    # Calculate the perimeter
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                per += 4  # Each cell with 1 contributes 4 units to the per

                # Subtract 2 if the neighboring cell above is also 1
                if i > 0 and grid[i-1][j] == 1:
                    per -= 2

                # Subtract 2 if the neighboring cell to the left is also 1
                if j > 0 and grid[i][j-1] == 1:
                    per -= 2

    return per  # Return the calculated perimeter

"""
Student:  Robin G. Blaine
Date:     December 11, 2017
Class:   _Python Programming

Assignment (Module 6, Data Structures - Chapter 7, Project 9):
	Write a program that solves the maze problem discussed earlier in this chapter.
	You should use the Grid class developed in Chapter 4 in this problem. The
	program should input a description of the maze from a text file at start-up. The
	program then displays this maze, attempts to find a solution, displays the result,
	and displays the maze once more.

Algorithm:
Instantiate a stack
Load the maze from a text file and store it in a grid
Locate the character 'P' on the grid
Push its location onto the stack
While the stack is not empty
    Pop a location (row, column) off the stack
        If the the grid contains 'T' at this location, then
            A path has been found
            Return True
    Else if this location does not contain a dot
        Place a dot in the grid at this location
        Examine the adjacent cells to this one and for for each one that contains a space or "T",
            push its location onto the stack
Return False
"""

from arraystack import ArrayStack

def main():
    """Main function."""
    mazeGrid = loadMaze("maze.txt")
    printMaze(mazeGrid)
    startCoords = findStart(mazeGrid)
    mazeStack = ArrayStack()
    mazeStack.push(startCoords)
    solved = solveMaze(mazeGrid, mazeStack)
    if not solved:
        raise ValueError("Maze not solved.")
    print("Maze solved.")
    printMaze(mazeGrid)

def loadMaze(filename):
    """Loads a maze from a text file and returns it as a list."""
    lyst = []
    readFile = open(filename, 'r')
    for line in readFile:
        lyst.append(line)
    return lyst

def printMaze(maze):
    """Prints the maze."""
    print("\n")
    for row in maze:
        print(row)
    print("\n")
    
def findStart(grid):
    """Finds the location of the character 'P' in the the grid."""
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "P":
                return [row, col]
    raise ValueError("Start position not found.")

def solveMaze(maze, stack):
    """Attempts to solve the maze. Returns True if solved, False otherwise."""
    h = len(maze)
    w = len(maze[0])
    while not stack.isEmpty():
        coords = stack.pop()
        row = coords[0]
        col = coords[1]
        if maze[row][col] == "T":
            printMaze(maze)
            return True
        elif maze[row][col] != ".":
            maze[row] = maze[row][:col] + "." + maze[row][col + 1:]
            if row > 0:
                if maze[row - 1][col] in [" ", "T"]:
                    stack.push([row - 1, col])
            if col > 0:
                if maze[row][col - 1] in [" ", "T"]:
                    stack.push([row, col - 1])
            if row < h - 1:
                if maze[row + 1][col] in [" ", "T"]:
                    stack.push([row + 1, col])
            if col < w - 1:
                if maze[row][col + 1] in [" ", "T"]:
                    stack.push([row, col + 1])
    return False

main()  

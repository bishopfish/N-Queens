import copy

# Produces an n*n empty board; False indicates an empty space, True an occupied space
def board(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(False)
        board.append(row)
    return board

# Produces a graphical representaion of a board        
def draw(board):
    for r in board:
        for s in r:
            if not s:
                print(' [ ] ', end='')
            else:
                print(' [Q] ', end='')
        print('\n')
        
# Returns the total number of Queens on the board  
def count(board):
    totalQueens = 0
    for r in board:
        for s in r:
            if s:
                totalQueens += 1
    return totalQueens
    
# Returns an array of threatened spaces (two-value tuples) on a board
def threatened(board):
    threatened = []
    # Add values to threatened based on board arrangement and count Queens.
    for c1, r in enumerate(board):
        for c2, s in enumerate(r):
            # If space contains a Queen
            if s:
                # Add row to threatened
                for i in range(len(board)):
                    threatened.append((c1, i))
                # Add column to threatened
                for j in range(len(board)):
                    threatened.append((j, c2))
                # Remove Queen's space (added twice)
                threatened.remove((c1,c2))
                # Add diagonals to threatened
                i = 1
                j = 1
                while c1 + i < len(board) and c2 + j < len(board):
                    threatened.append((c1 + i, c2 + j))
                    i += 1
                    j += 1
                i = 1
                j = 1
                while c1 + i < len(board) and c2 - j > -1:
                    threatened.append((c1 + i, c2 - j))
                    i += 1
                    j += 1
                i = 1
                j = 1
                while c1 - i > -1 and c2 + j < len(board):
                    threatened.append((c1 - i, c2 + j))
                    i += 1
                    j += 1
                i = 1
                j = 1
                while c1 - i > -1 and c2 - j > -1:
                    threatened.append((c1 - i, c2 - j))
                    i += 1
                    j += 1
                    
    return threatened


# Generates solutions for a given board. 
def solve(board): 
    
    # List of boards; accumulates solutions.
    solutions = []
    
    # Inner function that performs recursion.
    def solveInner(b):
        # Base case, when n Queens are on board.
        if count(b) == len(b):
            # Checks to see if solution has already been found.
            if b not in solutions:
                solutions.append(b)
        # Add Queen to first non-threatened space on board and run recursion        
        else:
            t = threatened(b)
            for c1, r in enumerate(b):
                for c2, s in enumerate(r):
                    if (c1, c2) not in t:
                        newB = copy.deepcopy(b)
                        newB[c1][c2] = True
                        solveInner(newB)
                    
        
    solveInner(board)    
    
    for b in solutions:
        draw(b)
        print('\n')
    
    print("Total solutions:",len(solutions))
    
def main():    
    
    b = board(8)
    solve(b)
       
    
    
main()
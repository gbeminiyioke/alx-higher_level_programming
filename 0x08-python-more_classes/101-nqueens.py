#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

N must be an integer greater than or equal to 4.

Attributes:
    brd (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize `n`x`n` sized chessboard with 0's."""
    brd = []
    [brd.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in brd]
    return (brd)


def board_deepcopy(brd):
    """Return a copy of a chessboard."""
    if isinstance(brd, list):
        return list(map(brd_deepcopy, brd))
    return (brd)


def get_solution(brd):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(brd)):
        for c in range(len(brd)):
            if brd[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(brd, row, col):
    """X out spots on a chessboard.

    Args:
        brd (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(brd)):
        brd[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        brd[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(brd)):
        brd[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        brd[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(brd)):
        if c >= len(brd):
            break
        brd[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        brd[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(brd):
            break
        brd[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(brd)):
        if c < 0:
            break
        brd[r][c] = "x"
        c -= 1


def recursive_solve(brd, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        brd (list): The current chessboard.
        row (int): The current row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(brd):
        solutions.append(get_solution(brd))
        return (solutions)

    for c in range(len(brd)):
        if brd[row][c] == " ":
            tmp_brd = brd_deepcopy(brd)
            tmp_brd[row][c] = "Q"
            xout(tmp_brd, row, c)
            solutions = recursive_solve(tmp_brd, row + 1, queens + 1, solutions)
            return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    brd = init_brd(int(sys.argv[1]))
    solutions = recursive_solve(brd, 0, 0, [])
    for sol in solutions:
        print(sol)

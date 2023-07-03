#!/usr/bin/python3
"""Solves the nqueens puzzle"""
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at position (row, col)"""
    for i in range(row):
        if board[i][col] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_nqueens(board, row):
    """Solve the n-queens problem using backtracking"""
    if row == N:
        print_solution(board)
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1)
            board[row][col] = 0

def print_solution(board):
    """Print the board configuration as a list of positions of the queens"""
    sol = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                sol.append([i, j])
    print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solve_nqueens(board, 0)

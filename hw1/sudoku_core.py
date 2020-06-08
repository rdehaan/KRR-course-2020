def propagate(sudoku_possible_values,k):
    """
    Carry out constraint propagation (as part of a backtracking search algorithm for solving a sudoku input), by removing possible values for some cells based on the remaining possible values for other cells.

    Parameters:
        sudoku_possible_values (list(list(list(int)))): Data structure with a list of remaining possible values for each cell in the sudoku input.
        k (int): The dimension of the sudoku input.

    Returns:
        (list(list(list(int)))): The data structure sudoku_possible_values after propagation.
    """

    return sudoku_possible_values


def solve_sudoku_SAT(sudoku,k):
    """
    Solve a sudoku input by encoding the problem into SAT, calling a SAT solver, and retrieving the solution for the sudoku input from a satisfying truth assignment given by the SAT solver.

    NOTE: still needs to be implemented. Currently returns None for every input.

    Parameters:
        sudoku (list(list(int))): Sudoku input as list of list of ints, where a 0 indicates that a cell is empty.
        k (int): The dimension of the sudoku input.

    Returns:
        (list(list(int))): The solution to the sudoku, or None if no solution was found.
    """

    return None


def solve_sudoku_CSP(sudoku,k):
    """
    Solve a sudoku input by encoding the problem into CSP, calling a CSP solver, and retrieving the solution for the sudoku input from a solution given by the CSP solver.

    NOTE: still needs to be implemented. Currently returns None for every input.

    Parameters:
        sudoku (list(list(int))): Sudoku input as list of list of ints, where a 0 indicates that a cell is empty.
        k (int): The dimension of the sudoku input.

    Returns:
        (list(list(int))): The solution to the sudoku, or None if no solution was found.
    """

    return None


def solve_sudoku_ASP(sudoku,k):
    """
    Solve a sudoku input by encoding the problem into ASP, calling an ASP solver, and retrieving the solution for the sudoku input from an answer set given by the ASP solver.

    NOTE: still needs to be implemented. Currently returns None for every input.

    Parameters:
        sudoku (list(list(int))): Sudoku input as list of list of ints, where a 0 indicates that a cell is empty.
        k (int): The dimension of the sudoku input.

    Returns:
        (list(list(int))): The solution to the sudoku, or None if no solution was found.
    """

    return None


def solve_sudoku_ILP(sudoku,k):
    """
    Solve a sudoku input by encoding the problem into ILP, calling an ILP solver, and retrieving the solution for the sudoku input from a satisfying assignment given by the ILP solver.

    NOTE: still needs to be implemented. Currently returns None for every input.

    Parameters:
        sudoku (list(list(int))): Sudoku input as list of list of ints, where a 0 indicates that a cell is empty.
        k (int): The dimension of the sudoku input.

    Returns:
        (list(list(int))): The solution to the sudoku, or None if no solution was found.
    """

    return None

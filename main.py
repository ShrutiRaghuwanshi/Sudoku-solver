from copy import deepcopy
#deepcopy as to not change the original problem sudoku.
#shallowcopy will change the original problem as it uses a reference to the object

Grid = [['.', '.', '2', '3'],
        ['.', '.', '.', '.'],
        ['.', '.', '.', '.'],
        ['3', '4', '.', '.']]

#valid elements for solving sudoku
elements = ['1','2','3','4']

def get_rows(new_Grid):
    rows = []
    for r in range(0,4):
        row = {}
        for c in range(0,4):
            row[(r,c)] = new_Grid[r][c]
        rows.append(row)
    return rows

## This cell is only for clarification and it is not part of the original code
print("rows and address")
rows = get_rows(Grid)
for r in rows:
    print(r)

def get_cols(new_Grid):
    cols = []
    for c in range (0,4):
        col = {}
        for r in range(0,4):
            col[(r,c)] = new_Grid[r][c]
        cols.append(col)
    return cols


## This cell is only for clarification and it is not part of the original code
print("rows and address")
cols = get_cols(Grid)
for c in cols:
    print(c)

#first(0,1) for rows range
#second(0,1) for col range
square_indx = [[(0,1),(0,1)],
               [(0,1),(2,3)],
               [(2,3),(0,1)],
               [(2,3),(2,3)]
              ]

def get_squares(new_Grid):
    squares = []
    for sq in range (0,4):
        square = {}
        for r in square_indx[sq][0]:
            for c in square_indx[sq][1]:
                square[(r,c)] = new_Grid[r][c]
        squares.append(square)

    return squares

## This cell is only for clarification and it is not part of the original code
print("square and address")
squares = get_squares(Grid)
for sq in squares:
    print(sq)

#calling functions for getting details
def get_all_related_cells(new_Grid):
    rows = get_rows(new_Grid)
    cols = get_cols(new_Grid)
    squares = get_squares(new_Grid)

    all_vec = squares + rows + cols
    return all_vec

## This cell is only for clarification and it is not part of the original code
print("all grids and address")
all_vec = get_all_related_cells(Grid)
for vector in all_vec:
    print(vector)


# gets the value of next row and col of the present row and col
def get_new_r_c(r, c):
    if c == 3:
        if r == 3:
            new_r = r
            new_c = c
        else:
            new_r = r + 1
            new_c = 0
    else:
        new_r = r
        new_c = c + 1

    return new_r, new_c

## This cell is only for clarification and it is not part of the original code
print(get_new_r_c(0,0))
print(get_new_r_c(0,3))
print(get_new_r_c(1,3))
print(get_new_r_c(2,3))


def get_legal_for_cell(cell_r, cell_c, new_Grid):
    # we dont want to change values that already exist in the sudoku
    if new_Grid[cell_r][cell_c] != '.':
        return [None], [None], [None]


def get_legal_for_cell(cell_r, cell_c, new_Grid):
    # we dont want to change values that already exist in the sudoku
    if new_Grid[cell_r][cell_c] != '.':
        return [None], [None], [None]

    # getting all related cells for solving a box
    map = {}
    all_groups = get_all_related_cells(new_Grid)

    for group in all_groups:
        if (cell_r, cell_c) in group.keys():
            map.update(group)

    exist = []
    for m in map:
        if not map[m] == '.':
            exist.append(map[m])

    rest = list(set(elements) - set(exist))

    return rest, exist, map

## This cell is only for clarification and it is not part of the original code
r = 0
c = 0
legal_for_cell, exist, map = get_legal_for_cell(r, c, Grid)
print(map)
print(exist)
print(legal_for_cell)

def is_complete(new_Grid):
    grid_complete = True
    for r in new_Grid:
        grid_complete = grid_complete and not ('.' in r)
    return grid_complete

def print_grid(new_Grid):
    for item in new_Grid:
        print(item)
    print()


## This cell is only for clarification and it is not part of the original code
print(is_complete(Grid))

## This cell is only for clarification and it is not part of the original code
print_grid(Grid)

## This cell is only for clarification and it is not part of the original code
# Explaining deep copy
from copy import deepcopy
x = [1,2,3]
y = x
z = deepcopy(x)
x[0] = 50
x[2] = 150
x.append(200)
print('x:',x)
print('y:',y)
print('z:',z)


def solve_step_in_sudoko(last_Grid, r, c):
    if is_complete(last_Grid):
        print('Complete:')
        print_grid(last_Grid)
        return 0

    #we are only interested in the first one returned container
    legal_for_cell, _, _ = get_legal_for_cell(r, c, last_Grid)

    for item in legal_for_cell:
        new_Grid = deepcopy(last_Grid)
        if last_Grid[r][c] == '.':
            new_Grid[r][c] = item
        new_r, new_c = get_new_r_c(r, c)

        solve_step_in_sudoko(new_Grid, new_r, new_c)


print('Incomplete:')
print_grid(Grid)
solve_step_in_sudoko(Grid, 0, 0)
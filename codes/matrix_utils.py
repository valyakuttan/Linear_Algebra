# matrix_utils.py
#
# A matrix is a list of it's rows.
# This is a 1x4 matrix [[0, 1, 2, 3, 4]]
# and this is a 4x1 matrix [[0], [1], [2], [3], [4]]

__all__ =['multiply', 'transpose', 'add', 'id', 'zero', 'dimension']

def multiply(m1, m2):
    assert num_cols(m1) == num_rows(m2)
    return [combine_rows(r, m2) for r in m1]

def combine_rows(ws, rs):
    return add_rows(*(scale_row(*z) for z in zip(ws, rs)))

def transpose(m):
    return [list(z) for z in zip(*m)]

def add(m1, m2):
    assert dimension(m1) == dimension(m2)
    return [add_rows(*z) for z in zip(m1, m2)]

def dot(r1, r2):
    assert len(r1) == len(r2)
    return sum(x*y for x, y in zip(r1, r2))

def id(n):
    return [[1 if r == c else 0 for c in range(n)] for r in range(n)]

def zero(m, n):
    return [[0 for _ in range(n)] for _ in range(m)]

def num_rows(m):
    return len(m)

def num_cols(m):
    return len(m[0]) if m else 0

def dimension(m):
    return (num_rows(m), num_cols(m))

def add_rows(*rows):
    return [sum(z) for z in zip(*rows)]

def scale_row(c, r):
    return [c * x for x in r]

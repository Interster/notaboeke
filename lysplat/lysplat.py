#%%
# Vanaf:  https://realpython.com/preview/python-flatten-list/
#
# Maak 'n matriks plat om 'n lys te wees.  Gebruik die += met lyste

matrix = [
    [9, 3, 8, 3],
    [4, 5, 2, 8],
    [6, 4, 3, 1],
    [1, 0, 4, 5],
]

#%%
# Metode 1:  Met extend

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list.extend(row)
    return flat_list

flatten_extend(matrix)

# %%
# Metode 2:  Met += byvoeg

def flatten_extend(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list

flatten_extend(matrix)
# %%

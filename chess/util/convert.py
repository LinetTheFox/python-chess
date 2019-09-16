# convert the name like e4, d8 etc to the couple of indices for the 2d array
def ntf(name: str) -> tuple:
    return '87654321'.index(name[1]), 'abcdefgh'.index(name[0])


# convert the couple of 2d array indices to the name like e5, a1
# def ftn(indices: tuple) -> str:
#     return 'abcdefgh'[indices[1]] + '87654321'[indices[0]]

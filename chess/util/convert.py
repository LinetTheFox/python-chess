# convert the name like e4, d8 etc to the couple of indices for the 2d array
def ntf(name: str) -> tuple:
    return '87654321'.index(name[1]), 'abcdefgh'.index(name[0])


# convert the piece code to its normal name for status messages
def ctn(code: str) -> str:
    color = 'white' if code[0] == 'W' else 'black'

    if code[1] == 'P':
        name = 'pawn'
    elif code[1] == 'N':
        name = 'knight'
    elif code[1] == 'B':
        name = 'bishop'
    elif code[1] == 'R':
        name = 'rook'
    elif code[1] == 'Q':
        name = 'queen'
    else:
        name = 'king'

    return f"{color} {name}"

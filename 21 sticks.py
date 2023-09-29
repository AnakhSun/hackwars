def make_move(sticks):
    if sticks % 4 == 0:
        return 3
    else:
        return sticks % 4
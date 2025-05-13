def min_abc(a, b, c):
    if a > b:
        if b > c:
            return c
        else:
            return b
    else:
        if a > c:
            return c
        else:
            return a
        
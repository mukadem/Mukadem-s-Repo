def min_pos(vals):
    """Returns the minimum positive value."""
    min_val = max(vals)
    print(x)
    for v in vals:
        if (v >= 0) and (v < min_val):
            min_val = v
    return min_val


x = [-2, -4, 3, 6, 88, 76, -7]
y = min_pos(x)

print(y)

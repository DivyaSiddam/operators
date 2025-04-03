def in_same_range(x, y):
    if 0 <= x <= 50 and 0 <= y <= 50:
        return True
    elif 51 <= x <= 100 and 51 <= y <= 100:
        return True
    return False

print(in_same_range(20, 45))  # True
print(in_same_range(20, 60))  # False

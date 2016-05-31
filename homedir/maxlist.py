def max_list(a_list):
    max_so_far = a_list[0]
    for a in a_list:
        if a > max_so_far:
            max_so_far = a
    return max_so_far

print(max_list([0, 4, -6, 9]))


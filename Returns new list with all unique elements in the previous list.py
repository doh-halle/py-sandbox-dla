def unique_list(ls):
    x = []
    for a in ls:
        if a not in x:
            x.append(a)
    return x
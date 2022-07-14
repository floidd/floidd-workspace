def set_gen(lst):
    item = 0
    while item < len(lst):
        cnt = lst.count(lst[item])
        if cnt > 1:
            lst[item] = str(lst[item]) * cnt
        item += 1
    return set(lst)


print(set_gen([1,2,2,2,3,4,4,5,5,6,7,8]))
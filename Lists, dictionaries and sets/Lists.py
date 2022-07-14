
def all_eq(list, new_list=[]):
    max_item = max(list, key=lambda x: len(x))
    max_len = len(max_item)
    for item in list:
        new_list.append(item.ljust(max_len, '!'))
    return new_list


print(all_eq(['Java', 'Python', 'C++']))
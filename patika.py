def flatten(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list


 
def reverse_nested(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(reverse_nested(item))
        else:
            reversed_list.append(item)
    return reversed_list

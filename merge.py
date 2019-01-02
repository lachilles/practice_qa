def merge(list1, list2):
    # Takes two sorted lists and merges them in sorted order
    i1 = i2 = 0
    out_list = []
    while i1 < len(list1) or i2 < len(list2):
        elem1 = list1[i1] if i1 < len(list1) else None
        elem2 = list2[i2] if i2 < len(list2) else None
        if elem1 is None or (elem2 is not None and elem2 < elem1):
            out_list.append(elem2)
            i2 += 1
        else:
            out_list.append(elem1)
            i1 += 1
    print(out_list)

merge([1, 2, 4], [3, 5, 6])
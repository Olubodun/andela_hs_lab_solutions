def my_sort(input_list):
    odd=[]
    even=[]
    for i in input_list:
        if i % 2 == 1:
            odd.append(i)
        else:
            even.append(i)
    return sorted(odd) + sorted(even)
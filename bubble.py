def bubble_sort(alist):
    is_sorted = False
    while(is_sorted == False):
        num_swaps = 0
        for i in range(len(alist)-1):
            if alist[i] > alist[i+1]:
                print(alist)
                current_index = alist[i]
                next_index = alist[i +1]
                alist[i] = next_index
                alist[i+1] = current_index
                num_swaps +=1
        if num_swaps == 0:
            is_sorted = True
    return alist

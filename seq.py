def seq(arr):
    length = 0
    i_var = -1
    j_var = -1

    for i in range(len(arr)-1):
        j=i+1
        while arr[j] < arr[j+1]:
            j+=1
        if (j-i) > length:
            i_var = i
            j_var = j

    for k in range(i,j+1):
        print k



arr = [3, 2, 3, 3, 4, 5 ,4, 4, 4, 6, 6, 6, 6, 3, 2, 99, 999, 9999]
seq(arr)

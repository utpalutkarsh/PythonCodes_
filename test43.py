def bubble_sorting(list1):
    for i in range(len(list1)-1, 0, -1):
     for j in range(i):
        if list1[j] > list1[j+1] :
            list1[j+1], list1[j] = list1[j], list1[j+1]
    return list1

def selection_sorting(list1):
    min_index = 0

list2 = [5, 4, 10, 3, 2, 1]
print(bubble_sorting(list2))


def merge_sort(arr):
    
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])

    return merge(left_half,right_half)

def merge(left,right):

    merged=[]
    left_index,right_index=0,0


    while left_index<len(left) and right_index<len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged    


liste=[1,4,2,98,45,76,72,95,12]
print(merge_sort(liste))
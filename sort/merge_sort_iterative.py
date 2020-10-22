import heapq
def mergeSort(a):
    current_size = 1
    while current_size < len(a):
        left = 0
        while left < len(a)-1:
            mid = min(left + current_size - 1, len(a)-1)
            right = min(left + 2*current_size - 1, len(a)-1) 
            merge(a,left,mid,right)
            # merge2(a,left,mid,right)
            # merge3(a,left,mid,right)
            left += current_size*2
        current_size *= 2

def merge(a,l,m,r):
    L = a[l:m+1]
    R = a[m+1:r+1]  
    k=l
    while L and R:
        if L[0] <= R[0]:
            a[k] = L.pop(0)
        else:
            a[k] = R.pop(0)
        k+=1 
    while L:
        a[k] = L.pop(0)
        k+=1
    while R:
        a[k] = R.pop(0)
        k+=1   

def merge2(a,l,m,r):
    L = a[l:m+1]
    R = a[m+1:r+1]    
    result=[]
    while L and R:
        if L[0] <= R[0]:
            result.append(L.pop(0))
        else:
            result.append(R.pop(0))
    if L:
        result += L
    if R:
        result += R                                          
    a[l:r+1] = result

# using heapq.merge
def merge3(a,l,m,r):
    L = a[l:m+1]
    R = a[m+1:r+1]    
    a[l:r+1] = heapq.merge(L,R)

# Driver code 
a = [8,4,9,2,1,5,7,6,3]
print("Given array is ") 
print(a) 

mergeSort(a) 

print("Sorted array is ") 
print(a)
#insertion sort:

def insertion_sort(a):
    for j in range(2,len(a)):
        key=a[j]
        i=j-1
        while(i>0 and a[i]>key):
            a[i+1]=a[i]
            i=i-1
        a[i+1]=key
        
    
a=[int(x) for x in input().split()]
insertion_sort(a)
print(a)

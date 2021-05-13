n = input()
l = list(map(int, input().split()))
def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr
ans=[]
L= bubble_sort(l)
k=0
for i in range(0,len(l),2):
    k=k+L[i]
print(k)
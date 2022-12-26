def arrayIndex(n,arr,a):
    if a not in arr :
        return -1
    else:
        for i in range(n):
            if arr[i]==a:
                return i

n = int(input())
arr = [int(x) for x in input().split()]
a = int(input())

print(arrayIndex(n,arr,a))

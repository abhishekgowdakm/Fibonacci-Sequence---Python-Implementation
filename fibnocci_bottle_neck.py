def bottom_neck(n):
    if n ==1 or n==2:
        return 1
    bottom_neck = [None]*(n+1)
    bottom_neck[1] = 1
    bottom_neck[2] = 1
    
    for i in range(3,n+1):
        bottom_neck[i] = bottom_neck[i-1] +bottom_neck[i-2]
    return bottom_neck[n]

print(bottom_neck(10))
    
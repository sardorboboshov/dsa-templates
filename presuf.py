def pre(arr):
    n = len(arr)
    ret = [0] * n
    ret[0] = arr[0]
    for i in range(1, n):
        ret[i] += ret[i-1] + arr[i]
    return ret

def suf(arr):
    n = len(arr)
    ret = [0] * n
    ret[-1] = arr[-1]
    for i in range(n - 2, -1, -1):
        ret[i] += ret[i+1] + arr[i]
    return ret
            


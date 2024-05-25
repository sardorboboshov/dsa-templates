dirs = ((0,1),(0,-1),(1,0),(-1,0))
m,n = 0,0
def gen(i,j,dirs):
    for di,dj in dirs:
        ni,nj = i+di,j+dj
        yield ni,nj

def isValid(i,j):
    return 0 <= i < m and 0 <= j < n
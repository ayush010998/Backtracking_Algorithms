# problem statements :-The subset sum problem is to find the subset of elements that are selected from a given set whose sum adds up to a given number K. We are considering the set contains non-negative values. It is assumed that the input set is unique (no duplicates are presented).

def subsetsutil(A,subset,index):
    for i in range(index,len(A)):
        subset.append(A[i])
        subsetsutil(A,subset,i+1)
        subset.pop(-1)
    return
def subsets(A):
    global res
    subset=[]
    index=0
    subsetsutil(A,subset,index)

A=[1,2,3,4,5]
subsets(A)
    
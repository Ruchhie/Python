#LISTS
#Python program to interchange first and last elements in a list
#Input : [12, 35, 9, 56, 24] Output : [24, 35, 9, 56, 12] Input : [1, 2, 3] Output : [3, 2, 1]

def SwapList(newlist):

    """size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp"""

    """temp=newlist[0]
    newlist[0]=newlist[-1]
    newlist[-1]=temp"""

    """newlist[0], newlist[-1] = newlist[-1], newlist[0]"""

    start,*middle, end = newlist
    newlist=[end, *middle, start]

    return newlist

newlist=[3,4,5,6, 7]
print(SwapList(newlist))


    
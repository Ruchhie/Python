"""Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]"""

def Swaplist(newlist,p1,p2):
    """newlist[p1],newlist[p2] = newlist[p2],newlist[p1]"""
    temp=list[p2]
    list[p2]=list[p1]
    list[p1]=temp
    
    return newlist


list=[2,6,1,9]
pos1=1
pos2=3
print(Swaplist(list,pos1-1,pos2-1))

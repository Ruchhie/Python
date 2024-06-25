#Swap elements in String list
#a->X
#X->a

list=['ABCX','abcX','dxabc','wXsd','dfga']
print("The original list : "+str(list))

#using replace join split
res=','.join(list)
print(res)
res=res.replace("a","-").replace("X","a").replace("-","X").split(',')
print(res)
print("list after swap :"+str(res))


def guibing(lista,listb):
    listc=[]
    i=j=0
    while i<len(lista) and j<len(listb):
        if lista[i]<listb[j]:
            listc.append(lista[i])
            i+=1
        else:
            listc.append(listb[j])
            j+=1
    if i==len(lista):
        for a in listb[j:]:
            listc.append(a)
    else:
        for a in lista[i:]:
            listc.append(a)
    return listc        
def merge_sort(lists):
    if len(lists)<=1:
        return lists
    mid=len(lists)//2
    left=merge_sort(lists[:mid])
    right=merge_sort(lists[mid:])
    return guibing(left, right)


if __name__=="__main__":
    alist=[5,7,3,0,2,4,90,8,80,999,9]
    print(merge_sort(alist))
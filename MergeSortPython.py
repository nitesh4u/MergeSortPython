def mergeSort(alist) :
    if len(alist)>1:
          mid = len(alist)/2
          lefthalf = alist[:mid]
          righthalf = alist[mid:]
        print("This is from FeatureB ")
        mergeSort(lefthalf)
        mergeSort(righthalf)

        i,j,k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
  
       while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

alist = [5,1,4,2,3,7]
mergeSort(alist)
print(alist)
print(alist)
print("This is added by Developer A from Feature A")
print("This is added by Developer B from Feature B")
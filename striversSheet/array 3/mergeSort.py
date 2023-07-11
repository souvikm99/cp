arr = [2,1,5,3,6,4,7]

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]

        mergeSort(l)
        mergeSort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
        

        while i<len(l):
            # print("if elm in l")
            # print(arr,k)
            # print(l)
            arr[k] = l[i]
            i+=1
            k+=1
        while j<len(r):
            # print("if elm in r")
            # print(arr,k)
            # print(r)
            arr[k] = r[j]
            j+=1
            k+=1
        
        return arr

print(mergeSort(arr))
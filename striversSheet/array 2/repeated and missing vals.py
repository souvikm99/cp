A = [3,1,2,5,4,6,7,5] 

b = set()

for i in range(len(A)):
    if A[i] not in b:
        b.add(A[i])
        b = list(b)
        b.sort()
        b = set(b)
        print("set : ", b)
    else:
        print("Missin: " ,A[i])

for i in range(len(A)):
    if i+1 not in b:
        print(i+1)
            
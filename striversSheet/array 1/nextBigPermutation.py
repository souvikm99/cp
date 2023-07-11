my_array = [1, 2, 3]
def next_perm(arr):
    def perm(lis):
        if len(lis) == 0:
            return []
        elif len(lis) == 1:
            return [lis]
        else:
            l = []
            for i in range(len(lis)):
                x = lis[i]
                xs = lis[:i] + lis[i+1:]
                print('x = ',x)
                print('xs = ',xs)
                for p in perm(xs):
                    l.append([x]+p)
                    print("l = ", l)
            print("lap ends")
            return l

    res = perm(my_array)
    print(res)

    for i in range(len(res)):
        if res[i] == my_array:
            return res[i+1]

print(next_perm(my_array))
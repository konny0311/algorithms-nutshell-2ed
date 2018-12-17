def insertionSort(l):
    for pos in range(1,len(l)):
        #insert関数
        insert(l, pos, l[pos])
    return l #ソートされたリスト
    end

def insert(l,pos,value):
    i = pos - 1
    while i >= 0 and l[i] > value:
        print(l[i])
        l[i+1] = l[i]
        i -= 1
        l[i+1] = value
        print(l)


l = [5,2,5,8,5,9,89,23,44,57,10]
print(l)
print(insertionSort(l))

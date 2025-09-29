#2025-09-29 
#課題：リストから偶数だけを取り出して表示

mylist1 = list(range(10))
mylist2 = []

for n in mylist1 :
    if n % 2 == 0 :
        mylist2.append(n)
print(mylist2)


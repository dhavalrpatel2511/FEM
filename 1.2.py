n = int(input("enter any integer value: "))
#print(n)
a = [500,200,100,50,20,10,5,2,1]
ans = []
for k in range(0,9,1):
    m = n//a[k]
    if m > 0:
        for i in range(m):
          ans.append(a[k])
    n = n%a[k]
print(ans)





import numpy as np
p=[[[1,2],[3,4]],[[1,2],[3,4]]]
#print(p)

n = int(input('enter any integer value for elements: '))
A = []
for i in range(n):
    a = np.zeros((2,n+1))
    a[0][i]=1
    a[1][i+1]=1
    A.append(a)
#print(A[0])
#print(A[1])
#print(A[2])
#at = A[1].transpose(1,0),
#print(at)
k=np.zeros((n+1,n+1))
K=[[1,-1],[-1,1]]
for i in range(n):
    k = k + np.matmul(np.matmul(A[i].transpose(1,0),K),A[i])
print(k)
f=np.zeros(n+1)
F=[1,1]
for i in range(n):
    f = f + np.matmul(A[i].transpose(1,0),F)
print(f)
ke=k[1:,1:]
#print(ke)  
fe=f[1:]
#print(fe)
ans = np.matmul(np.linalg.inv(ke),fe)
print(ans)
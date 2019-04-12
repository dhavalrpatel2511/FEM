import numpy as np
n = int(input('enter any integer value for elements: '))
A = []
for i in range(n):
    a = np.zeros((2,n+1))
    a[0][i]=1
    a[1][i+1]=1
    A.append(a)
k=np.zeros((n+1,n+1))
K=[[1,-1],[-1,1]]
for i in range(n):
    k = k + np.matmul(np.matmul(A[i].transpose(1,0),K),A[i])
print('the stiffness matrix is: \n',k)
f=np.zeros(n+1)
F=[1,1]
for i in range(n):
    f = f + np.matmul(A[i].transpose(1,0),F)
print('the force vector is:\n ',f)
ke=k[1:,1:]
#print(ke)
fe=f[1:]
#print(fe)
ans = np.matmul(np.linalg.inv(ke),fe)
print('The FEM solution for the displacement: ',ans)
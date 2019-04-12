import matplotlib.pyplot as plt
N = int(input("enter any integer value: "))
i = 1
X = []
Y = []
x = 1
y = N/x
X = [x]
Y = [y]
while round(x,5)!=round(y,5):
    x = (x+y)/2
    y = N/x
    X.append(x)
    Y.append(y)
print(x)
#print(X)
sx = len(X)
sy = len(Y)
dX=[]
dY=[]
for i in range(sx-1):
    dx = X[i+1]-X[i]
    dy = Y[i+1]-Y[i]
    dX.append(dx)
    dY.append(dy)
#print(sx,sy)
#print(dX)
#print(dY)
dXp = [abs(i) for i in dX]
dYp = [abs(i) for i in dY]
plt.subplot(2,1,1)
plt.plot(X,'r--o')
plt.plot(Y,'b--o')
plt.ylabel('X,Y')
plt.subplot(2,1,2)
plt.plot(dXp,'r--o')
plt.yscale('log')
plt.plot(dYp,'b--o')
plt.yscale('log')
plt.ylabel('dX,dY')
plt.show()



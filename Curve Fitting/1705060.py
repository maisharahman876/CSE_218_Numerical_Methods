import numpy as np;
import matplotlib.pyplot as plt
import string
np.set_printoptions(formatter={'float':'{:0.3f}'.format})
        
x=[]
y=[]
temp=[]
fin=open('data.txt','r');
lines=fin.readlines()
fin.close()
n=len(lines)
inf=open('data.txt','r')
for i in range(n):
    ln=inf.readline().split()
    x.append(float(ln[0]))
    temp.append(float(ln[0]))
    y.append(float(ln[1]))
temp.sort()    
plt.figure(figsize=(15,10))        
plt.scatter(x,y, s=1)
def summation(n,x,y,px,py):
    s=0
    for i in range(n):
        s+=(x[i]**px)*(y[i]**py)
    return s    
        
def lu_method(a,b,n):
    l = np.zeros([n, n])
    y= np.zeros([n,1])
    xx= np.zeros([n,1])
    for k in range(1,n):
         r=a[k-1][k-1]
         for i in range (k,n):
             m=a[i][k-1]
             l[i][k-1]=m/r
             for j in range(k-1,n):
                 a[i][j]=a[i][j]-((a[k-1][j]*m)/r)
    y[0][0]=b[0][0]             
    for i in range(1,n):
        sum=0
        for j in range(i):
            sum=sum+ l[i][j]* y[j][0]
        y[i][0]=b[i][0]-sum 
    xx[n-1][0]=y[n-1][0]/(a[n-1][n-1])            
    for i in range(n-2,-1,-1):
        sum=0
        for j in range(n-1,i,-1):
            sum=sum+ a[i][j]* xx[j][0]
        xx[i][0]=(y[i][0]-sum)/a[i][i] 
    return xx 
def curve_fitting(x,y,n,d,temp):    
    y1=[]
    yi=[]
    a=np.zeros([d+1,d+1])
    b=np.zeros([d+1,1])
    for i in range(d+1):
        for j in range(d+1):
            a[i][j]=summation(n,x,y,i+j,0)
        b[i][0]=summation(n,x,y,i,1)
    a[0][0]=n
    ans=lu_method(a,b,d+1)
    print('The Parameters for degree',d,' are:')
    print(ans)
    st=0
    sr=0
    avgy=summation(n,x,y,0,1)/n
    for j in range(n):
        s1=0
        for i in range(d+1):
            s1+=(ans[i][0])*(x[j]**i)
        yi.append(s1)
   
    for i in range(n):
        st+=(y[i]-avgy)**2
        sr+=(y[i]-yi[i])**2
        
    r=((st-sr)/st)**(1/2)
    print('The value of r is ','%.4f' % r)
   
    for j in range(len(temp)):
        s=0
        for i in range(d+1):
            s+=(ans[i][0])*(temp[j]**i)
        y1.append(s)    
    return y1   
        

#x1=np.arange(min(x),max(x),0.1)
#temp=x  
#temp.sort()
y1=curve_fitting(x,y,n,1,temp)
y2=curve_fitting(x,y,n,2,temp)
y3=curve_fitting(x,y,n,3,temp)
plt.plot(temp,y1, label="order=1")
plt.plot(temp,y2, label="order=2")
plt.plot(temp,y3, label="order=3")
plt.grid("True")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

            
            
    
    
          
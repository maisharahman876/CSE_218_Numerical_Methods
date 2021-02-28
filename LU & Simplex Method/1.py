import numpy as np
np.set_printoptions(formatter={'float':'{:0.4f}'.format})
import string

fin=open('in1.txt','r')
n= int(fin.readline())
b = np.zeros([n, 1])
l = np.zeros([n, n])
y= np.zeros([n,1])
xx= np.zeros([n,1])
u = np.zeros([n, n])

for i in np.arange(n):
    ln=fin.readline().split()
    j=0
    for x in ln:
        u[i][j]=float(x)
        if (i == j):
            l[i][j]=1
        j=j+1

 
for i in np.arange(n):
  b[i][0] = float(fin.readline())   
"""finding l and u """ 
for k in range(1,n):
     r=u[k-1][k-1]
     for i in range (k,n):
         m=u[i][k-1]
         l[i][k-1]=m/r
         for j in range(k-1,n):
             u[i][j]=u[i][j]-((u[k-1][j]*m)/r)
             
             
def validity(u,n):
    for i in range(n):
       s=0
       for j in range(n):
          if(u[i][j]==0):
            s+=1
       if(s==n):
         return 0
    return 1

y[0][0]=b[0][0]             
for i in range(1,n):
    sum=0
    for j in range(i):
        sum=sum+ l[i][j]* y[j][0]
    y[i][0]=b[i][0]-sum       


xx[n-1][0]=y[n-1][0]/(u[n-1][n-1])            
for i in range(n-2,-1,-1):
    sum=0
    for j in range(n-1,i,-1):
        sum=sum+ u[i][j]* xx[j][0]
    xx[i][0]=(y[i][0]-sum)/u[i][i]    
fout=open("out.txt","w")
for i in range(n):
    for j in range(n):
        fout.write(str.format('{:0.4f}',l[i][j]))
        fout.write(' ')
    fout.write("\n")
fout.write("\n") 
for i in range(n):
    for j in range(n):
        fout.write(str.format('{:0.4f}',u[i][j]))
        fout.write(' ')
    fout.write("\n")
fout.write("\n")    
if(validity(u,n)):
    for i in range(n):
        fout.write(str.format('{:0.4f}',y[i][0]))
        fout.write("\n")
    fout.write("\n")    
    for i in range(n):
        fout.write(str.format('{:0.4f}',xx[i][0]))
        fout.write("\n")
    fout.write("\n")       
else:
   fout.write("No unique solution")     



















fin.close()
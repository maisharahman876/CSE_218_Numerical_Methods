import numpy as np
np.set_printoptions(formatter={'float':'{:0.2f}'.format})
fin=open('in2.txt','r')
n=0
 
ln=fin.readline().split()
lines=fin.readlines()     
for x in ln:
        n+=1
        
fin.close()
l=len(lines)
nf=n+l+3
lf=l+1
z=np.zeros([lf,nf])
nfin=open('in2.txt','r') 
ln=nfin.readline().split()
z[0][0]=1
j=1
for x in ln:
    z[0][j]=-float(x)
    j+=1
for i in np.arange(len(lines)):
    ln=nfin.readline().split()
    j=0
    for x in ln:
        if(j==n):
            z[i+1][nf-2]=float(x)
        else:
             z[i+1][j+1]=float(x)
        j=j+1 
for i in range(1,l+1):
     for j in range(n+1,n+l+1):
         if((i-1)==(j-n-1)):
             z[i][j]=1
#print(z) 
#print("\n")            
def nonnegative(list1,n):
    for i in range(1,n-2):
        if(list1[0][i]<0):
            return False
    return True    
def basic_variable(list1,col):
    min=0
    for i in range(1,col):
        if(list1[0][i]<list1[0][min]):
            min=i
    return min

def intercept_col(list1,col,row,c):
    for i in range(1,row):
        if(list1[i][c]==0):
            list1[i][col-1]=0
        else:
           list1[i][col-1]=list1[i][col-2]/list1[i][c]    
    return

def smallest(list1,n,m):
    min_int=1
    min=100000
    for i in range(1,m):
        if(list1[i][n-1]==0 or list1[i][n-1]<0):
            continue
        else:
            if(list1[i][n-1]<min):
                min=list1[i][n-1]
                min_int=i
    return min_int        
    
print(z)
print("\n")        
def gausss_jordan(list1,col,row):
    c=basic_variable(list1,col)
    intercept_col(list1,col,row,c)
    r=smallest(list1,col,row)
   
    v = (list1[r][c])
    for i in range(1, col):
         
         list1[r][i]=(list1[r][i]/v)
   
   
    #for i in range(1, col-1):
        #list1[r][i] = list1[r][i]/list1[r][c]
    for i in range(row):
        temp = list1[i][c]/list1[r][c]
        for j in range(col-1):
            if i != r:
                list1[i][j] = list1[i][j]-temp*list1[r][j]
    
    print(list1)
    print("\n")
    for i in range(row):
        list1[i][col-1]=0
        
    return list1
    
    
while nonnegative(z,nf)==False:      
    a=gausss_jordan(z,nf,lf)
    z=a
print("The result is ",z[0][nf-2])
print("he value of variables are:")    
for var in range(1,n+1):         
    for i in range(lf):
        if(z[i][var]==1):
           print(z[i][nf-2])
           break
    
    
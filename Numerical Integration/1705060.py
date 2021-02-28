import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(formatter={'float':'{:0.4f}'.format})

def trapezoidal(i,x,fx):
    a=x[i]
    b=x[i+1]
    fa=fx[i]
    fb=fx[i+1]
    return ((b-a)*(fa+fb)/2)
def simpson_one_third(i,x,fx):
    a=x[i]
    b=x[i+2]
    h=(b-a)/2
    fx0=fx[i]
    fx1=fx[i+1]
    fx2=fx[i+2]
    return (h*(fx0+(4*fx1)+fx2)/3)
def simpson_three_eight(i,x,fx):
    a=x[i]
    b=x[i+3]
    h=(b-a)/3
    fx0=fx[i]
    fx1=fx[i+1]
    fx2=fx[i+2]
    fx3=fx[i+3]
    return (3*h*(fx0+(3*fx1)+(3*fx2)+fx3)/8)
def interval(x,i,j):
    return(x[j]-x[i])

def func(l):
    if(int(l/3)%2==0):
        return int(l/3)
    else:
        return (int(l/3)-1)
def func1(l):
    if(int(l/3)%2==1):
        return int(l/3)
    else:
         return (int(l/3)-1)
        
    
    
def graph(i,x,fx,n,nl):
    x1=[]
    y1=[]
    if(n==3):
        for j in range(n+1):
            x1.append(x[j+i])
            y1.append(fx[i+j])
        if(nl==0):    
           plt.fill_between(x1,y1,color="skyblue",alpha=1.0,label='Simpsons 3/8 Rule')
        else:
          plt.fill_between(x1,y1,color="skyblue",alpha=1.0)  
    elif(n==2):
         for j in range(n+1):
            x1.append(x[j+i])
            y1.append(fx[i+j])
         if(nl==0):    
           plt.fill_between(x1,y1,color="purple",alpha=1.0,label='Simpsons 1/3 Rule')
         else:
          plt.fill_between(x1,y1,color="purple",alpha=1.0) 
    else:
        for j in range(n+1):
            x1.append(x[j+i])
            y1.append(fx[i+j])
        if(nl==0):    
           plt.fill_between(x1,y1,color="blue",alpha=1.0,label='Trapezoid Rule')
        else:
          plt.fill_between(x1,y1,color="blue",alpha=1.0) 
    #plt.plot(x1,y1)
    #plt.fill_between(x1,y1,color="skyblue",alpha=1.0)
        
fin=open('input.txt','r')
n=int(fin.readline())
x=[]
xl=[]
fx=[]
j=0
k=0
for i in range(n):    
    line=fin.readline().split()
    if(j>0):
       h2=round((x[j-1]-x[j-2]),5)
    x.append(float(line[0]))
    j+=1
    fx.append(float(line[1]))
    if(j>1):
       h1=round((x[j-1]-x[j-2]),5)
       if(h1==h2):
           xl.append(k)
       else:
           k+=1
           xl.append(k)
plt.figure(figsize=(15,10)) 
ml=xl[n-2]           
la=[]
for m in range(1,ml+1):           
    l=0         
    for p in range(len(xl)):
             if(xl[p]==m):
                 l+=1
    la.append(l)             
#print(la)            
n1=0
n2=0
n3=0
sum=0.0
i=0
m=1
for  j in la:      
         if(j==1):
                sum+=trapezoidal(i,x,fx)
                graph(i,x,fx,1,n1)
                n1+=1
                i+=1
             
         elif(j==4):
                 sum+=simpson_one_third(i,x,fx)
                 graph(i,x,fx,2,n2)
                 i+=2
                 n2+=1
                 sum+=simpson_one_third(i,x,fx)
                 graph(i,x,fx,2,n2)
                 i+=2
                 n2+=1             
         elif(j==3):
                sum+=simpson_three_eight(i,x,fx)
                graph(i,x,fx,3,n3)
                i+=3
                n3+=1
         elif(j==2):
                sum+=simpson_one_third(i,x,fx)
                graph(i,x,fx,2,n2)
                i+=2
                n2+=1
         else:
                if(j%2==0):
                    sim38=func(j)
                    sim13=int((j-3*sim38)/2)
                    #print(sim38)
                    for q in range(sim38):
                        sum+=simpson_three_eight(i,x,fx)
                        graph(i,x,fx,3,n3)
                        i+=3
                        n3+=1
                        #sim38-=1
                    for q in range(sim13):
                        sum+=simpson_one_third(i,x,fx)
                        graph(i,x,fx,2,n2)
                        i+=2
                        n2+=1
                        #sim13-=1
                else:
                    sim38=func1(j)
                    sim13=int((j-3*sim38)/2)
                    #print(sim38)
                    for q in range(sim38):
                        sum+=simpson_three_eight(i,x,fx)
                        graph(i,x,fx,3,n3)
                        i+=3
                        n3+=1
                        #sim38-=1
                    for q in range(sim13):
                        sum+=simpson_one_third(i,x,fx)
                        graph(i,x,fx,2,n2)
                        i+=2
                        n2+=1
                        #sim13-=1
      
            
                 
    
plt.plot(x,fx,color='black',marker='o',markerfacecolor='black',markersize=10,label='Curve') 
plt.grid("True")
plt.title("Numerical Integration")
plt.xlabel('Value of x')
plt.ylabel('Value of fx')
plt.legend()           
print('Trapezoid Rule:',n1,'intervals')
print('Simpsons 1/3 Rule:',n2*2,'intervals')
print('Simpsons 3/8 Rule:',n3*3,'intervals\n')

print('Integral Value:',round(sum,4))
#print(fx)
plt.show()
fin.close()
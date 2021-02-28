import math
import matplotlib.pyplot as plt
import numpy as np
def loge(n, x) :
    sum = 1.0
    for i in range(n, 1, -1) :
        sum = 1 - (float(i) - 1) * x * sum / float(i)
    return (sum * x)
 
n = int(input("enter the number of iteration: "))
x = float(input("The value of x is : "))
print ("ln(1+x): ",loge(n, x))       

x=np.arange(-1,1,0.1)
y=np.log(1+x)
y1=[]
y2=[]
y3=[]
y4=[]
y5=[]
plt.plot(x,y)
plt.show()
for i in x:
    y1.append(loge(1,i))
    
plt.plot(x,y1)
for i in x:
    y2.append(loge(3,i))
    
plt.plot(x,y2)  
for i in x:
    y3.append(loge(5,i))
    
plt.plot(x,y3)
for i in x:
    y4.append(loge(20,i))
    
plt.plot(x,y4)
for i in x:
    y5.append(loge(50,i))
    
plt.plot(x,y5) 
plt.show()
x6=np.arange(2,51,1)
y6=[]
prev=1
"""
for i in range(2,51):
    x6.append(i)
    print(i)
    """
   
for i in x6:
    pre=loge(i,0.5)
    y6.append(abs((pre-prev)/pre*100))
    prev=pre
    
    
plt.plot(x6,y6,0.1)  
plt.show() 


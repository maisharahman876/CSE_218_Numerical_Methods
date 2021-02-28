import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,1,.001)
y1=[]
for i in x:
    y1.append(0)
y=x**3-2400*x**2-3*x+2
plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.plot(x,y1)

plt.show()
def f(x):
    return x**3-2400*x**2-3*x+2
l=0.0
u=1.0
es=0.5
max=int(input("The maximum iteration is : "))
def secant(f,x1,x2,e,m):
    xm=0
    x0=0
    n=0
    c=0
    if(f(x1)*f(x2)<0):
        while True:
            x0 = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
            c = f(x1) * f(x0)
            x1 = x2
            x2 = x0
            n += 1
            if (c == 0):
                break
            xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)))
            if(abs(xm - x0) > e):
                break
           
        if(n>m):
                print("Secant method:The root can't be find in the maximum iteration")
        else:
            print("Root of the given equation in secant method =", x0)
            print("No. of iterations in Secant Method = ", n)
    else:
        print("Can not find a root in ", "the given inteval")
        
secant(f,l,u,es,max)  
def false_position(f,lower,upper,e,m):
    c=lower
    n=0
    if(f(upper)*f(lower)<0):

           
        for i in range(m):
            c = (lower * f(upper) - upper * f(lower))/ (f(upper) - f(lower)) 
            n=n+1
            
            if f(c) == 0:
                break

            elif f(c) * f(lower) < 0: 
                upper = c 
            else: 
                lower= c
                
        print("Root of the given equation in False Position Method : " ,c)
        print("Number of iteration in False positin Method " ,n)
    else:
        print("The root can't be found in this interval")
false_position(f,l,u,es,max)     
             

    
    

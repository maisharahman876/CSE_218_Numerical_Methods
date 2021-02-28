import math
import numpy as np
import matplotlib.pyplot as plt
#x=np.arange(0,11)
y0=4
#y=[]
def getx(h):
    x=np.arange(0,10+h,h)
    return x
def dydx(x,y):
    return ((x + 20*y)*math.sin(x*y))
def euler(f,y0,h):
    x=np.arange(0,10+h,h)
    y=[]
    y.append(y0)
    yi=y0
    j=0
    for i in range(len(x)-1):
        yf=yi+f(x[j],yi)*h
        y.append(yf)
        yi=yf
        j+=1
    return y
def RK2(f,y0,h,a2):
    x=getx(h)
    y=[]
    y.append(y0)
    yi=y0
    a1=1-a2
    p1=1/(2*a2)
    q11=p1
    j=0
    for i in range(len(x)-1):
        k1=f(x[j],yi)
        k2=f(x[j]+p1*h,yi+q11*h*k1)
        yf=yi+(a1*k1+a2*k2)*h
        y.append(yf)
        yi=yf
        j+=1
    return y  
def RK4(f,y0,h):
     x=getx(h)
     y=[]
     y.append(y0)
     yi=y0
     j=0
     for i in range(len(x)-1):
        k1=f(x[j],yi)
        k2=f(x[j]+0.5*h,yi+0.5*h*k1)
        k3=f(x[j]+0.5*h,yi+0.5*h*k2)
        k4=f(x[j]+h,yi+h*k3)
        yf=yi+( (k1+2*k2+2*k3+k4)*h*(1/6))
        y.append(yf)
        yi=yf
        j+=1
     return y
     

#plt.legend()        
plt.figure(figsize=(15,10))
plt.plot(getx(.01),euler(dydx,y0,.01),label="h=0.01")
plt.plot(getx(.05),euler(dydx,y0,.05),label="h=0.05")
plt.plot(getx(.1),euler(dydx,y0,.1),label="h=0.1")
plt.plot(getx(.5),euler(dydx,y0,.5),label="h=0.5")
plt.grid("True")
plt.title("Euler Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend() 
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.01),RK2(dydx,y0,.01,0.5),label="h=0.01")
plt.plot(getx(.05),RK2(dydx,y0,.05,0.5),label="h=0.05")
plt.plot(getx(.1),RK2(dydx,y0,.1,0.5),label="h=0.1")
plt.plot(getx(.5),RK2(dydx,y0,.5,0.5),label="h=0.5")
plt.grid("True")
plt.title("Heun's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend() 
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.01),RK2(dydx,y0,.01,1),label="h=0.01")
plt.plot(getx(.05),RK2(dydx,y0,.05,1),label="h=0.05")
plt.plot(getx(.1),RK2(dydx,y0,.1,1),label="h=0.1")
plt.plot(getx(.5),RK2(dydx,y0,.5,1),label="h=0.5")
plt.grid("True")
plt.title("Midpoint Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.01),RK2(dydx,y0,.01,2/3),label="h=0.01")
plt.plot(getx(.05),RK2(dydx,y0,.05,2/3),label="h=0.05")
plt.plot(getx(.1),RK2(dydx,y0,.1,2/3),label="h=0.1")
plt.plot(getx(.5),RK2(dydx,y0,.5,2/3),label="h=0.5")
plt.grid("True")
plt.title("Ralston's Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.01),RK4(dydx,y0,.01),label="h=0.01")
plt.plot(getx(.05),RK4(dydx,y0,.05),label="h=0.05")
plt.plot(getx(.1),RK4(dydx,y0,.1),label="h=0.1")
plt.plot(getx(.5),RK4(dydx,y0,.5),label="h=0.5")
plt.grid("True")
plt.title("4th Order RK Method")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.01),euler(dydx,y0,0.01),label="Euler Method")
plt.plot(getx(.01),RK2(dydx,y0,.01,0.5),label="Heun's Method")
plt.plot(getx(.01),RK2(dydx,y0,.01,1),label="Midpoint Method")
plt.plot(getx(.01),RK2(dydx,y0,.01,2/3),label="Ralston's Method")
plt.plot(getx(.01),RK4(dydx,y0,.01),label="4th Order RK Method")
plt.grid("True")
plt.title("Step Size 0.01")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.05),euler(dydx,y0,0.05),label="Euler Method")
plt.plot(getx(.05),RK2(dydx,y0,.05,0.5),label="Heun's Method")
plt.plot(getx(.05),RK2(dydx,y0,.05,1),label="Midpoint Method")
plt.plot(getx(.05),RK2(dydx,y0,.05,2/3),label="Ralston's Method")
plt.plot(getx(.05),RK4(dydx,y0,.05),label="4th Order RK Method")
plt.grid("True")
plt.title("Step Size 0.05")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.1),euler(dydx,y0,0.1),label="Euler Method")
plt.plot(getx(.1),RK2(dydx,y0,.1,0.5),label="Heun's Method")
plt.plot(getx(.1),RK2(dydx,y0,.1,1),label="Midpoint Method")
plt.plot(getx(.1),RK2(dydx,y0,.1,2/3),label="Ralston's Method")
plt.plot(getx(.1),RK4(dydx,y0,.1),label="4th Order RK Method")
plt.grid("True")
plt.title("Step Size 0.1")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.figure(figsize=(15,10))
plt.plot(getx(.5),euler(dydx,y0,0.5),label="Euler Method")
plt.plot(getx(.5),RK2(dydx,y0,0.5,0.5),label="Heun's Method")
plt.plot(getx(.5),RK2(dydx,y0,0.5,1),label="Midpoint Method")
plt.plot(getx(.5),RK2(dydx,y0,0.5,2/3),label="Ralston's Method")
plt.plot(getx(.5),RK4(dydx,y0,0.5),label="4th Order RK Method")
plt.grid("True")
plt.title("Step Size 0.5")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
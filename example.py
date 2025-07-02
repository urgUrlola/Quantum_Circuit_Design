import numpy as np
import matplotlib.pyplot as plt 

# just testing some numpy functions 
result =[]
for x in range (10):
    result.append(x)
print(result)
 
 # to create an array np.array 
result = np.array(result) 
print (result)
result=np.array(x for x in range(10))
print(result)

 # to increment by a specific number use np.arange a(start,stop,increase by)
result =np.arange(0,10,2)
print(result)
result = np.arange(2,10,3)
print(result)

 # to get a specific number of values within a range a(start,stop,steps)
result = np.linspace(0,10,5) # increment by 10/4
print(result)
result = np.linspace(3,20,5) # increment by (20-3)/4
print(result)

 # arithmeic 
result= [5 * (result**2) -4]
print(result)
result = np.array([x**2 for x in range(4)])
result = np.sqrt(result)
print(result)
result=np.arange(10)
result=result[3::3]
print(result)

 #boolean 
result=np.arange(11)
print(result)
print(result<0)  
print(result%2==0)

# a[3::3] = -1
# print(a)
# [ 0  1  2 -1  4  5 -1  7  8 -1 10 11 -1 13 14 -1 16 17 -1 19]

# a = np.arange(10)
# a[::-1]
# array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])


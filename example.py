
a = np.array([2.0, 4.0, 8.0, 16.0])
b = np.array([0, 1 + 0j, 1 + 1j, 2 - 2j])
c = np.array(["a", "b", "c", "d"])
print(a)
print(b)
print(c)
#create the list inside of the array function
np.array([n for n in range(10)])

np.arange(0, 10, 2)
array([0, 2, 4, 6, 8])

np.linspace(0, 10, 5)
array([ 0. ,  2.5,  5. ,  7.5, 10. ])


5 * a**2 - 4
array([ 1, 16, 41, 76])

x = np.array([x**2 for x in range(4)])
np.sqrt(x)
array([0., 1., 2., 3.])

a = np.array([0, -1, 2, -3, 4])
print(a < 0)

a = np.arange(20)
a[3::3]
a[start:stop:step]
array([ 3,  6,  9, 12, 15, 18])

a[3::3] = -1
print(a)
[ 0  1  2 -1  4  5 -1  7  8 -1 10 11 -1 13 14 -1 16 17 -1 19]

a = np.arange(10)
a[::-1]
array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

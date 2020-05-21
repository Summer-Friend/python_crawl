import pandas as pd
import numpy as np
import math

x = pd.Series([2.079, 2.565, 3.178, 3.689, 4.159, 4.522, 4.820])
y = pd.Series([0.693, 0.486, 0.613, 0.511, 0.47, 0.363, 0.298])
'''
x = pd.Series(np.arange(10, 80, 10))
y = pd.Series([92, 100, 118, 146, 184, 232, 290])
#print(x)
'''
n = len(x)
print(n)

x1=sum(x)
y1=sum(y)
x2=sum(x**2)
y1x1=sum(x*y)

a = (n*y1x1-x1*y1)/(n*x2-x1*x1)
b = (y1-a*x1)/n
print(a,' ',b)

'''
a = pd.Series([1,2,3])
b = pd.Series([2,3,4])
print(sum(a*b))
'''
#input()
print(math.exp(b/(-a)))

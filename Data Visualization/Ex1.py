import pandas as pd
from matplotlib import pyplot as plt
x=[1,2,3]
y=[1,4,9]
z=[10,5,0]
plt.plot(x,y)
plt.plot(x,z)
plt.title("sample plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["(x,y)","(x,z)"])
plt.show()
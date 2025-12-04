#USING SCRATCH APPROACH

import numpy as np
x=np.array([1.1,1.3,1.5,2.0,2.2,2.9,3.0,3.2,3.2,3.7])
y=np.array([39,46,47,52,56,64,65,67,68,70])

xmean=np.mean(x)
ymean=np.mean(y)

m=np.sum((x-xmean)*(y-ymean)) / np.sum((x-xmean)**2)

b=ymean-(m*xmean)

print("slope:",m)
print("intercept:",b)
newx=4.5
pred=(m*newx) + b
print("predicted salary:", pred)

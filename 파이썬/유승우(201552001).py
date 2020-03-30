# 1번
import numpy as np
np.random.seed(1234)

x = np.random.normal(170., 5.0, size=1000)    
pass 
maxValue = x[0]
for i in range(1, len(x)):
    if maxValue < x[i]:
        maxValue = x[i]
print('%.2f' % maxValue)


# 2번
import numpy as np
np.random.seed(1234)

def piEstimate (n):
    pass
import random
def piestimate(n): 
    t = 0
    for i in range(n):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1: t += 1 
    return 4 * (t/n)
print ("pi=",'%.3f' % piestimate(10000))

# 3번
import pandas as pd
data = pd.read_csv('C:/Users/ysw29/Downloads/MLBattend.csv',sep=',',na_values=".")
pass
df=data[['league','attendance', 'runs.scored', 'runs.allowed']]
df.groupby(['league'], as_index=False).mean()

df.groupby(['league'], as_index=False).corr()

# 4 
import numpy as np
X = np.array(data[['attendance', 'runs.scored', 'runs.allowed']])
n, k  = X.shape         # n: number of observations, k: number of variables
pass
s=np.cov(x)
(X - X.mean()).T.dot((X - X.mean()))/(len(X)-1)



    


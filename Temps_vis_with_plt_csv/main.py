import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df=pd.read_csv("death_valley_2018_simple.csv")
header=df.head()
print(header)
tmax=df["TMAX"]
tmin=df["TMIN"]
date=np.arange(1,365)

fig=plt.figure()
fig.set_size_inches(13,13)
plt.plot(date,tmax,tmin)
plt.title("Temperatures(max and low) in Death Valley")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()
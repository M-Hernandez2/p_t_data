#March 29, 2023
#sampling methods 2.0
#this time I am making 2 sample spaces for hist and proj to be put on the same scatter plot

import chaospy as cp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#SOBOL sample using chaospy
#HISTORIC ONLY
l_hist = [21.37, 45] #P then T
u_hist = [67.21, 61.9]

distribution = cp.J(cp.Uniform(l_hist[0], u_hist[0]),
                    cp.Uniform(l_hist[1], u_hist[1]))
num_hist = 50
samples_h = distribution.sample(size=num_hist, rule="S")
#print(samples_h)

hx = samples_h[0]
hy = samples_h[1]

#creates dataframe of p and t
hist_df = pd.DataFrame({'precipitation': hx,
                           'temperature': hy})
print(hist_df)

#pROJECTED DATA ONLY
l_proj = [26.34, 49.81] #P then T
u_proj = [88.78, 75.88]

distribution = cp.J(cp.Uniform(l_proj[0], u_proj[0]),
                    cp.Uniform(l_proj[1], u_proj[1]))
num_proj = 150
samples_p = distribution.sample(size=num_proj, rule="S")
#print(samples_p)

px = samples_p[0]
py = samples_p[1]

#creates dataframe of p and t
proj_df = pd.DataFrame({'precipitation': px,
                           'temperature': py})
print(proj_df)



#COMBINE HIST AND PROJ TO PLOT
fig, ax = plt.subplots()
ax.scatter(x = hist_df['precipitation'], y = hist_df['temperature'], color = 'indianred')
ax.scatter(x = proj_df['precipitation'], y = proj_df['temperature'], color = 'darkorange')

#ax.scatter(x, y, color = 'darkorange')
ax.set_xlabel('precipitation (in)')
ax.set_ylabel('temperature (F)')
ax.set_title('Sobol Sample of Projected P & T')
plt.show()

#save the hist and proj sobol samples to excel file
hist_df.to_excel("sobol_hist_sample.xlsx")
proj_df.to_excel("sobol_proj_sample.xlsx")





#LATIN-HYPERCUBE sample using chaospy
#HISTORIC ONLY
l_hist = [21.37, 45] #P then T
u_hist = [67.21, 61.9]

distribution = cp.J(cp.Uniform(l_hist[0], u_hist[0]),
                    cp.Uniform(l_hist[1], u_hist[1]))
num_hist = 50
samples_h = distribution.sample(size=num_hist, rule="L")
#print(samples_h)

hx = samples_h[0]
hy = samples_h[1]

#creates dataframe of p and t
hist_df = pd.DataFrame({'precipitation': hx,
                           'temperature': hy})
print(hist_df)

#pROJECTED DATA ONLY
l_proj = [26.34, 49.81] #P then T
u_proj = [88.78, 75.88]

distribution = cp.J(cp.Uniform(l_proj[0], u_proj[0]),
                    cp.Uniform(l_proj[1], u_proj[1]))
num_proj = 150
samples_p = distribution.sample(size=num_proj, rule="L")
#print(samples_p)

px = samples_p[0]
py = samples_p[1]

#creates dataframe of p and t
proj_df = pd.DataFrame({'precipitation': px,
                           'temperature': py})
print(proj_df)



#COMBINE HIST AND PROJ TO PLOT
fig, ax = plt.subplots()
ax.scatter(x = hist_df['precipitation'], y = hist_df['temperature'], color = 'indianred')
ax.scatter(x = proj_df['precipitation'], y = proj_df['temperature'], color = 'darkorange')

#ax.scatter(x, y, color = 'darkorange')
ax.set_xlabel('precipitation (in)')
ax.set_ylabel('temperature (F)')
ax.set_title('Latin-Hypercube Sample of Projected P & T')
plt.show()

#save the hist and proj latinhypercube samples to excel file
hist_df.to_excel("LHC_hist_sample.xlsx")
proj_df.to_excel("LHC_proj_sample.xlsx")
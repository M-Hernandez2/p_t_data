#February 27, 2023
#file to create time series and statisutical distributions of precipitation and temperature data
#from projected and historic data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#make pandas dataframe out of projected data for p & t
t_all = pd.read_excel("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ALL_T_p.xlsx", sheet_name='ssp_all')
p_all = pd.read_excel("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ALL_P_p.xlsx", sheet_name='ssp_all')

t_stats = pd.read_excel("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ALL_T_p.xlsx", sheet_name='ssp_values')
p_stats = pd.read_excel("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ALL_P_p.xlsx", sheet_name='ssp_values')

#NOAAs historic P and T data
t_hist = [53.4, 54.2, 53.5, 54.7, 54.9, 61.9, 52.7, 54.7, 55.3, 55.2, 56, 54.7, 57.3, 55, 54.9, 45, 57.1,
             54.4, 57.9, 55.5, 55.1, 53.7, 55.7, 54, 55.6, 55, 55.9, 56.4, 57.4, 56.8, 56.4, 54.7, 54.6, 55.1,
             55.4, 56.8, 56.7, 53.5, 56.8, 56.6, 54.4, 56.1, 56.3, 57, 56.9, 55.5, 59.6, 55.3, 56.7, 57.1, 59.5,
             57.2, 56.6, 57, 57.1, 54.4, 57.8, 55.4, 55.7, 54.7, 54.8, 56.5, 56.2, 55.6, 54.8, 55.8, 55.3, 55.5,
             56.2, 55.6, 57.5, 56.6, 57.1, 56.1, 57.1, 54.1, 57.5, 56.2, 55.5, 56.2, 57, 56.8, 57.6, 57.3, 57.7,
             58.7, 57.3, 58.9, 59.1, 55.9, 57.5, 56, 56.5, 55, 55.8, 58.1, 57.3, 55.4, 57, 58.2, 55.5, 57, 58.5,
             58.8, 57.7, 57.8, 59.1, 57.8, 58.8, 59, 56.2, 55.5, 57.6, 58.4, 58.5, 57.9, 58.1, 49.6, 45.7, 57.5,
             60.4]
p_hist = [41.19, 36.77, 42.58, 40.01, 44.6, 39.49, 48.96, 50.67, 57.9, 44.1, 32.21, 50.82, 34, 60.05, 39.25,
             48.11, 40.62, 43.48, 46.7, 35.86, 33.96, 36.04, 21.37, 37.27, 52.89, 33.52, 51.3, 35.87, 57.25,
             55.22, 40.1, 61.37, 40.56, 43.68, 35.59, 39.56, 58.69, 41.64, 46.74, 37.29, 36.2, 40.37, 62.82,
             41.67, 40.89, 39.63, 41.87, 47.64, 38.04, 61.9, 46.93, 42.05, 44.23, 51.48, 38.75, 51.49, 62.97,
             44.88, 44.44, 41.48, 52.58, 46.03, 49.07, 67.21, 44.04]


#TIME SERIES DATA
#plot time series from projected Temperature data
#plt.rcParams['figure.figsize'] = (14,7)
#t_all.plot(x='year', alpha=.4)
#plt.xlabel('years')
#plt.ylabel('temp (°F)')
#plt.title('CMIP6 Model Temperature Projections')
#plt.legend().set_visible(False)
#plt.set_cmap('Greys')
#plt.show()

#plot time series from projected Precipitation data
#plt.rcParams['figure.figsize'] = (14,7)
#p_all.plot(x='year', alpha=.4)
#plt.xlabel('years')
#plt.ylabel('precip (in/year)')
#plt.title('CMIP6 Models Precipitation Projections')
#plt.legend().set_visible(False)
#plt.set_cmap('Greys')
#plt.show()


#plot time series of min, max, mean for temperature data
#fig, ax = plt.subplots()
#ax.fill_between(t_stats['year'], t_stats['min'], t_stats['max'], alpha=0.4, linewidth=0, color='moccasin')
#ax.plot(t_stats['year'], t_stats['average'], linewidth=2, color='goldenrod', label='average')
#ax.legend(loc='upper left')
#plt.title('CMIP6 Models Temperature Projections')
#plt.xlabel('year')
#plt.ylabel('temp (°F)')
#plt.show()



#plot time series of min, max, mean for precipitation data
#fig, ax = plt.subplots()
#ax.fill_between(p_stats['year'], p_stats['min'], p_stats['max'], alpha=0.3, linewidth=0, color='forestgreen')
#ax.plot(p_stats['year'], p_stats['average'], linewidth=2, color='darkgreen', label='average')
#ax.legend(loc='upper left')
#plt.title('CMIP6 Models Precipitation Projections')
#plt.xlabel('year')
#plt.ylabel('precip (in/year)')
#plt.show()



#STATS TIME NOW
#temperature stat distribution
t_df_all = []
#remove missing values
t_all.dropna()
#print(t_all.head())

#make list with all temp values
t_all = t_all.drop('year', axis=1)
#print(t_all)

t_df_all = np.ravel(t_all.values).tolist()
#print(t_df_all)

#sort temp data for distribution
t_df_all.sort(reverse = True)
t_hist.sort(reverse = True)

th_count = []
tp_count = []
#print(len(t_df_all))

#make x axis for hist out of 100%
for i in range(0, len(t_hist)):
    th_count.append((i/121)*100)
#make x axis for projected temp data out of 100%
for i in range(0, len(t_df_all)):
    tp_count.append((i/14790)*100)

#plot the data
#plt.plot(th_count, t_hist, color = 'indianred')
#plt.plot(tp_count, t_df_all, color = 'goldenrod')
#plt.title('Annual Temperature Values Distribution')
#plt.xlabel('liklihood percent')
#plt.ylabel('temperature (°F)')
#plt.legend(['historical', 'projected'], loc = 'lower left')
#plt.show()


#plot Precipitation STAT DISTRIBUTION
p_df_all = []
#remove missing values
p_all = p_all.dropna()

#make list with all pr values
p_all = p_all.drop('year', axis=1)
#print(p_all)

p_df_all = np.ravel(p_all.values).tolist()

#sort pr data for distribution
p_df_all.sort(reverse = True)
#print(p_df_all)
p_hist.sort(reverse = True)

ph_count = []
pp_count = []
#print(len(p_df_all))

#historical range x values out of 100%
for i in range(0, len(p_hist)):
    ph_count.append((i/65)*100)
#projected range x values out of 100%
for i in range(0, len(p_df_all)):
    pp_count.append((i/13630)*100)

#plt.plot(ph_count, p_hist, color = 'indianred')
#plt.plot(pp_count, p_df_all, color = 'forestgreen')
#plt.title('Annual Precipitation Values Distribution')
#plt.xlabel('liklihood percent')
#plt.ylabel('precipitation (in/year)')
#plt.legend(['historical', 'projected'], loc = 'lower left')
#plt.show()


#VIOLIN PLOTS AND BOX PLOTS
#temperature
positions = [2, 3]
plt.figure(figsize=(8,6))
t1 = plt.violinplot([t_hist], positions=[2], showmeans=True, showmedians=True, showextrema=True, widths=0.9)
t2 = plt.violinplot([t_df_all], positions=[3], showmeans=True, showmedians=True, showextrema=True, widths=0.9)

#set shaded area color
for i in [t1,t2]:
    for patch in i['bodies']:
        patch.set_facecolor('lightcoral' if i == t1 else 'goldenrod')
        patch.set_edgecolor('black')

#set color for the lines
for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
    vp = t1[partname]
    vp.set_edgecolor('lightcoral')
    vp.set_linewidth(2)
for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
    vp = t2[partname]
    vp.set_edgecolor('goldenrod')
    vp.set_linewidth(2)

plt.title('Historic and Projected Temperature Distributions')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.xticks(positions, ['Historic', 'Projected'])
plt.show()

#precipitation
plt.figure(figsize=(8,6))
p1 = plt.violinplot([p_hist], positions=[2], showmeans=True, showmedians=True, showextrema=True, widths=0.9)
p2 = plt.violinplot([p_df_all], positions=[3], showmeans=True, showmedians=True, showextrema=True, widths=0.9)

for i in [p1,p2]:
    for patch in i['bodies']:
        patch.set_facecolor('lightcoral' if i == p1 else 'forestgreen')
        patch.set_edgecolor('black')

for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
    vp = p1[partname]
    vp.set_edgecolor('lightcoral')
    vp.set_linewidth(2)
for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
    vp = p2[partname]
    vp.set_edgecolor('forestgreen')
    vp.set_linewidth(2)

plt.title('Historic and Projected Precipitation Distributions')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.xticks(positions, ['Historic', 'Projected'])
plt.show()


#HISTOGRAM
#temperature
fig, ax = plt.subplots()
n, bins, patches = ax.hist(t_hist, 10, density=True)
y= ((1/np.sqrt(2*np.pi)*np.std(p_hist))*np.exp(-0.5*(1/np.std(p_hist)*(bins-np.mean(p_hist)))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('temp values')
ax.set_ylabel('Probability density')
ax.set_title('Normal Distribution of Historic Temperature Values')
fig.tight_layout()
plt.show()


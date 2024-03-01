#February 21, 2024
#Stat distribution of projected SLR for Dover, DE
#data from NASA sea level rise projections
#https://sealevel.nasa.gov/ipcc-ar6-sea-level-projection-tool


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

slr_total = pd.read_excel("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\SeaLevelRise\ipcc_ar6_slr.xlsx", sheet_name= 'SLR_total')
slr_rates = pd.read_excel("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\SeaLevelRise\ipcc_ar6_slr.xlsx", sheet_name= 'SLR_rate')

#create fill between plot of each scenario with line being the 50 interval and the shaded area being the 5-95 interval
#fig, ax = plt.subplots()
#ax.fill_between(slr_total['scenario'], slr_total['ssp26_05'], slr_total['ssp26_95'], alpha=0.3, linewidth=0, color='lightgreen')
#ax.plot(slr_total['scenario'], slr_total['ssp26_50'], linewidth=2, color='green', label='ssp_2.6')

#ax.fill_between(slr_total['scenario'], slr_total['ssp45_05'], slr_total['ssp45_95'], alpha=0.3, linewidth=0, color='khaki')
#ax.plot(slr_total['scenario'], slr_total['ssp45_50'], linewidth=2, color='gold', label='ssp_4.5')

#ax.fill_between(slr_total['scenario'], slr_total['ssp70_05'], slr_total['ssp70_95'], alpha=0.3, linewidth=0, color='sandybrown')
#ax.plot(slr_total['scenario'], slr_total['ssp70_50'], linewidth=2, color='orange', label='ssp_7.0')

#ax.fill_between(slr_total['scenario'], slr_total['ssp85_05'], slr_total['ssp85_95'], alpha=0.3, linewidth=0, color='tomato')
#ax.plot(slr_total['scenario'], slr_total['ssp85_50'], linewidth=2, color='orangered', label='ssp_8.5')

#ax.legend(loc='upper left')
#plt.title('Projected Total Sea Level Rise Scenarios')
#lt.xlabel('year')
#plt.ylabel('SLR (in)')
#plt.show()



#fig, ax = plt.subplots()
#ax.fill_between(slr_rates['scenario'], slr_rates['ssp26_05'], slr_rates['ssp26_95'], alpha=0.3, linewidth=0, color='lightgreen')
#ax.plot(slr_rates['scenario'], slr_rates['ssp26_50'], linewidth=2, color='green', label='ssp_2.6')

#ax.fill_between(slr_rates['scenario'], slr_rates['ssp45_05'], slr_rates['ssp45_95'], alpha=0.3, linewidth=0, color='khaki')
#ax.plot(slr_rates['scenario'], slr_rates['ssp45_50'], linewidth=2, color='gold', label='ssp_4.5')

#ax.fill_between(slr_rates['scenario'], slr_rates['ssp70_05'], slr_rates['ssp70_95'], alpha=0.3, linewidth=0, color='sandybrown')
#ax.plot(slr_rates['scenario'], slr_rates['ssp70_50'], linewidth=2, color='orange', label='ssp_7.0')

#ax.fill_between(slr_rates['scenario'], slr_rates['ssp85_05'], slr_rates['ssp85_95'], alpha=0.3, linewidth=0, color='tomato')
#ax.plot(slr_rates['scenario'], slr_rates['ssp85_50'], linewidth=2, color='orangered', label='ssp_8.5')

#ax.legend(loc='upper left')
#plt.title('Projected Rate of Sea Level Rise Scenarios')
#plt.xlabel('year')
#plt.ylabel('SLR (in/year)')
#plt.show()


#total sea level rise distribution
# stat distribution
slr_all = []
#remove missing values
slr_total.dropna()
print(slr_total.head())

#make list with all values
slr_total = slr_total.drop('scenario', axis=1)
print(slr_all)

slr_all = np.ravel(slr_total.values).tolist()

#sort  data for distribution
slr_all.sort(reverse = True)

count = []
print(slr_all)
print(len(slr_all))

#make x axis for hist out of 100%
for i in range(0, len(slr_all)):
    count.append((i/168)*100)

plt.plot(count, slr_all, color = 'yellowgreen')
plt.title('Sea Level Rise Projection Distribution')
plt.xlabel('liklihood percent')
plt.ylabel('SLR (in)')
plt.show()



#violin plot
positions = [0, 1]
plt.figure(figsize=(8,6))
slr1 = plt.violinplot([slr_all], positions=[1], showmeans=True, showmedians=True, showextrema=True, widths=0.9)

for i in [slr1]:
    for patch in i['bodies']:
        patch.set_facecolor('yellowgreen' if i == slr1 else 'black')
        patch.set_edgecolor('black')

#set color for the lines
for partname in ('cbars', 'cmins', 'cmaxes', 'cmeans', 'cmedians'):
    vp = slr1[partname]
    vp.set_edgecolor('olivedrab')
    vp.set_linewidth(2)

plt.title('Historic and Projected Temperature Distributions')
plt.xlabel('Groups')
plt.ylabel('Values')
plt.xticks(positions, ['Historic', 'Projected'])
plt.show()



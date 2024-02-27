#February 23, 2024
#opening netcdf files with all models of downscaled CMIP6 data for the NE coast of the USA
#https://psl.noaa.gov/ipcc/cmip6/timeseries6.html
#projected mean annual precipitation data for ssp 2.6, ssp 4.5, ssp7.0, ssp 8.5

import numpy as np
import pandas as pd
import xarray as xr

#open and upload netcdf files for porecipitation models for ssp 2.6 and ssp8.5
data_a = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p1.nc")
data_b = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p2.nc")
data_c = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p3.nc")
data_d = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p4.nc")
data_e = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p5.nc")
data_f = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p6.nc")
data_g = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p7.nc")
data_h = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p8.nc")
data_i = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p9.nc")
data_j = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p10.nc")
data_k = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p11.nc")
data_l = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p12.nc")
data_m = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p13.nc")
data_n = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p14.nc")
data_o = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p15.nc")
data_p = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p16.nc")
data_q = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p17.nc")
data_r = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p18.nc")
data_s = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p19.nc")
data_t = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p20.nc")
data_u = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p21.nc")
data_v = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p22.nc")
data_w = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p23.nc")
data_x = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\p24.nc")


#save the mean as a dataframe for ssp2.6 and convert to csv file
p2_1 = data_a['mean_ssp1'].to_dataframe()
p2_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_1.csv")

p2_2 = data_b['mean_ssp1'].to_dataframe()
p2_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_2.csv")

p2_3 = data_c['mean_ssp1'].to_dataframe()
p2_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_3.csv")

p2_4 = data_d['mean_ssp1'].to_dataframe()
p2_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_4.csv")

p2_5 = data_e['mean_ssp1'].to_dataframe()
p2_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_5.csv")

p2_6 = data_f['mean_ssp1'].to_dataframe()
p2_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_6.csv")

p2_7 = data_g['mean_ssp1'].to_dataframe()
p2_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_7.csv")

p2_8 = data_h['mean_ssp1'].to_dataframe()
p2_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_8.csv")

p2_9 = data_i['mean_ssp1'].to_dataframe()
p2_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_9.csv")

p2_10 = data_j['mean_ssp1'].to_dataframe()
p2_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_10.csv")

p2_11 = data_k['mean_ssp1'].to_dataframe()
p2_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_11.csv")

p2_12 = data_l['mean_ssp1'].to_dataframe()
p2_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_12.csv")

p2_13 = data_m['mean_ssp1'].to_dataframe()
p2_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_13.csv")

p2_14 = data_n['mean_ssp1'].to_dataframe()
p2_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_14.csv")

p2_15 = data_o['mean_ssp1'].to_dataframe()
p2_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_15.csv")

p2_16 = data_p['mean_ssp1'].to_dataframe()
p2_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_16.csv")

p2_17 = data_q['mean_ssp1'].to_dataframe()
p2_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_17.csv")

p2_18 = data_r['mean_ssp1'].to_dataframe()
p2_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_18.csv")

p2_19 = data_s['mean_ssp1'].to_dataframe()
p2_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_19.csv")

p2_20 = data_t['mean_ssp1'].to_dataframe()
p2_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_20.csv")

p2_21 = data_u['mean_ssp1'].to_dataframe()
p2_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_21.csv")

p2_22 = data_v['mean_ssp1'].to_dataframe()
p2_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_22.csv")

p2_23 = data_w['mean_ssp1'].to_dataframe()
p2_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_23.csv")

p2_24 = data_x['mean_ssp1'].to_dataframe()
p2_24.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P2_24.csv")



#save the mean for ssp8.5 and convert to csv file
p8_1 = data_a['mean_ssp2'].to_dataframe()
p8_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_1.csv")

p8_2 = data_b['mean_ssp2'].to_dataframe()
p8_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_2.csv")

p8_3 = data_c['mean_ssp2'].to_dataframe()
p8_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_3.csv")

p8_4 = data_d['mean_ssp2'].to_dataframe()
p8_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_4.csv")

p8_5 = data_e['mean_ssp2'].to_dataframe()
p8_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_5.csv")

p8_6 = data_f['mean_ssp2'].to_dataframe()
p8_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_6.csv")

p8_7 = data_g['mean_ssp2'].to_dataframe()
p8_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_7.csv")

p8_8 = data_h['mean_ssp2'].to_dataframe()
p8_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_8.csv")

p8_9 = data_i['mean_ssp2'].to_dataframe()
p8_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_9.csv")

p8_10 = data_j['mean_ssp2'].to_dataframe()
p8_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_10.csv")

p8_11 = data_k['mean_ssp2'].to_dataframe()
p8_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_11.csv")

p8_12 = data_l['mean_ssp2'].to_dataframe()
p8_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_12.csv")

p8_13 = data_m['mean_ssp2'].to_dataframe()
p8_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_13.csv")

p8_14 = data_n['mean_ssp2'].to_dataframe()
p8_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_14.csv")

p8_15 = data_o['mean_ssp2'].to_dataframe()
p8_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_15.csv")

p8_16 = data_p['mean_ssp2'].to_dataframe()
p8_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_16.csv")

p8_17 = data_q['mean_ssp2'].to_dataframe()
p8_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_17.csv")

p8_18 = data_r['mean_ssp2'].to_dataframe()
p8_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_18.csv")

p8_19 = data_s['mean_ssp2'].to_dataframe()
p8_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_19.csv")

p8_20 = data_t['mean_ssp2'].to_dataframe()
p8_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_20.csv")

p8_21 = data_u['mean_ssp2'].to_dataframe()
p8_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_21.csv")

p8_22 = data_v['mean_ssp2'].to_dataframe()
p8_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_22.csv")

p8_23 = data_w['mean_ssp2'].to_dataframe()
p8_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_23.csv")

p8_24 = data_x['mean_ssp2'].to_dataframe()
p8_24.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp2.6_8.5\P8_24.csv")


#open and upload netcdf files for porecipitation models for ssp 4.6 and ssp 7.0
data_a = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p1.nc")
data_b = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p2.nc")
data_c = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p3.nc")
data_d = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p4.nc")
data_e = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p5.nc")
data_f = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p6.nc")
data_g = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p7.nc")
data_h = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p8.nc")
data_i = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p9.nc")
data_j = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p10.nc")
data_k = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p11.nc")
data_l = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p12.nc")
data_m = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p13.nc")
data_n = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p14.nc")
data_o = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p15.nc")
data_p = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p16.nc")
data_q = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p17.nc")
data_r = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p18.nc")
data_s = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p19.nc")
data_t = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p20.nc")
data_u = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p21.nc")
data_v = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p22.nc")
data_w = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\p23.nc")

#save the mean as a dataframe for ssp2.6 and convert to csv file
p4_1 = data_a['mean_ssp1'].to_dataframe()
p4_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_1.csv")

p4_2 = data_b['mean_ssp1'].to_dataframe()
p4_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_2.csv")

p4_3 = data_c['mean_ssp1'].to_dataframe()
p4_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_3.csv")

p4_4 = data_d['mean_ssp1'].to_dataframe()
p4_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_4.csv")

p4_5 = data_e['mean_ssp1'].to_dataframe()
p4_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_5.csv")

p4_6 = data_f['mean_ssp1'].to_dataframe()
p4_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_6.csv")

p4_7 = data_g['mean_ssp1'].to_dataframe()
p4_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_7.csv")

p4_8 = data_h['mean_ssp1'].to_dataframe()
p4_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_8.csv")

p4_9 = data_i['mean_ssp1'].to_dataframe()
p4_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_9.csv")

p4_10 = data_j['mean_ssp1'].to_dataframe()
p4_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_10.csv")

p4_11 = data_k['mean_ssp1'].to_dataframe()
p4_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_11.csv")

p4_12 = data_l['mean_ssp1'].to_dataframe()
p4_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_12.csv")

p4_13 = data_m['mean_ssp1'].to_dataframe()
p4_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_13.csv")

p4_14 = data_n['mean_ssp1'].to_dataframe()
p4_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_14.csv")

p4_15 = data_o['mean_ssp1'].to_dataframe()
p4_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_15.csv")

p4_16 = data_p['mean_ssp1'].to_dataframe()
p4_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_16.csv")

p4_17 = data_q['mean_ssp1'].to_dataframe()
p4_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_17.csv")

p4_18 = data_r['mean_ssp1'].to_dataframe()
p4_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_18.csv")

p4_19 = data_s['mean_ssp1'].to_dataframe()
p4_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_19.csv")

p4_20 = data_t['mean_ssp1'].to_dataframe()
p4_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_20.csv")

p4_21 = data_u['mean_ssp1'].to_dataframe()
p4_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_21.csv")

p4_22 = data_v['mean_ssp1'].to_dataframe()
p4_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_22.csv")

p4_23 = data_w['mean_ssp1'].to_dataframe()
p4_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P4_23.csv")


#save the mean as a dataframe for ssp7.0 and convert to csv file
p7_1 = data_a['mean_ssp2'].to_dataframe()
p7_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_1.csv")

p7_2 = data_b['mean_ssp2'].to_dataframe()
p7_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_2.csv")

p7_3 = data_c['mean_ssp2'].to_dataframe()
p7_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_3.csv")

p7_4 = data_d['mean_ssp2'].to_dataframe()
p7_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_4.csv")

p7_5 = data_e['mean_ssp2'].to_dataframe()
p7_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_5.csv")

p7_6 = data_f['mean_ssp2'].to_dataframe()
p7_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_6.csv")

p7_7 = data_g['mean_ssp2'].to_dataframe()
p7_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_7.csv")

p7_8 = data_h['mean_ssp2'].to_dataframe()
p7_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_8.csv")

p7_9 = data_i['mean_ssp2'].to_dataframe()
p7_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_9.csv")

p7_10 = data_j['mean_ssp2'].to_dataframe()
p7_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_10.csv")

p7_11 = data_k['mean_ssp2'].to_dataframe()
p7_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_11.csv")

p7_12 = data_l['mean_ssp2'].to_dataframe()
p7_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_12.csv")

p7_13 = data_m['mean_ssp2'].to_dataframe()
p7_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_13.csv")

p7_14 = data_n['mean_ssp2'].to_dataframe()
p7_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_14.csv")

p7_15 = data_o['mean_ssp2'].to_dataframe()
p7_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_15.csv")

p7_16 = data_p['mean_ssp2'].to_dataframe()
p7_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_16.csv")

p7_17 = data_q['mean_ssp2'].to_dataframe()
p7_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_17.csv")

p7_18 = data_r['mean_ssp2'].to_dataframe()
p7_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_18.csv")

p7_19 = data_s['mean_ssp2'].to_dataframe()
p7_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_19.csv")

p7_20 = data_t['mean_ssp2'].to_dataframe()
p7_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_20.csv")

p7_21 = data_u['mean_ssp2'].to_dataframe()
p7_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_21.csv")

p7_22 = data_v['mean_ssp2'].to_dataframe()
p7_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_22.csv")

p7_23 = data_w['mean_ssp2'].to_dataframe()
p7_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_P_proj\ssp4.5_7.0\P7_23.csv")




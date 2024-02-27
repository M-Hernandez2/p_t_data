#February 22, 2024
#opening netcdf files with all models of downscaled CMIP6 data for the NE coast of the USA
#https://psl.noaa.gov/ipcc/cmip6/timeseries6.html
#projected mean annual temperature data for ssp 2.6, ssp 4.5, ssp7.0, ssp 8.5

import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#open and upload netcdf files for temperature models for ssp 2.6 and ssp8.5
data_a = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\ccess_t.nc")
data_b = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\ccess_esm_t.nc")
data_c = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\wi_cm_t.nc")
data_d = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\cc_csm_t.nc")
data_e = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\canesm_t.nc")
data_f = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\cnrm_hr_t.nc")
data_g = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\cnrm_cm_t.nc")
data_h = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\cnrme_t.nc")
data_i = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\earth_t.nc")
data_j = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\earthveg_t.nc")
data_k = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\goals_t.nc")
data_l = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\goalsg_t.nc")
data_m = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\gio_t.nc")
data_n = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\gfdl_t.nc")
data_o = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\giss_t.nc")
data_p = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\hadgem_t.nc")
data_q = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\inm_t.nc")
data_r = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\inm_cm_t.nc")
data_s = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\ipsl_t.nc")
data_t = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\kace_t.nc")
data_u = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\mcm_t.nc")
data_v = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\micro_t.nc")
data_w = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\microes_t.nc")
data_x = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\mpi_t.nc")
data_y = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\mpilr_t.nc")
data_z = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\mri_t.nc")

#save the mean as a dataframe for ssp2.6 and convert to csv file
t2_1 = data_a['mean_ssp1'].to_dataframe()
t2_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_1.csv")

t2_2 = data_b['mean_ssp1'].to_dataframe()
t2_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_2.csv")

t2_3 = data_c['mean_ssp1'].to_dataframe()
t2_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_3.csv")

t2_4 = data_d['mean_ssp1'].to_dataframe()
t2_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_4.csv")

t2_5 = data_e['mean_ssp1'].to_dataframe()
t2_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_5.csv")

t2_6 = data_f['mean_ssp1'].to_dataframe()
t2_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_6.csv")

t2_7 = data_g['mean_ssp1'].to_dataframe()
t2_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_7.csv")

t2_8 = data_h['mean_ssp1'].to_dataframe()
t2_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_8.csv")

t2_9 = data_i['mean_ssp1'].to_dataframe()
t2_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_9.csv")

t2_10 = data_j['mean_ssp1'].to_dataframe()
t2_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_10.csv")

t2_11 = data_k['mean_ssp1'].to_dataframe()
t2_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_11.csv")

t2_12 = data_l['mean_ssp1'].to_dataframe()
t2_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_12.csv")

t2_13 = data_m['mean_ssp1'].to_dataframe()
t2_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_13.csv")

t2_14 = data_n['mean_ssp1'].to_dataframe()
t2_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_14.csv")

t2_15 = data_o['mean_ssp1'].to_dataframe()
t2_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_15.csv")

t2_16 = data_p['mean_ssp1'].to_dataframe()
t2_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_16.csv")

t2_17 = data_q['mean_ssp1'].to_dataframe()
t2_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_17.csv")

t2_18 = data_r['mean_ssp1'].to_dataframe()
t2_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_18.csv")

t2_19 = data_s['mean_ssp1'].to_dataframe()
t2_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_19.csv")

t2_20 = data_t['mean_ssp1'].to_dataframe()
t2_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_20.csv")

t2_21 = data_u['mean_ssp1'].to_dataframe()
t2_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_21.csv")

t2_22 = data_v['mean_ssp1'].to_dataframe()
t2_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_22.csv")

t2_23 = data_w['mean_ssp1'].to_dataframe()
t2_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_23.csv")

t2_24 = data_x['mean_ssp1'].to_dataframe()
t2_24.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_24.csv")

t2_25 = data_y['mean_ssp1'].to_dataframe()
t2_25.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_25.csv")

t2_26 = data_z['mean_ssp1'].to_dataframe()
t2_26.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T2_26.csv")


#save the mean for ssp8.5 and convert to csv file
t8_1 = data_a['mean_ssp2'].to_dataframe()
t8_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_1.csv")

t8_2 = data_b['mean_ssp2'].to_dataframe()
t8_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_2.csv")

t8_3 = data_c['mean_ssp2'].to_dataframe()
t8_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_3.csv")

t8_4 = data_d['mean_ssp2'].to_dataframe()
t8_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_4.csv")

t8_5 = data_e['mean_ssp2'].to_dataframe()
t8_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_5.csv")

t8_6 = data_f['mean_ssp2'].to_dataframe()
t8_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_6.csv")

t8_7 = data_g['mean_ssp2'].to_dataframe()
t8_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_7.csv")

t8_8 = data_h['mean_ssp2'].to_dataframe()
t8_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_8.csv")

t8_9 = data_i['mean_ssp2'].to_dataframe()
t8_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_9.csv")

t8_10 = data_j['mean_ssp2'].to_dataframe()
t8_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_10.csv")

t8_11 = data_k['mean_ssp2'].to_dataframe()
t8_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_11.csv")

t8_12 = data_l['mean_ssp2'].to_dataframe()
t8_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_12.csv")

t8_13 = data_m['mean_ssp2'].to_dataframe()
t8_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_13.csv")

t8_14 = data_n['mean_ssp2'].to_dataframe()
t8_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_14.csv")

t8_15 = data_o['mean_ssp2'].to_dataframe()
t8_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_15.csv")

t8_16 = data_p['mean_ssp2'].to_dataframe()
t8_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_16.csv")

t8_17 = data_q['mean_ssp2'].to_dataframe()
t8_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_17.csv")

t8_18 = data_r['mean_ssp2'].to_dataframe()
t8_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_18.csv")

t8_19 = data_s['mean_ssp2'].to_dataframe()
t8_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_19.csv")

t8_20 = data_t['mean_ssp2'].to_dataframe()
t8_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_20.csv")

t8_21 = data_u['mean_ssp2'].to_dataframe()
t8_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_21.csv")

t8_22 = data_v['mean_ssp2'].to_dataframe()
t8_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_22.csv")

t8_23 = data_w['mean_ssp2'].to_dataframe()
t8_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_23.csv")

t8_24 = data_x['mean_ssp2'].to_dataframe()
t8_24.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_24.csv")

t8_25 = data_y['mean_ssp2'].to_dataframe()
t8_25.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_25.csv")

t8_26 = data_z['mean_ssp2'].to_dataframe()
t8_26.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T8_26.csv")

#open and upload netcdf files for temperature models for ssp 4.5 and ssp 7.0
data_a = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T1.nc")
data_b = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T2.nc")
data_c = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T3.nc")
data_d = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4.nc")
data_e = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T5.nc")
data_f = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T6.nc")
data_g = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T7.nc")
data_h = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T8.nc")
data_i = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T9.nc")
data_j = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T10.nc")
data_k = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T11.nc")
data_l = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T12.nc")
data_m = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T13.nc")
data_n = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T14.nc")
data_o = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T15.nc")
data_p = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T16.nc")
data_q = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T17.nc")
data_r = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T18.nc")
data_s = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T19.nc")
data_t = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T20.nc")
data_u = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T21.nc")
data_v = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T22.nc")
data_w = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T23.nc")
data_x = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T24.nc")
data_y = xr.open_dataset("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T25.nc")

#save the mean as a dataframe for ssp4.5 and convert to csv file
t4_1 = data_a['mean_ssp1'].to_dataframe()
t4_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_1.csv")

t4_2 = data_b['mean_ssp1'].to_dataframe()
t4_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_2.csv")

t4_3 = data_c['mean_ssp1'].to_dataframe()
t4_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_3.csv")

t4_4 = data_d['mean_ssp1'].to_dataframe()
t4_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_4.csv")

t4_5 = data_e['mean_ssp1'].to_dataframe()
t4_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_5.csv")

t4_6 = data_f['mean_ssp1'].to_dataframe()
t4_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_6.csv")

t4_7 = data_g['mean_ssp1'].to_dataframe()
t4_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_7.csv")

t4_8 = data_h['mean_ssp1'].to_dataframe()
t4_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_8.csv")

t4_9 = data_i['mean_ssp1'].to_dataframe()
t4_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_9.csv")

t4_10 = data_j['mean_ssp1'].to_dataframe()
t4_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_10.csv")

t4_11 = data_k['mean_ssp1'].to_dataframe()
t4_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_11.csv")

t4_12 = data_l['mean_ssp1'].to_dataframe()
t4_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_12.csv")

t4_13 = data_m['mean_ssp1'].to_dataframe()
t4_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_13.csv")

t4_14 = data_n['mean_ssp1'].to_dataframe()
t4_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_14.csv")

t4_15 = data_o['mean_ssp1'].to_dataframe()
t4_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_15.csv")

t4_16 = data_p['mean_ssp1'].to_dataframe()
t4_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_16.csv")

t4_17 = data_q['mean_ssp1'].to_dataframe()
t4_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_17.csv")

t4_18 = data_r['mean_ssp1'].to_dataframe()
t4_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_18.csv")

t4_19 = data_s['mean_ssp1'].to_dataframe()
t4_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_19.csv")

t4_20 = data_t['mean_ssp1'].to_dataframe()
t4_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_20.csv")

t4_21 = data_u['mean_ssp1'].to_dataframe()
t4_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_21.csv")

t4_22 = data_v['mean_ssp1'].to_dataframe()
t4_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_22.csv")

t4_23 = data_w['mean_ssp1'].to_dataframe()
t4_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_23.csv")

t4_24 = data_x['mean_ssp1'].to_dataframe()
t4_24.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_24.csv")

t4_25 = data_y['mean_ssp1'].to_dataframe()
t4_25.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp4.5_7.0\T4_25.csv")

#save the mean for ssp7.0 and convert to csv file
t7_1 = data_a['mean_ssp2'].to_dataframe()
t7_1.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_1.csv")

t7_2 = data_b['mean_ssp2'].to_dataframe()
t7_2.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_2.csv")

t7_3 = data_c['mean_ssp2'].to_dataframe()
t7_3.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_3.csv")

t7_4 = data_d['mean_ssp2'].to_dataframe()
t7_4.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_4.csv")

t7_5 = data_e['mean_ssp2'].to_dataframe()
t7_5.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_5.csv")

t7_6 = data_f['mean_ssp2'].to_dataframe()
t7_6.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_6.csv")

t7_7 = data_g['mean_ssp2'].to_dataframe()
t7_7.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_7.csv")

t7_8 = data_h['mean_ssp2'].to_dataframe()
t7_8.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_8.csv")

t7_9 = data_i['mean_ssp2'].to_dataframe()
t7_9.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_9.csv")

t7_10 = data_j['mean_ssp2'].to_dataframe()
t7_10.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_10.csv")

t7_11 = data_k['mean_ssp2'].to_dataframe()
t7_11.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_11.csv")

t7_12 = data_l['mean_ssp2'].to_dataframe()
t7_12.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_12.csv")

t7_13 = data_m['mean_ssp2'].to_dataframe()
t7_13.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_13.csv")

t7_14 = data_n['mean_ssp2'].to_dataframe()
t7_14.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_14.csv")

t7_15 = data_o['mean_ssp2'].to_dataframe()
t7_15.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_15.csv")

t7_16 = data_p['mean_ssp2'].to_dataframe()
t7_16.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_16.csv")

t7_17 = data_q['mean_ssp2'].to_dataframe()
t7_17.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_17.csv")

t7_18 = data_r['mean_ssp2'].to_dataframe()
t7_18.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_18.csv")

t7_19 = data_s['mean_ssp2'].to_dataframe()
t7_19.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_19.csv")

t7_20 = data_t['mean_ssp2'].to_dataframe()
t7_20.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_20.csv")

t7_21 = data_u['mean_ssp2'].to_dataframe()
t7_21.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_21.csv")

t7_22 = data_v['mean_ssp2'].to_dataframe()
t7_22.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_22.csv")

t7_23 = data_w['mean_ssp2'].to_dataframe()
t7_23.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_23.csv")

t7_24 = data_x['mean_ssp2'].to_dataframe()
t7_24.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_24.csv")

t7_25 = data_y['mean_ssp2'].to_dataframe()
t7_25.to_csv("C:/Users\mjh7517\OneDrive - The Pennsylvania State University\Downloads\SWI Research\ALL_T_proj\ssp2.6_8.5\T7_25.csv")


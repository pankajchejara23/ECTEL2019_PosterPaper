import pandas as pd
import numpy as np
import prince

from sklearn.preprocessing import StandardScaler

# open dataset file
data_18oct = pd.read_csv('ProcessedData_ProjectDay_20171018.csv')
data_8nov = pd.read_csv('ProcessedData_ProjectDay_20171108.csv')
data_22nov = pd.read_csv('ProcessedData_ProjectDay_20171122.csv')
data_6dec = pd.read_csv('ProcessedData_ProjectDay_20171206.csv')

groups ={'physical':['disengaged','looking','talking','intTech','intRes','intExt'],'logs':['Accessed','Create','Open','Update']}
groups1 ={'physical':['disengaged','looking','talking','intTech','intRes','intExt'],'logs':['Accessed']}

group_all = {'disengaged','looking','talking','intTech','intRes','intExt','Accessed','Create','Open','Update'}
group_partial = {'disengaged','looking','talking','intTech','intRes','intExt','Accessed'}

scaler1 = StandardScaler()
scaler2 = StandardScaler()
scaler3 = StandardScaler()
scaler4 = StandardScaler()



data_ready_18oct = data_18oct.drop(data_18oct.columns[[0,1,2]],axis=1)
data_ready_8nov = data_8nov.drop(data_8nov.columns[[0,1,2]],axis=1)
data_ready_22nov = data_22nov.drop(data_22nov.columns[[0,1,2]],axis=1)
data_ready_6dec = data_6dec.drop(data_6dec.columns[[0,1]],axis=1)

data_ready_22nov.dropna(axis=0,how="any",inplace=True)

data_ready_18oct = pd.DataFrame(scaler1.fit_transform(data_ready_18oct),columns=group_all)
data_ready_8nov = pd.DataFrame(scaler2.fit_transform(data_ready_8nov),columns=group_all)
data_ready_22nov = pd.DataFrame(scaler3.fit_transform(data_ready_22nov),columns=group_all)
data_ready_6dec = pd.DataFrame(scaler4.fit_transform(data_ready_6dec),columns=group_partial)




#famd = prince.FAMD(n_components = 2)
mfa1 = prince.MFA(groups=groups,n_components=2)
mfa2 = prince.MFA(groups=groups,n_components=2)
mfa3 = prince.MFA(groups=groups,n_components=2)
mfa4 = prince.MFA(groups=groups1,n_components=2)

#famd_result = famd.fit_transform(std_data_8nov)
mfa_result_18oct = mfa1.fit_transform(data_ready_18oct)
mfa_result_8nov = mfa2.fit_transform(data_ready_8nov)
mfa_result_22nov = mfa3.fit_transform(data_ready_22nov)
mfa_result_6dec = mfa4.fit_transform(data_ready_6dec)

#famd.to_csv('famd_result.csv')
mfa_result_18oct.to_csv('mfa_result_18oct.csv')
mfa_result_8nov.to_csv('mfa_result_8nov.csv')
mfa_result_22nov.to_csv('mfa_result_22nov.csv')
mfa_result_6dec.to_csv('mfa_result_6dec.csv')

import numpy as np
import pandas as pd
import re
# df_err= pd.read_csv(r'C:/Users/User/Desktop/DELL/SmartLogger/Dataset_ver2.csv',nrows=20000)
df_err= pd.read_csv(r'C:/Users/User/Desktop/DELL/SmartLogger/Ux_apps_errors.csv')

# df_info=df1[df1['level']=='info']
# df_err=df1[df1['level']=='error']
# df_warn=df1[df1['level']=='warn']
# df_info['Info']=np.nan


df_err['Error Message']=np.nan
df_err['Exception Details']=np.nan
df_err['Exception Name']=np.nan
# df_err['x22']=np.nan
# df_err['x31']=np.nan
# df_err['x32']=np.nan
df_err['Others']=np.nan

# df_warn['Warning']=np.nan
# df_warn['Warning Title']=np.nan
# df_warn['Others']=np.nan

# print(df_info)
# for i in df_info.index:
    # x=re.search(r'^Sec(.*)Detail$',df_info['@message'][i])
    # print(x)

    # if x is not None:
    #     print(x.group(1))
    # if df_info['@message'][i].startswith("[Sec") and df_info['@message'][i].endswith("]"):
    #     print(df_info['@message'][i])  


# for i in df_info.index:
#     x= re.search(r'49m:(.*)',df_info['@message'][i]) 
#     # print(x)
#     if x is not None:
#         df_info['Info'][i]= x.group(1)
#         # print(df_info['x1'][i])
#         continue
#     x=re.search(r'"(.*),',df_info['@message'][i])
#     if x is not None:
#         df_info['Info'][i]= x.group(1)
#         # print(df_info['x2'][i])
#         continue
 
 
#     df_info['Info'][i]=df_info['@message'][i]
# # print(df_info.head())

for i in df_err.index:
    x=re.search(r'message-data-start =>(.*)message-data-end',df_err['@message'][i])
    if x is not None:
        df_err['Error Message'][i]= x.group(1)
        y=re.search(r'exception-data-start =>(.*)exception-data-end',df_err['@message'][i])
        # print(df_err['x11'][i])
        if y is not None:
            df_err['Exception Details'][i]=y.group(1)
            z=re.search(r'exception-data-start => (.*?):',df_err['@message'][i])
            if z is not None:
                df_err['Exception Name'][i]=z.group(1)
        continue
    x=re.search(r'Error calling method:(.*)Ex',df_err['@message'][i])
    if x is not None:
        df_err['Error Message'][i]= x.group(1)
        y=re.search(r'Ex:(.*)',df_err['@message'][i])
        if y is not None:
            df_err['Exception Details'][i]=y.group(1)
            z=re.search(r'Ex:(.*).',df_err['@message'][i])
            if z is not None:
                pos=z.group(1).find('.')
                if pos== -1:
                    pos=len(z.group(1))
                df_err['Exception Name'][i]=z.group(1)[:pos]
                print(z.group(1))
        continue
    x=re.search(r'Error(.*)?fromDate',df_err['@message'][i])
    if x is not None:
        df_err['Error Message'][i]= x.group(1)
        y=re.search(r'Exception =(.*)',df_err['@message'][i])
        if y is not None:
           df_err['Exception Details'][i]= y.group(1)
           z=re.search(r'=>(.*?):',df_err['@message'][i])
           if z is not None:
                df_err['Exception Name'][i]=z.group(1)
        continue
 
    df_err['Others'][i]=df_err['@message'][i]
# print(df_err.head())

# for i in df_warn.index:
#     x=re.search(r'49m:(.*)',df_warn['@message'][i])
#     if x is not None:
#         df_warn['Warning'][i]= x.group(1)
#         # print(df_warn['x1'][i])
#         continue
#     x=re.search(r'Warning(.*)]',df_warn['@message'][i])
#     if x is not None:
#         df_warn['Warning'][i]= x.group(1)+str(']')
#         # print(df_warn['x2'][i])
#         continue
#     df_warn['Others'][i]=df_warn['@message'][i]
# # print(df_warn['x3'][i])
# # print(df_warn.head())
# # print(df_info.head())
# # print(df_err.head())
# # print(df_warn.head())
# df_info.to_csv('Info2.csv')
df_err.to_csv('UX_Error.csv')
# df_warn.to_csv('Warn2.csv')
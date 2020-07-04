# import numpy as np
# import pandas as pd
import re


def error_clean(df_err):

    x = re.search(r'message-data-start =>(.*)message-data-end',
                  df_err['message'])
    if x is not None:
        df_err['Error_Message'] = x.group(1)
        y = re.search(
            r'exception-data-start =>(.*)exception-data-end', df_err['message'])
    # print(df_err['x11'][i])
        if y is not None:
            df_err['Exception_Details'] = y.group(1)
            z = re.search(r'exception-data-start => (.*?):', df_err['message'])
            if z is not None:
               df_err['Exception_Name'] = z.group(1)
    else:
        x = re.search(r'Error calling method:(.*)Ex', df_err['message'])
        if x is not None:
            df_err['Error_Message'] = x.group(1)
            y = re.search(r'Ex:(.*)', df_err['message'])
            if y is not None:
                df_err['Exception_Details'] = y.group(1)
                z = re.search(r'Ex:(.*).', df_err['message'])
                if z is not None:
                    pos = z.group(1).find('.')
                    if pos == -1:
                        pos = len(z.group(1))
                    df_err['Exception_Name'] = z.group(1)[:pos]
                # print(z.group(1))
        else:
            x = re.search(r'Error(.*)?fromDate', df_err['message'])
            if x is not None:
                df_err['Error_Message'] = x.group(1)
                y = re.search(r'Exception =(.*)', df_err['message'])
                if y is not None:
                    df_err['Exception_Details'] = y.group(1)
                    z = re.search(r'=>(.*?):', df_err['message'])
                    if z is not None:
                        df_err['Exception_Name'] = z.group(1)
            else:
                df_err['Error_Message'] = "Null"
                df_err['Exception_Details'] = "Null"
                df_err['Exception_Name'] = 'Generic Exception'
    # df_err['Others'][i]=df_err['message'][i]

# df_err.to_csv('UX_Error.csv')
    return df_err

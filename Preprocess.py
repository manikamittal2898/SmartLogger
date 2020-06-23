import numpy as np
import pandas as pd
import re
log_data= pd.read_csv(r'C:/Users/User/Desktop/DELL/filtered_data_June.csv')
# print(log_data.head())
# print(list(log_data.columns))
# print(log_data.cf_app_name.unique())
# print(log_data.cf_app_name.nunique(dropna=True))
# print(log_data.shortmessage.unique())
# print(log_data.shortmessage.nunique(dropna=True))
# num_of_rows=len(log_data.axes[0])
# print("Number of rows is "+ str(num_of_rows))
df=log_data.groupby('cf_app_name').agg(lambda x: list(x))
df.drop(['source_instance'],axis=1)
print(df)
print(list(df.columns))
for i in log_data.index:
    # print(df['shortmessage'][i])
    # print('\n')
   x= re.search(r'message-data-start =>(.*)message-data-end',log_data['shortmessage'][i])
#    x= re.search(r'\s',log_data['shortmessage'][i])
   if x is not None:
       print(x.group(1))
#    pos1
#    if not x:
#        print("\n")
#     else:
#         print(x)

# with open("/home/manika/Desktop/Dell/filtered_data_June.csv") as csvDataFile:
#     data = [row for row in csv.reader(csvDataFile)]
#     data=data[1:5]
# lemmatizer= WordNetLemmatizer()
# # def lemmatize_stemming(text):
# #     return lemmatizer.lemmatize(text) 
# def preprocess(text):
#     result = ""
#     for token in gensim.utils.simple_preprocess(text):
#         if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
#             result=result+" "+lemmatize_stemming(token)
#     return result

# flag=-1

# listofrows=[]
# for rows in data:
#     flag+=1
#     flag2=-1
#     for columns in rows:
#         col=[]
#         flag2+=1
#         doc_sample = data[flag][flag2]
#         # print(doc_sample)
#         print('original document: ')
#         # words = []
#         # for word in doc_sample.split(' '):
#         #     words.append(word)
#         #     # if words.count==0:
#         #     #     continue
#         #     # else: 
#         print(doc_sample)
#         print('\n\n tokenized and lemmatized document: ')
#         print(preprocess(doc_sample))
#         col.append(preprocess(doc_sample))
#     listofrows.append(col)
 	
# # Creating a dataframe object from listoftuples
# # dfObj = pd.DataFrame(students,) 
# final_doc=pd.DataFrame(listofrows)
# final_doc.to_csv('file1.csv')
import pandas as pd
import numpy as np

def unique_value(df):
    columns = list(df.columns)
    for i in columns:
        print(i)
        print('고유한 데이터의 수:', df[i].nunique())
        print('총 비율:', len(df[i].unique()) / len(crawled)) #처음에 json파일의 이름이 곧 상품몰의 이름)
        print('고유한 데이터:',df[i].unique())
        print("\n")

#Null인 것 True
def Null_value(df,wanted_column):    
    print(df[df[wanted_column].isnull()==True])
    
#Null인 False
def Null_value(df,wanted_column):    
    print(df[df[wanted_column].isnull()==False])
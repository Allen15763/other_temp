# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 15:14:54 2020

@author: allenli
"""

import os 
import pandas as pd

# 讀取 N個excel 檔案
path = 'C:/Data/pantest/'
files = os.listdir(path)
files_xlsx = list(filter(lambda x: x[-5:]=='.xlsx' , files)) #[取幾個檔案]

#定義一個空列表
data_list = []

for file in  files_xlsx:
    tmp = pd.read_excel(path + file, sheet_name="Void")
    data_list.append(tmp)
    
#print(data_list[0])
print(files_xlsx)
#all_data = pd.concat(data_list) 會所有檔案的df混在一起

def test(data_list):
    collecta = []
    collectb = []
    c = []
    d = []
    for df in range(1):
        pd.set_option("display.precision", 2)
        pd.set_option("display.max_colwidth", 12)
        df_mask1 = data_list[df][data_list[df]["符合Flag1或Flag2或Flag3任一條件且Flag4_Rate少於0_5_建議查核交易為T"] == "T"] 
        c.append([files_xlsx[:][df][:5]])
        d.append([df_mask1["交易時間"].nunique()])          
        print('\n', "店號", files_xlsx[:][df][:5])
        print("建議查核筆數", df_mask1["交易時間"].nunique())

        x = [x for x in df_mask1["收銀員"].unique()]
        data_list[df]["Total"] = data_list[df]["單價"] * data_list[df]["數量"]
        print("基本銷售額", data_list[df]["Total"].sum())
        print("最大單項位置", data_list[df]["Total"].idxmax() + 2, "金額", data_list[df]["Total"].max())

        df_mask2 = data_list[df][data_list[df]["收銀員"].isin(x)]
        a = df_mask2.groupby(["收銀員", "交易型態"]).交易時間.agg(['nunique', 'count']).unstack()
        b = df_mask2.groupby(["收銀員", "交易型態"]).Total.agg(['sum']).unstack()
        print(a)
        print(b)
        # c.append(c)
        # d.append(d)
        collecta.append(a)
        collectb.append(b)
    return c, d, collecta, collectb

#print(type(test(data_list)))
print(test(data_list))


#test(data_list).to_csv("123.csv", encoding="utf-8")
def timetree(data_list):
    cc = []
    dd = []
    A24L = []
    dic = {
        "店號" : cc,
        "建議查核筆數" : dd,
        "24點" : A24L,
        
        }
    for df in range(1):
        pd.set_option("display.precision", 2)
        pd.set_option("display.max_colwidth", 12)
        df_mask1 = data_list[df][data_list[df]["符合Flag1或Flag2或Flag3任一條件且Flag4_Rate少於0_5_建議查核交易為T"] == "T"] 
        cc.append([files_xlsx[:][df][:5]])
        dd.append([df_mask1["交易時間"].nunique()])          
        print('\n', "店號", files_xlsx[:][df][:5])
        print("建議查核筆數", df_mask1["交易時間"].nunique())

        data_list[df]['交易時間'] = pd.to_datetime(data_list[df]['交易時間'], format='%Y/%m/%d %H:%M:%S')
        data_list[df].set_index('交易時間', inplace=True, drop=True)
        # df_mask2 = data_list[df][data_list[df]["交易型態"] == "Void_Tran"] | data_list[df][data_list[df]["交易型態"] == "Void_Item"]
        df_mask3 = data_list[df][data_list[df]["交易型態"] == "Void_Tran"] 
        df_mask4 = data_list[df][data_list[df]["交易型態"] == "Void_Item"] 
        df_mask2 = pd.concat([df_mask3, df_mask4])
        
        print(len(data_list[df].between_time('0:00', '1:00:59')))
        print(len(data_list[df].between_time('1:01', '2:00:59')))
        print(len(data_list[df].between_time('2:01', '3:00:59')))
        print(len(data_list[df].between_time('3:01', '4:00:59')))
        print(len(data_list[df].between_time('4:01', '5:00:59')))
        print(len(data_list[df].between_time('5:01', '6:00:59')))
        print(len(data_list[df].between_time('6:01', '7:00:59')))
        print(len(data_list[df].between_time('7:01', '8:00:59')))
        print(len(data_list[df].between_time('8:01', '9:00:59')))
        print(len(data_list[df].between_time('9:01', '10:00:59')))
        print(len(data_list[df].between_time('10:01', '11:00:59')))
        print(len(data_list[df].between_time('11:01', '12:00:59')))
        print(len(data_list[df].between_time('12:01', '13:00:59')))
        print(len(data_list[df].between_time('13:01', '14:00:59')))
        print(len(data_list[df].between_time('14:01', '15:00:59')))
        print(len(data_list[df].between_time('15:01', '16:00:59')))
        print(len(data_list[df].between_time('16:01', '17:00:59')))
        print(len(data_list[df].between_time('17:01', '18:00:59')))
        print(len(data_list[df].between_time('18:01', '19:00:59')))
        print(len(data_list[df].between_time('19:01', '20:00:59'))) # peak
        print(len(data_list[df].between_time('20:01', '21:00:59')))
        print(len(data_list[df].between_time('21:01', '22:00:59')))
        print(len(data_list[df].between_time('22:01', '23:00:59')))
        print(len(data_list[df].between_time('23:01', '23:59:59')))
        print("分隔線--------")
        print(len(df_mask2.between_time('0:00', '1:00:59')))
        print(len(df_mask2.between_time('1:01', '2:00:59')))
        print(len(df_mask2.between_time('2:01', '3:00:59')))
        print(len(df_mask2.between_time('3:01', '4:00:59')))
        print(len(df_mask2.between_time('4:01', '5:00:59')))
        print(len(df_mask2.between_time('5:01', '6:00:59')))
        print(len(df_mask2.between_time('6:01', '7:00:59')))
        print(len(df_mask2.between_time('7:01', '8:00:59')))
        print(len(df_mask2.between_time('8:01', '9:00:59')))
        print(len(df_mask2.between_time('9:01', '10:00:59')))
        print(len(df_mask2.between_time('10:01', '11:00:59')))
        print(len(df_mask2.between_time('11:01', '12:00:59')))
        print(len(df_mask2.between_time('12:01', '13:00:59')))
        print(len(df_mask2.between_time('13:01', '14:00:59')))
        print(len(df_mask2.between_time('14:01', '15:00:59')))
        print(len(df_mask2.between_time('15:01', '16:00:59')))
        print(len(df_mask2.between_time('16:01', '17:00:59')))
        print(len(df_mask2.between_time('17:01', '18:00:59')))
        print(len(df_mask2.between_time('18:01', '19:00:59')))
        print(len(df_mask2.between_time('19:01', '20:00:59'))) # peak
        print(len(df_mask2.between_time('20:01', '21:00:59')))
        print(len(df_mask2.between_time('21:01', '22:00:59')))
        print(len(df_mask2.between_time('22:01', '23:00:59')))
        print(len(df_mask2.between_time('23:01', '23:59:59')))
        
        A24 = len(data_list[df].between_time('0:00', '1:00:59'))
        # A01 = len(data_list[df].between_time('1:01', '2:00:59'))
        # A02 = len(data_list[df].between_time('2:01', '3:00:59'))
        # A03 = len(data_list[df].between_time('3:01', '4:00:59'))
        # A04 = len(data_list[df].between_time('4:01', '5:00:59'))
        # A05 = len(data_list[df].between_time('5:01', '6:00:59'))
        # A06 = len(data_list[df].between_time('6:01', '7:00:59'))
        # A07 = len(data_list[df].between_time('7:01', '8:00:59'))
        # A08 = len(data_list[df].between_time('8:01', '9:00:59'))
        # A09 = len(data_list[df].between_time('9:01', '10:00:59'))
        # A10 = len(data_list[df].between_time('10:01', '11:00:59'))
        # A11 = len(data_list[df].between_time('11:01', '12:00:59'))
        # A12 = len(data_list[df].between_time('12:01', '13:00:59'))
        # A13 = len(data_list[df].between_time('13:01', '14:00:59'))
        # A14 = len(data_list[df].between_time('14:01', '15:00:59'))
        # A15 = len(data_list[df].between_time('15:01', '16:00:59'))
        # A16 = len(data_list[df].between_time('16:01', '17:00:59'))
        # A17 = len(data_list[df].between_time('17:01', '18:00:59'))
        # A18 = len(data_list[df].between_time('18:01', '19:00:59'))
        # A19 = len(data_list[df].between_time('19:01', '20:00:59')) # peak
        # A20 = len(data_list[df].between_time('20:01', '21:00:59'))
        # A21 = len(data_list[df].between_time('21:01', '22:00:59'))
        # A22 = len(data_list[df].between_time('22:01', '23:00:59'))
        # A23 = len(data_list[df].between_time('23:01', '23:59:59'))
        A24L.append(A24)
        # print("分隔線--------")
        # V24 = len(df_mask2.between_time('0:00', '1:00:59'))
        # V01 = len(df_mask2.between_time('1:01', '2:00:59'))
        # V02 = len(df_mask2.between_time('2:01', '3:00:59'))
        # V03 = len(df_mask2.between_time('3:01', '4:00:59'))
        # V04 = len(df_mask2.between_time('4:01', '5:00:59'))
        # V05 = len(df_mask2.between_time('5:01', '6:00:59'))
        # V06 = len(df_mask2.between_time('6:01', '7:00:59'))
        # V07 = len(df_mask2.between_time('7:01', '8:00:59'))
        # V08 = len(df_mask2.between_time('8:01', '9:00:59'))
        # V09 = len(df_mask2.between_time('9:01', '10:00:59'))
        # V10 = len(df_mask2.between_time('10:01', '11:00:59'))
        # V11 = len(df_mask2.between_time('11:01', '12:00:59'))
        # V12 = len(df_mask2.between_time('12:01', '13:00:59'))
        # V13 = len(df_mask2.between_time('13:01', '14:00:59'))
        # V14 = len(df_mask2.between_time('14:01', '15:00:59'))
        # V15 = len(df_mask2.between_time('15:01', '16:00:59'))
        # V16 = len(df_mask2.between_time('16:01', '17:00:59'))
        # V17 = len(df_mask2.between_time('17:01', '18:00:59'))
        # V18 = len(df_mask2.between_time('18:01', '19:00:59'))
        # V19 = len(df_mask2.between_time('19:01', '20:00:59')) # peak
        # V20 = len(df_mask2.between_time('20:01', '21:00:59'))
        # V21 = len(df_mask2.between_time('21:01', '22:00:59'))
        # V22 = len(df_mask2.between_time('22:01', '23:00:59'))
        # V23 = len(df_mask2.between_time('23:01', '23:59:59'))

    return cc, dd, dic

print(timetree(data_list))

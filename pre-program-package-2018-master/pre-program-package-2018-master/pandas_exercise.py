import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import os

#######################

def HD(HD):
	print('-'*62)
	print('['+ HD +']' )

def CP(CP):
    print('-'*25+"CheckPoint "+CP+'-'*25)

def N(N):
    print("\n")
    print('['+N+']')
########################



def CheckPoint_1_series():
    CP("1")

    HD("1.Tạo series, khai báo index, type")

    S = pd.Series(data=[50191*1000000,46305*1000000,14371*1000000], index=[" The forest"," Cs:go"," Paladins"])
    
    print("Lượng người chơi trong 15 năm của Game:")
    print(S)

    N("khai báo index")
    print(S.index)

    N("lấy phần tử trong series 1")
    print(S[1])

    N("làm phép tính * với phần tử trong series")
    print(S*2)

def CheckPoint_1_DataFrame():

    S = pd.Series(data=[50191*1000000,46305*1000000,14371*1000000], index=["Team Fortress 2"," Cs:go"," Paladins"])

    HD("2.DATA FRAME")

    N("tạo 1 data frame")
    df = pd.DataFrame({"3 tựa game hot nhất trên steam":["Team Fortress 2","CS:GO","PUPG"],"3 tựa game được xem nhiều nhất trên twich":["Liên Minh Huyền Thoại","PUPG","Dota2"],"3 tựa game doanh thu cao nhất":["Warframe","DOTA 2","Tom Clancy’s Rainbow Six Siege"]})
    print(df)

    N("tạo data frame với dữ liệu khác")
    data = {"HS Giỏi":["Ngân","Khánh","Hòa"],"Điểm thi toán:":[10,9,8],"Tổng Điểm:":[29, 25, 28]}
    df2 = pd.DataFrame(data, columns=["HS Giỏi","Điểm thi toán:","Tổng Điểm:"])
    print(df2)

    N("từ numpy.ndarry")
    np_df = pd.DataFrame(np.arange(0, 5))
    print(np_df)

    N("từ 1 series")
    S_df = pd.DataFrame(S, columns= ["Số người chơi"])
    print(S_df)

    N("từ 1 data frame khác")
    df_2 = pd.DataFrame(S_df[1:2])
    print(df_2)

def Checkpoint_2():
    CP("2")
    HD("Đọc và lấy dữ liệu từ dataframe")
    df = pd.read_csv("student-mat.csv",sep=';')
    
    df = df[["school","age","G1", "G2", "G3"]]
    N("lấy 10 dòng đầu")
    print(df.head(10))
    N("lấy 10 dòng cuối")
    print(df.tail(10))
    N("trả nhãn của các cột")
    print(df.columns)
    N("mô tả loại dữ liệu và số dữ liệu có trong mỗi cột ")
    print(df.info(10))
    N("lấy từ dòng 2 đến 10")
    print(df[2:10])
    N("Tính số dữ liệu")
    print(df.describe())
    N("Số dữ liệu trong describe: count là tổng số dòng mà ta nhập dữ liệu, Mean là giá trị trung bình của tổng các số trong 1 cột, min là số nhỏ nhất trong cột, 25% là 25% tổng các số trong cột và lần lượt 50%, 75%, Max là số lớn nhất trong cột")

def CheckPonit_3():
    CP("3")
    HD("1.Lấy dữ liệu lượng mưa (rainfall) và nhiệt độ cao nhất (max_temperature (F)) vào tháng 6 và tháng 7 tại Hà Nội - thời điểm diễn ra MaSSP 2018!")
    df_main = pd.read_csv("weather_in_Hanoi.csv")
    df = df_main[["month","rainfall (mm)","max_temperature (F)"]]
    print(df[5:7])
    N("tháng có (min_temperature (F) bằng 77")
    df = df_main[["month","min_temperature (F)"]]
    print(df[df_main["min_temperature (F)"]==77])
    N("tháng có số ngày mưa cao nhất")
    df = df_main[["month","rainy_days"]]
    print(df.iloc[df_main["rainy_days"].argsort()[-3:]]) 
def checkpoint_4():
    CP("4")
    HD("chèn thêm dữ liệu vào những dữ liêu chưa có")
    df = pd.read_csv("cs_applications.csv")
    print(df)
    N("chèn thêm số vào dữ liệu chưa có trong cột điểm ")
    df_fill = df.fillna({"Điểm phẩy môn Toán":0.0,"Điểm phẩy môn Tin":0.0}, inplace = True )
    print (df)
    N("chèn chứ không dữ liệu chưa có trong cột kí túc xá")
    df_fill = df.fillna({"Cần hỗ trợ kí túc xá":("Không")}, inplace = True )
    print (df)
def CheckPoint_5():
    CP("5")
    HD("Chuyển đổi dữ liệu")
    df_main = pd.read_csv("weather_in_Hanoi.csv")
    N("thêm cột dữ liệu vào df")
    #df_them = pd.DataFrame(df_main["min_temperature (C)","max_temperature (C)","rainfall (cm)"])
    print(df_main)
    N("chuyển đổi độ F sang C và mm sang cm ")
    #df_them = pd.DataFrame(df_main, columns =["month","min_temperature (C)","max_temperature (C)","rainfall (cm)","rainy_days"])
    #df = (df["min_temperature (C)"] == (df_main["min_temperature (F)"]-32)/1.80,df["max_temperature (C)"] ==  (df_main["max_temperature (F)"]-32/1.80),df["rainfall (cm)"]==(df_main["rainfall (mm)"]/10))
    df_main['max_temperature (C)'] = (df_main['max_temperature (F)'] - 32 ) / 1.80
    df_main['min_temperature (C)'] = (df_main['min_temperature (F)'] -32 ) /1.80
    df_main['rainfall (cm)'] = (df_main['min_temperature (F)'] -32 )/ 1.80
    print(df_main)
    N("Tạo df mới ")
    df2 = df_main[["month","max_temperature (C)","min_temperature (C)", "rainfall (cm)", "rainy_days"]]
    print (df2)
    df2.plot()
  
    plt.suptitle("TIEU DE CUA BIEU DO")
    plt.show()
    

CheckPoint_1_series()
CheckPoint_1_DataFrame()
Checkpoint_2()
CheckPoint_3()
checkpoint_4() 
CheckPoint_5()
os.system('pause')  
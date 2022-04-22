import pandas as pd
import re
import cn2an


def data_cleaning():

    # 讀取檔案、建立 dataframe 物件

    city_list = ['a', 'b', 'e', 'f', 'h']

    dataframe_list = []

    for i in range(len(city_list)):
        temp_df = pd.read_csv('land_data/' + city_list[i] + '_lvr_land_a.csv')
        dataframe_list.append(temp_df)

    df_a = dataframe_list[0]
    df_b = dataframe_list[1]
    df_e = dataframe_list[2]
    df_f = dataframe_list[3]
    df_h = dataframe_list[4]


    # 合併 dataframe 物件
    df_all = pd.concat([df_a, df_b, df_e, df_f, df_h],
                       axis=0, ignore_index=True)


    # 篩選【 主要用途 】 為 【 住家用 】
    df_housing = df_all.query("主要用途 == '住家用'")

    # 篩選【 建物型態 】 為 【 住宅大樓 】
    df_hous_building = df_housing[df_housing['建物型態'].apply(
        lambda x: True if re.search('^住宅大樓', x) else False)]

    # 抓出剩餘的 index
    index_list = []
    for i in df_hous_building.index:
        index_list.append(i)

    # 將樓層中文轉成數字(int)
    for j in index_list:
        df_hous_building['總樓層數'][j] = cn2an.transform(
            df_hous_building['總樓層數'][j], "cn2an")
        df_hous_building['總樓層數'][j] = int(
            df_hous_building['總樓層數'][j].replace("層", ""))

    # 篩選總樓層數大於等於十三層的資料
    df_layer = df_hous_building.query("總樓層數 >= 13")

    # 抓出剩餘的 index
    index2_list = []
    for i in df_layer.index:
        index2_list.append(i)

    # 將樓層從數字再轉回中文小寫
    for j in index2_list:
        df_layer['總樓層數'][j] = cn2an.an2cn(df_layer['總樓層數'][j], "low")
        df_layer['總樓層數'][j] = str(df_layer['總樓層數'][j]) + "層"


    df_layer.to_csv('filter_a.csv')


if __name__ == "__main__":
    data_cleaning()

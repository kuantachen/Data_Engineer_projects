import pandas as pd
import re
import cn2an


def filter_b():
    # 讀取檔案、建立 dataframe 物件

    city_list = ['a', 'b', 'e', 'f', 'h']

    dataframe_list = []

    for i in range(len(city_list)):
        temp_df = pd.read_csv('land_data/' + city_list[i] + '_lvr_land_a.csv')
        dataframe_list.append(temp_df)

    df_a = dataframe_list[0].iloc[1:, :]
    df_b = dataframe_list[1].iloc[1:, :]
    df_e = dataframe_list[2].iloc[1:, :]
    df_f = dataframe_list[3].iloc[1:, :]
    df_h = dataframe_list[4].iloc[1:, :]

    # 合併 dataframe 物件
    df_all = pd.concat([df_a, df_b, df_e, df_f, df_h],
                       axis=0, ignore_index=True)

    # 計算【總件數】
    total_count = len(df_all.index)

    print('總件數: ' + str(total_count) + '件')

    # 計算【總車位數】
    regex = "[\u4e00-\u9fa5]{2}[0-9]{1,}[\u4e00-\u9fa5]{2}[0-9]{1,}[\u4e00-\u9fa5]{2}"

    for i in range(len(df_all.index)):
        if type(df_all['交易筆棟數'].iloc[i]) != int:
            df_all['交易筆棟數'][i] = int(re.sub(regex, '', df_all['交易筆棟數'].iloc[i]))

    total_park = df_all['交易筆棟數'].sum()
    print('總車位數: ' + str(total_park) + "個車位")

    # 計算【平均總價元】
    for i in range(len(df_all.index)):
        df_all['總價元'][i] = int(df_all['總價元'][i])

    total_amount = df_all['總價元'].sum()
    average_amount = round(total_amount / total_count, 2)

    print('平均總價元: ' + str(average_amount) + '元')

    # 計算【平均車位總價元】
    for i in range(len(df_all.index)):
        if type(df_all['車位總價元'].iloc[i]) != int:
            df_all['車位總價元'][i] = int(df_all['車位總價元'][i])

    total_park_dollar = df_all['車位總價元'].sum()
    avg_park_dollar = round(total_park_dollar / total_park, 2)

    print('平均車位總價元: ' + str(avg_park_dollar) + "元")

    # 整理成 filter_b dataframe
    filter_dict = {'總件數': [total_count],
                   '總車位數': [total_park],
                   '平均總價元': [average_amount],
                   '平均車位總價元': [avg_park_dollar]}

    df_filter = pd.DataFrame.from_dict(filter_dict)

    # 匯出 filter_b.csv
    df_filter.to_csv('filter_b.csv')


if __name__ == "__main__":
    filter_b()

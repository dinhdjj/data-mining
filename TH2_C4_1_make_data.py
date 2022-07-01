from math import isnan, nan
import pandas as pd


df = pd.read_csv('datasets/Full_Mark_2020.csv')

df['Vatli'] = pd.to_numeric(df['Vatli'], errors='coerce')
df['DiemTrungBinh'] = df.iloc[:, 2:13].mean(axis=1)


def all_greater_than_or_equal(obj, diem):
    if(not isnan(obj['Diali']) and obj['Diali'] < diem):
        return False

    if(not isnan(obj['GDCD']) and obj['GDCD'] < diem):
        return False

    if(not isnan(obj['Hoahoc']) and obj['Hoahoc'] < diem):
        return False

    if(not isnan(obj['LichSu']) and obj['LichSu'] < diem):
        return False

    if(not isnan(obj['Ngoaingu']) and obj['Ngoaingu'] < diem):
        return False

    if(not isnan(obj['Nguvan']) and obj['Nguvan'] < diem):
        return False

    if(not isnan(obj['Sinhhoc']) and obj['Sinhhoc'] < diem):
        return False

    if(not isnan(obj['Toan']) and obj['Toan'] < diem):
        return False

    if(not isnan(obj['Vatli']) and obj['Vatli'] < diem):
        return False

    return True


def xep_loai(row):
    if not all_greater_than_or_equal(row, 1):
        return 'rot'

    if (row['DiemTrungBinh'] < 5):
        return 'rot'

    if row['DiemTrungBinh'] >= 8 and all_greater_than_or_equal(row, 7):
        return 'gioi'

    if row['DiemTrungBinh'] >= 6.5 and all_greater_than_or_equal(row, 6):
        return 'kha'

    return 'trungbinh'


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html
df['XepLoai'] = df.apply(xep_loai, axis=1)

df.to_csv('datasets/Extended_Full_Mark_2020.csv', index=False)

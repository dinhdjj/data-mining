from math import isnan
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/Extended_Full_Mark_2020.csv')

print(f"số học sinh rớt: {df.groupby('XepLoai')['Code'].count()['rot']}")
print(
    f"số học sinh trung bình: {df.groupby('XepLoai')['Code'].count()['trungbinh']}")
print(f"số học sinh khá: {df.groupby('XepLoai')['Code'].count()['kha']}")
print(f"số học sinh giỏi: {df.groupby('XepLoai')['Code'].count()['gioi']}")

"""
số học sinh rớt: 132920
số học sinh trung bình: 812208
số học sinh khá: 82298
số học sinh giỏi: 24434
"""

# Vẽ biểu đồ xếp loại học sinh (pie)
plt.close()
plt.figure(figsize=(12, 6))
plt.tight_layout()

rot = df[df['XepLoai'] == 'rot']['Code'].count()
trungbinh = df[df['XepLoai'] == 'trungbinh']['Code'].count()
kha = df[df['XepLoai'] == 'kha']['Code'].count()
gioi = df[df['XepLoai'] == 'gioi']['Code'].count()

plt.title("Biểu đồ xếp loại học sinh (pie)")
plt.pie(
    [rot, trungbinh, kha, gioi],
    labels=['Rớt', 'Trung bình', 'Khá', 'Giỏi'],
    autopct='%1.1f%%'
)

plt.savefig('images/pie_xep_loai_hoc_sinh.png', dpi=300)
# plt.show()

# Vẽ biểu đồ xếp loại học sinh (dist)
plt.close()
plt.figure(figsize=(12, 6))
plt.tight_layout()
plt.title("Biểu đồ xếp loại học sinh (hist)")
plt.xlabel("Xếp loại")
plt.ylabel("Số lượng")
plt.hist(df['XepLoai'])

plt.savefig('images/hist_xep_loai_hoc_sinh.png', dpi=300)
# plt.show()

# Vẽ biểu đồ điểm trung bình (hist)
plt.close()
plt.figure(figsize=(12, 6))
plt.tight_layout()
plt.title("Biểu đồ điểm trung bình (hist)")
plt.xlabel("Điểm")
plt.ylabel("Số lượng")

bins = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4, 4.6, 4.8,
        5, 5.2, 5.4, 5.6, 5.8, 6, 6.2, 6.4, 6.6, 6.8, 7, 7.2, 7.4, 7.6, 7.8, 8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6, 9.8, 10]
ticks = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5,
         5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]

plt.hist(df['DiemTrungBinh'], bins=bins)
plt.xticks(ticks)

plt.savefig('images/hist_diem_trung_binh_hoc_sinh.png', dpi=300)
# plt.show()

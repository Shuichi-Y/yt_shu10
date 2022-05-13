'''
Excelで9 × 13マスに漢字1文字を描く
RGBLED点灯用のArduinoプログラムに変換
漢字は、右 → 左に移動
２文字目は１文字目の１列後にスタート
2022/4/18
'''

import pandas as pd
# Excelファイルのファイル名を変数に格納する
file_name = 'yt_data1.xlsx'
# Excelファイルを読み込む
df = pd.read_excel(file_name, engine='openpyxl')
print(df)
# Excelデータを蓄積するリスト
data_list = []
# 列ループ
for index, col in df.iteritems():
    # 1列分のデータを保存する作業用リスト
    work = []
    # 行ループ
    for rows in col:
        # 行を追加
        work.append(rows)
    # 1行分のデータをリストに追加
    data_list.append(work)
# 最後に読み込んだCSVファイルから列名を取得
#columns = list(df.columns)
print(data_list)

# ダミーデータ作成
dm_data = ['〇', '〇', '〇', '〇', '〇', '〇', '〇', '〇', '〇', '〇', '〇', '〇', '〇']
# RGBLEDの配列リスト作成
a = [0, 17, 18, 35, 36, 53, 54, 71, 72, 89, 90, 107, 108]
b = [1, 16, 19, 34, 37, 52, 55, 70, 73, 88, 91, 106, 109]
c = [2, 15, 20, 33, 38, 51, 56, 69, 74, 87, 92, 105, 110]
d = [3, 14, 21, 32, 39, 50, 57, 68, 75, 86, 93, 104, 111]
e = [4, 13, 22, 31, 40, 49, 58, 67, 76, 85, 94, 103, 112]
f = [5, 12, 23, 30, 41, 48, 59, 66, 77, 84, 95, 102, 113]
g = [6, 11, 24, 29, 42, 47, 60, 65, 78, 83, 96, 101, 114]
h = [7, 10, 25, 28, 43, 46, 61, 64, 79, 82, 97, 100, 115]
i = [8, 9, 26, 27, 44, 45, 62, 63, 80, 81, 98, 99, 116]
# 右側からの表示の為i列から処理
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = dm_data[num]+data_list[0][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({i[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
print('RGBLED1.show() ;')
print('delay(dt_20) ;')
for num in range(13):
    data_list1 = data_list[0][num]+data_list[1][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({h[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({i[num]}, white[0], white[1], white[2]);')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[1][num]+data_list[2][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({g[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({h[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_1')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[2][num]+data_list[3][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({f[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({g[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_2')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[3][num]+data_list[4][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({e[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({f[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_3')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[4][num]+data_list[5][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({d[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({e[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_4')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[5][num]+data_list[6][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({c[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({d[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_5')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[6][num]+data_list[7][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        pass
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({b[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({c[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_6')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, red[0], red[1], red[2]);')
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({b[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_7')
print('RGBLED1.show() ;')
print('delay(sptime) ;')
for num in range(13):
    data_list1 = data_list[7][num]+data_list[8][num]
    if data_list1 == '〇〇':
        pass
    elif data_list1 == '〇●':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
    elif data_list1 == '●〇':
        pass
    elif data_list1 == '●●':
        print(f'RGBLED1.setPixelColor({a[num]}, white[0], white[1], white[2]);')
print('// 次の文字挿入_8')
print('RGBLED1.show() ;')
print('delay(sptime) ;')

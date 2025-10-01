#2025-10-02 
#課題：関数を使って円の面積を計算する

import math

#円の面積を計算。**で二乗を使っている
def area(r):
  return math.pi*r**2

#半径
r=int(input("半径を入力してください："))
area_ans=area(r)


#桁数を指定して表示
print('円の面積は'+'{:.5}'.format(area_ans)+'cm ^2です。')
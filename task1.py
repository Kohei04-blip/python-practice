#1~10までの数字を足して合計を出す

#numberを初期化する
number = 0
# 1から10までの整数を足し合わせる
# range関数を使って繰り返し処理を行う
for n in range(1,11):
    number += n
print(number)
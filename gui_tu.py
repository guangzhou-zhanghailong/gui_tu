import random
import time

"""
乌龟：快走50% 向右3格
      跌倒20% 向左6格
      慢走30% 向右1格

兔子：睡觉20% 不动
      大跳20% 向右9格
      大跌10% 向左12格
      小跳30% 向右1格
      小跌20% 向左2格
"""
print('游戏开始')
paodao = '_' * 70
#乌龟的初始位置
wpos = 0
#兔子的初始位置
tpos = 0
while True:
    n = random.randint(0, 9)
    # 乌龟的移动
    if n <= 4:
        wpos += 3
    elif 5 <= n <= 6:
        wpos -= 6
    else:
        wpos += 1
    # 兔子移动
    if n <= 1:
        tpos += 0
    elif 2 <= n <= 3:
        tpos += 9
    elif n == 4:
        tpos -= 12
    elif 5 <= n <= 7:
        tpos += 1
    else:
        tpos -= 2
    # 判断是否有选手到达终点
    if tpos >= 70 or wpos >= 70:
        break
    # 判断是否有选手位置为负数
    if tpos < 0:
        tpos = 0
    if wpos < 0:
        wpos = 0
    # 绘制跑道
    if tpos == wpos:
        print(paodao[:tpos] + '咬' + paodao[tpos:] + '__')
    else:
        xpaodao = paodao[:tpos] + '兔' + paodao[tpos:]
        xpaodao = xpaodao[:wpos] + '龟' + xpaodao[wpos:]
        print(xpaodao)
    # 每0.5进行一次奔跑
    time.sleep(0.5)
if wpos >= 70:
    print(paodao[:tpos] + '兔' + paodao[tpos:] + '龟')
    print('乌龟获胜')
else:
    print(paodao[:wpos] + '龟' + paodao[wpos:] + '兔')
    print('兔子获胜')

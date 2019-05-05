# encoding=utf-8
import random
from collections import Counter


class Card(object):
    def __init__(self):
        # 初始化,生成花色和数字的列表
        self.hua_se = ['红桃', '黑桃', '方片', '梅花']
        self.shu_zi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        # 创建保存全部牌和手牌的列表
        self.pai = []
        self.shou_pai = []
        # 用来记录第几次发牌
        self.num = 1

    def xin_pai(self):
        # 循环遍历花色和数字列表生成一副新的牌
        for i in self.hua_se:
            for j in self.shu_zi:
                self.pai.append(i + str(j))
        list = self.da_yin(self.pai)
        print('这是新牌:\n%s' % list)

    def xi_pai(self):
        # 运用随机方法打乱新生成的牌
        random.shuffle(self.pai)
        list = self.da_yin(self.pai)
        print('洗牌后:\n%s' % list)

    def fa_pai(self):
        # 根据发牌的次数每次从开始取5张牌
        self.shou_pai = self.pai[(self.num - 1) * 5:self.num * 5]
        list = self.da_yin(self.shou_pai)
        self.num += 1
        print('手牌为:\n%s' % list)

    def fen_xi(self):
        # 将手牌列表的每个元素分解成花色和数字
        color = []
        num = []
        for i in self.shou_pai:
            color.append(i[:2])
            num.append(int(i[2:]))
        # 对手牌的数字进行从小到大的排序方便后面作比较
        num.sort()
        return color, num

    def pai_xing(self):
        # 分析出手牌的类型
        color, num = self.fen_xi()
        if len(set(color)) == 1 and (
                num[0] + 4 == num[1] + 3 == num[2] + 2 == num[3] + 1 == num[4] or num[0] + 12 == num[1] + 3 == num[
            2] + 2 == num[3] + 1 == num[4]):
            print('牌型是:同花顺')
        elif 4 in Counter(num).values():
            print('牌型是:炸弹')
        elif 3 in Counter(num).values() and 2 in Counter(num).values():
            print('牌型是:满堂红')
        elif len(set(color)) == 1:
            print('牌型是:同花')
        elif num[0] + 4 == num[1] + 3 == num[2] + 2 == num[3] + 1 == num[4] or num[0] + 12 == \
                num[2] == num[1] + 3 == num[2] + 2 == num[3] + 1 == num[4]:
            print('牌型是:顺子')
        elif 2 == list(Counter(num).values()).count(2):
            print('牌型是:两对')
        elif 3 in Counter(num).values():
            print('牌型是:三条')
        elif 2 in Counter(num).values():
            print('牌型是:一对')
        else:
            print('牌型是:单牌')

    def da_yin(self, p):
        # 将数字1,11,12,13替换成A,J,Q,K打印出来
        list = []
        for index, i in enumerate(p):
            if i[2:] == '1':
                list.append(i[:2] + 'A')
            elif i[2:] == '11':
                list.append(i[:2] + 'J')
            elif i[2:] == '12':
                list.append(i[:2] + 'Q')
            elif i[2:] == '13':
                list.append(i[:2] + 'K')
            else:
                list.append(p[index])
        return list


if __name__ == '__main__':
    c = Card()
    c.xin_pai()
    c.xi_pai()
    c.fa_pai()
    c.pai_xing()
    c.fa_pai()
    c.pai_xing()
    c.fa_pai()
    c.pai_xing()
    c.fa_pai()
    c.pai_xing()

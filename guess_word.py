import random

# 生成变量num用来记录剩余游戏次数
num = 5
# 生成变量list用来保存存放单词的列表
list = ['apple', 'pear', 'peach', 'grape', 'banana', 'cherry', 'lemon', 'orange', 'fig', 'tomato']
# 随机从列表中选取一个单词
n = random.randint(0, len(list) - 1)
word = list[n]
timu = '_' * len(word)
# print(word)  # 答案
# 随机选取题目单词中的一个字母并出题
n = random.randint(0, len(word) - 1)
timu = timu[:n] + word[n] + timu[n + 1:]
print(timu)
# 进入游戏循环体
while True:
    # 判断剩余游戏次数
    if num <= 0:
        print('游戏挑战失败')
        break
    # 判断是否已经完成作答
    if '_' not in timu:
        print('游戏挑战成功')
        break
    # 获取用户的作答并转换成小写字母
    da = input('请输入您认为单词内存在的字母:').lower()
    # 判断用户输入的字母是否在单词内部
    if da in word:
        # 生成一个变量j用来记录遍历单词的下标
        j = 0
        for i in word:
            if i == da:
                # 将用户作答的字母全部匹配出来
                timu = timu[:j] + i + timu[j + 1:]
            j += 1
        print(timu)
    else:
        # 如果作答错误剩余次数减一并且提示用户
        num -= 1
        print('输入字母错误请重新作答,答题次数还有%s次' % (num))

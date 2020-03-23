# 这个一个简单的文字游戏程序

import time
import random


# 逐行打印间隔封装
def textSleep(string, sleep):
    print(string)
    time.sleep(int(sleep))


# 逐行打印字符串，并设置间隔时间
def textShow():
    textList = [
        ["你有多久没有面对现实了？", 1],
        ["一起来玩真心话大冒险吧！", 2],
        ["准备好你的勇气了嘛？", 1],
        ["让我们一起探索真实的世界吧！", 2],
    ]
    for n in textList:
        textSleep(n[0], n[1])


# 再来一次判断
def agin():
    agin = input('再玩一次？(y/n)\n').lower()
    if agin == 'y' or 'none':
        getSelectNumber()
    else:
        return textSleep("再来玩哦！", 0)


# 获取用户选择的数字
def getSelectNumber():
    selectNumber = input("请输入你要挑战的问题数量\n") or 'none'
    # 如果直接按回车重新开始
    if selectNumber == 'none':
        getSelectNumber()
    else:
        randomQuestion(int(selectNumber))


# 校验答案列表
def answerCheck(answer, number):
    if len(answer) > 0 and len(answer) == number:
        textSleep("成功", 0)
        agin()
    else:
        textSleep("失败", 0)
        agin()


# 随机提问
def randomQuestion(number):
    question = ['你喜欢什么样的女人', '你喜欢什么样的男人', '你能喝多少白酒', '你喜欢什么色号的口红', '你体重多少']
    if number > len(question):
        textSleep(f"讨厌~人家只有{len(question)}条了啦~", 0)
        getSelectNumber()
    # 随机获取问题
    randomQuestionList = random.sample(question, number)
    # 收集用户输入问题列表
    answer = []
    index = 0
    while len(randomQuestionList) > index:
        answerItem = input(randomQuestionList[index]+'?\n')
        index += 1
        # 存储用户输入以供校验
        answer += answerItem
    answerCheck(answer, number)


# 启动入口
def init():
    textShow()
    getSelectNumber()


init()

# 这个一个简单的文字游戏程序
import time, random


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
    aginValue = input('再玩一次？(y/n)\n').lower()
    if aginValue == 'y':
        getSelectNumber()
    elif aginValue == 'n':
        return textSleep("再来玩哦！", 0)
    else:
        isinstance (aginValue, str)
        textSleep("请输入(y or n)", 0)
        agin()


# 获取用户选择的数字
def getSelectNumber():
    selectNumber = input("请输入你要挑战的问题数量\n") or 'none'
    # 如果直接按回车重新开始
    if selectNumber == 'none':
        textSleep("输入的内容不能为空", 0)
        getSelectNumber()
    # 判断输入的是否是数字
    elif selectNumber.isdigit():
        randomQuestion(int(selectNumber))
    else:
        textSleep("请输入数字", 0)
        getSelectNumber()


# 校验答案列表
def answerCheck(answer, number):
    # 检查是否存在空答案
    flag = True
    for item in answer:
        if item == '':
            flag = False
    # 如果不存在空答案 and 答案数 == 问题数：通关 否则 失败
    if flag and len(answer) == number:
        textSleep("恭喜通关！:)", 0)
        agin()
    else:
        textSleep("挑战失败！-.-", 0)
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
        answer.extend([answerItem])
    print('你输入的所有答案：', answer)
    answerCheck(answer, number)


# 启动入口
def init():
    textShow()
    getSelectNumber()


init()

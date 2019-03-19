# 请你写出一段代码，判断美国队长的工资水平，代码需要满足如下条件：
# 1.如果月工资小于等于500美元，显示“欢迎进入史塔克穷人帮前三名”
# 1.1如果月工资在100-500美元之间，显示“请找弗瑞队长加薪”
# 1.2如果月工资小于等于100美元，显示“恭喜您荣获“美元队长”称号！”
#
# 2.如果月工资在500-1000美元之间（含1000美元），打印“祝贺您至少可以温饱了。”
#
# 3.其他情况下，如果工资大于1000美元，打印“经济危机都难不倒您！”
# 3.1如果工资在1000-20000美元（含20000美元）之间，打印“您快比钢铁侠有钱了！”
# 3.2如果月工资大于20000美元，打印“您是不是来自于瓦坎达国？”
#
# 4.不管赋值改变后输出结果如何，都需固定打印“程序结束”

wage = 1800

if wage <= 500:
    print("欢迎进入史塔克穷人帮前三名")
    if 500 < wage > 100:
        print("请找弗瑞队长加薪")
    elif wage <= 100:
        print("""恭喜您荣获“美元队长”称号！""")
elif 500 < wage <= 1000:
    print("祝贺您至少可以温饱了.")

elif wage > 1000:
    print("经济危机都难不倒您！")
elif 1000 < wage > 20000:
    print("您快比钢铁侠有钱了！")

elif wage > 200000:
    print("您是不是来自于瓦坎达国？")
else:
    print("程序结束")

    # 如果罗恩一天吃超过10个巧克力蛙，罗恩要给哈利100块；
    # 如果罗恩一天吃小于等于10个的巧克力蛙，哈利就给罗恩100块。
    # 输入罗恩吃的巧克力数量，并判断是哈利给罗恩钱，还是罗恩给哈利钱。

number = int(input("罗恩，请输入你要吃的巧克力蛙的数量: "))
if number > 10:
    print("罗恩要给哈利100块")
elif number <= 10:
    print("哈利就给罗恩100块")
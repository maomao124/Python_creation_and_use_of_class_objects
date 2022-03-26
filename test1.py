"""
 * Project name(项目名称)：Python类对象的创建和使用
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 20:17
 * Version(版本): 1.0
 * Description(描述)：
对已定义好的类进行实例化
类名(参数)
定义类时，如果没有手动添加 __init__() 构造方法，又或者添加的 __init__() 中仅有一个 self 参数，则创建类对象时的参数可以省略不写。
 """


class C1:
    a = 2
    b = 3

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print(self.a, "--", self.b)


if __name__ == '__main__':
    c1 = C1(3, 9)
    c1.display()
    print(c1.a)
    print(c1.b)
    c1.a = 22
    c1.display()
    c1.c = 123
    # 增加一个实例变量
    print(c1.c)
    # 删除一个实例变量
    del c1.c
    # print(c1.c)

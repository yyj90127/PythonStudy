# 1、导入wx模块
import wx
import decimal


class cal_GUI():
    # 页面控件初始化：创建所需控件（包括app、window、panel）
    def __init__(self):
        # 2、定义应用程序类的一个对象
        self.app = wx.App()
        # 3、创建一个顶层窗口的wx.Frame类对象，无父窗口时用None
        self.window = wx.Frame(None, title = '简易计算', size = (500,400))
        # 4、定义Panel对象，用于放置容器
        self.panel = wx.Panel(self.window)
        # 5.1、添加第一个数的文本框
        self.num1 = wx.TextCtrl(self.panel)
        # 5.2、添加符号文本框
        self.operator = wx.TextCtrl(self.panel)
        # 5.3、添加第二个数的文本框
        self.num2 = wx.TextCtrl(self.panel)
        # 5.4、添加一个按钮
        self.button = wx.Button(self.panel, label='this is a button，click me！')
        # 5.5、添加结果文本框
        self.res = wx.TextCtrl(self.panel)

    # 控件布局处理：通过BoxSizer设置界面布局
    def layout(self):
        # 定义水平排列容器1
        BoxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        # 依次把相关控件加入容器
        BoxSizer1.Add(self.num1, proportion = 3, border = 6, flag = wx.LEFT|wx.RIGHT)
        BoxSizer1.Add(self.operator, proportion = 1)
        BoxSizer1.Add(self.num2, proportion = 3, border = 6, flag = wx.LEFT|wx.RIGHT)

        # 定义垂直排列容器2
        BoxSizer2 = wx.BoxSizer(wx.VERTICAL)
        # 依次把相关控件加入容器，把BoxSizer1加入BoxSizer2中（嵌套）
        BoxSizer2.Add(BoxSizer1, flag = wx.EXPAND|wx.TOP|wx.BOTTOM, border = 6)
        BoxSizer2.Add(self.button, flag = wx.EXPAND|wx.LEFT|wx.RIGHT, border = 6)
        BoxSizer2.Add(self.res, proportion = 1, flag = wx.EXPAND|wx.ALL, border = 6)

        # 执行布局设置（存在嵌套时，执行最外层的布局）
        self.panel.SetSizer(BoxSizer2)

    # 事件函数定义：各种控件对应的事件函数（1个事件创建1个方法）
    def cal_event(self,event):
        # 获取num1中的输入数据
        number1 = self.num1.GetValue()
        # 获取运行符号
        fun = self.operator.GetValue()
        # 获取num2中的输入数据
        number2 = self.num2.GetValue()
        # 根据运算符进行运算处理
        if fun == "+":
            result = decimal.Decimal(str(number1))+decimal.Decimal(str(number2))
        elif fun == "-":
            result = decimal.Decimal(str(number1))-decimal.Decimal(str(number2))
        elif fun == "*":
            result = decimal.Decimal(str(number1))*decimal.Decimal(str(number2))
        elif fun == "/":
            if number2 != "0":
                result = decimal.Decimal(str(number1))/decimal.Decimal(str(number2))
            else:
                self.res.SetValue("被除数不能为0")
                return
        else:
            self.res.SetValue("请输入正确的符号")
            return
        # 将获取的数据放入结果
        self.res.SetValue(number1+fun+number2+'='+str(result))

    # 控件和事件的绑定：将控件与对应的事件函数进行绑定
    def eventbind(self):
        # 画完界面再进行事件的绑定
        self.button.Bind(wx.EVT_BUTTON,self.cal_event)

    # 执行界面App：显示窗体+运行app
    def run(self):
        # 6、show()方法激活框架窗口
        self.window.Show(True)
        # 7、运行程序
        self.app.MainLoop()

    def main(self):
        self.layout()
        # 事件函数不用直接调用，通过“控件和事件绑定”的函数可以间接调用
        self.eventbind()
        self.run()


if __name__ == '__main__':
    obj = cal_GUI()
    obj.main()
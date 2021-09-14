import os
import wx
from creatTestData import get_random_Email

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PKG_DIR = os.path.abspath(os.path.join(CUR_DIR, os.pardir))


class testTool():
    def __init__(self):
        # 初始化app
        self.app = wx.App()
        # 定义窗体
        self.window = wx.Frame(None, title = '简易测试工具', size = (400,270))
        # 定义panel
        self.panel = wx.Panel(self.window)
        # 定义标签
        self.txt_minlen = wx.StaticText(self.panel, label='最小长度')
        self.lab_minlen = wx.TextCtrl(self.panel)
        self.txt_maxlenText = wx.StaticText(self.panel, label='最大长度')
        self.lab_maxlen = wx.TextCtrl(self.panel)
        self.chkB1 = wx.CheckBox(self.panel, label='包含大写字母')
        self.chkB2 = wx.CheckBox(self.panel, label='包含小写字母')
        self.chkB3 = wx.CheckBox(self.panel, label='包含数字')
        self.chkB4 = wx.CheckBox(self.panel, label='包含符号')
        self.chkB5 = wx.CheckBox(self.panel, label='包含序号')
        self.chkB6 = wx.CheckBox(self.panel, label='包含邮箱后缀')
        self.chkB7 = wx.CheckBox(self.panel, label='保存到文件')
        self.txt_fileAddress = wx.StaticText(self.panel, label='文件名及路径选择')
        self.lab_fileAddress = wx.TextCtrl(self.panel)
        self.txt_numText = wx.StaticText(self.panel, label='数据总数')
        self.lab_num = wx.TextCtrl(self.panel,value = "1")
        self.but_Ok = wx.Button(self.panel, label='确定')
        self.but_Reset = wx.Button(self.panel, label='重置')

    def layout(self):
        BoxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer1.Add(self.txt_minlen, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer1.Add(self.lab_minlen, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer1.Add(self.txt_maxlenText, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer1.Add(self.lab_maxlen, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer2.Add(self.chkB1, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer2.Add(self.chkB2, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer3.Add(self.chkB3, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer3.Add(self.chkB4, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer4.Add(self.chkB5, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer4.Add(self.chkB6, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer5.Add(self.chkB7, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer5.Add(self.txt_fileAddress, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer5.Add(self.lab_fileAddress, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer6.Add(self.txt_numText, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer6.Add(self.lab_num, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer7.Add(self.but_Ok, flag=wx.LEFT | wx.TOP, border=10)
        BoxSizer7.Add(self.but_Reset, flag=wx.LEFT | wx.TOP, border=10)

        BoxSizerFinal = wx.BoxSizer(wx.VERTICAL)
        # 使用for循环来添加上述7个BoxSizer
        for i in range(1,8):
            Box = f'BoxSizer{i}'
            # 使用eval()函数将str转换为对象，这add的是个对象，不是str字符串
            BoxSizerFinal.Add(eval(Box))

        self.panel.SetSizer(BoxSizerFinal)

    def check_ok_input(self):
        # 判断"最大长度"、"最大长度"是否符合规则
        try:
            minlen = int(self.lab_minlen.GetValue())
            maxlen = int(self.lab_maxlen.GetValue())
        except ValueError:
            return('"最大长度"和"最小长度"必须是整数且不能为空')
        else:
            if minlen <= 0 or maxlen <= 0:
                return('"最大长度"和"最小长度"必须大于0')
            elif minlen > maxlen:
                return('"最小长度"必须小于或等于"最大长度"')

        # 判断数据总和是否符合规则
        num = self.lab_num.GetValue()
        if num != "":
            try:
                num = int(self.lab_num.GetValue())
            except ValueError:
                return('"数据总数"必须是整数')
            else:
                if num <= 0:
                    return('"数据总数"必须大于0')
        else:
            num = 1

        # 获取email地址
        fileAddress = self.lab_fileAddress.GetValue()

        # 返回所有参数
        return minlen,maxlen,num,fileAddress

    def event_ok(self,event):
        result = self.check_ok_input()
        if len(result) != 4:
            dlg = wx.MessageDialog(None,result,"错误信息",wx.YES_DEFAULT|wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                dlg.Destroy()
        else:
            # 调用函数，获取email数据列表
            email = get_random_Email(result[0],result[1],result[2])
            # 判断email保存地址
            if self.chkB7.GetValue():
                filename = "result.csv"
                if result[3] == "":
                    filepath = CUR_DIR+"/"+filename
                else:
                    filepath = result[3]+"/"+filename
                # 判断文件路径是否存在
                try:
                    if os.path.exists(filepath):
                        os.remove(filepath)
                    with open(filepath,"w") as f:
                        for i in email:
                            f.write(i+"\n")
                except FileNotFoundError:
                    dlg = wx.MessageDialog(None,"请输入正确的路径","错误信息",wx.YES_DEFAULT|wx.ICON_QUESTION)
                    if dlg.ShowModal() == wx.ID_YES:
                        dlg.Destroy()
            else:
                # 定义一个新窗口并输出
                window = wx.Frame(None, title = '测试数据', size = (400,270))
                panel = wx.Panel(window)
                # 定义多行文本框
                value = ""
                for i in email:
                    value = i+"\n" + value
                result = wx.TextCtrl(panel,value = value, style = wx.TE_MULTILINE)
                BoxSizer = wx.BoxSizer(wx.HORIZONTAL)
                BoxSizer.Add(result, proportion = 1, flag=wx.ALL | wx.EXPAND, border=10)
                panel.SetSizer(BoxSizer)
                window.Show(True)

    def event_reset(self,event):
        dlg = wx.MessageDialog(None,"确认要清空所有内容嘛？","提示",wx.YES_NO|wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            # 将输入框清空
            self.lab_minlen.SetValue("")
            self.lab_maxlen.SetValue("")
            self.lab_fileAddress.SetValue("")
            self.lab_num.SetValue("")
            for i in range(1,8):
                Box = f'self.chkB{i}'
                # 使用eval()函数将str转换为对象
                eval(Box).SetValue(False)
            dlg.Destroy()
        else:
            dlg.Destroy()

    def eventbind(self):
        self.but_Ok.Bind(wx.EVT_BUTTON,self.event_ok)
        self.but_Reset.Bind(wx.EVT_BUTTON,self.event_reset)

    def run(self):
        self.window.Show(True)
        self.app.MainLoop()

    def main(self):
        self.layout()
        self.eventbind()
        self.run()

if __name__ == '__main__':
    obj = testTool()
    obj.main()
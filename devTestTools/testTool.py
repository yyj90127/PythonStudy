import wx

class testTool():
    def __init__(self):
        # 初始化app
        self.app = wx.App()
        # 定义窗体
        self.window = wx.Frame(None, title = '简易测试工具', size = (500,400))
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
        self.lab_num = wx.TextCtrl(self.panel)
        self.but_Ok = wx.Button(self.panel, label='确定')
        self.but_Reset = wx.Button(self.panel, label='重置')

    def layout(self):
        BoxSizer1 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer1.Add(self.txt_minlen, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer1.Add(self.lab_minlen, proportion = 3, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer1.Add(self.txt_maxlenText, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer1.Add(self.lab_maxlen, proportion = 3, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizer2 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer2.Add(self.chkB1, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer2.Add(self.chkB2, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizer3 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer3.Add(self.chkB3, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer3.Add(self.chkB4, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizer4 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer4.Add(self.chkB5, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer4.Add(self.chkB6, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizer5 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer5.Add(self.chkB7, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer5.Add(self.txt_fileAddress, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer5.Add(self.lab_fileAddress, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizer6 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer6.Add(self.txt_numText, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer6.Add(self.lab_num, proportion = 3, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        BoxSizer7.Add(self.but_Ok, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizer7.Add(self.but_Reset, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)

        BoxSizerFinal = wx.BoxSizer(wx.VERTICAL)
        BoxSizerFinal.Add(BoxSizer1, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizerFinal.Add(BoxSizer2, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizerFinal.Add(BoxSizer3, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizerFinal.Add(BoxSizer4, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizerFinal.Add(BoxSizer5, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizerFinal.Add(BoxSizer6, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)
        BoxSizerFinal.Add(BoxSizer7, proportion = 1, border = 0, flag = wx.LEFT|wx.RIGHT)

        self.panel.SetSizer(BoxSizerFinal)

    def event_ok(self,event):
        pass

    def event_reset(self,event):
        pass

    def run(self):
        self.window.Show(True)
        self.app.MainLoop()

    def main(self):
        self.layout()
        self.run()

if __name__ == '__main__':
    obj = testTool()
    obj.main()
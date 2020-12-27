# TODO
class Settings():
    def __init__(self):
        # 自动复制结果到clipboard
        self.autoCopy = False
        # 增量复制模式
        self.increment = False
        # 贴边自动隐藏
        self.autoHide = False
        # 复制自动显示
        self.autoShow = False
        # 自动格式化文本
        self.autoFormat = False
        # 启用系统通知
        self.enableNotification = False
        # 拖拽翻译
        self.dragCopy = False
        # 窗口总是在最前
        self.alwaysTop = False
        # 监视clipboard
        self.monitorClipboard = False

    def setSettings(self,settings):
        if len(settings) != 9:
            return
        else:
            self.autoCopy = settings[0]
            self.increment = settings[1]
            self.autoHide = settings[2]
            self.autoShow = settings[3]
            self.autoFormat = settings[4]
            self.enableNotification = settings[5]
            self.dragCopy = settings[6]
            self.alwaysTop = settings[7]
            self.monitorClipboard = settings[8]

    def showSettings(self):
        print('All settings are shown as fellow:')
        print('autoCpoy:'+str(self.autoCopy))
        print('increment:'+str(self.increment))
        print('autoHide:'+str(self.autoHide))
        print('autoShow:'+str(self.autoShow))
        print('autoFormat:'+str(self.autoFormat))
        print('enableNotification:'+str(self.enableNotification))
        print('dragCopy:'+str(self.dragCopy))
        print('alwaysTop:'+str(self.alwaysTop))
        print('monitorClipboard:'+str(self.monitorClipboard))
        print()




import sys,math,time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from translate import Translate
from settings import Settings
from utils import  Utils

class CopyTranslator(QMainWindow):
    def __init__(self):
        super(CopyTranslator, self).__init__()
        self.settings = Settings()
        self.initUI()
        self.clipboard = QApplication.clipboard()
        self.temp_clipboard = self.clipboard.text()
        self.clipboard_timer = QTimer()
        self.clipboard_timer.timeout.connect(self.monitorClipboard)
        self.clipboard_timer.start(1000)
        self.utils = Utils()


    def initUI(self):
        self.setWindowTitle('CopyTranslator')
        self.outerLayout = QHBoxLayout()
        self.innerLayout1 = QVBoxLayout()
        self.innerLayout2 = QVBoxLayout()

        self.plainEdit = QTextEdit()
        self.translatedEdit = QTextEdit()
        self.innerLayout1.addWidget(self.plainEdit)
        self.innerLayout1.addWidget(self.translatedEdit)

        self.autoCopyCheckBox = QCheckBox('自动复制')
        self.incrementCopyCheckBox = QCheckBox('增量复制')
        self.autoHideCheckBox = QCheckBox('自动隐藏')
        self.autoShowCheckBox = QCheckBox('自动显示')
        self.autoFormatCheckBox = QCheckBox('自动格式化')
        self.enableNotificationCheckBox = QCheckBox('启用通知')
        self.dragCopyCheckBox = QCheckBox('拖拽复制')
        self.alwaysTopCheckBox = QCheckBox('总是置顶')
        self.monitorClipboardCheckBox = QCheckBox('监听剪切板')

        self.label1 = QLabel('源语言')
        self.label2 = QLabel('目标语言')

        self.sourceCombobox = QComboBox()
        self.aimCombobox = QComboBox()

        # self.focusModeButton = QPushButton('专注模式')
        self.translateButton = QPushButton('翻译')
        self.settingButton = QPushButton('设置')

        self.innerLayout2.addWidget(self.autoCopyCheckBox)
        self.innerLayout2.addWidget(self.incrementCopyCheckBox)
        self.innerLayout2.addWidget(self.autoHideCheckBox)
        self.innerLayout2.addWidget(self.autoShowCheckBox)
        self.innerLayout2.addWidget(self.autoFormatCheckBox)
        self.innerLayout2.addWidget(self.enableNotificationCheckBox)
        self.innerLayout2.addWidget(self.dragCopyCheckBox)
        self.innerLayout2.addWidget(self.alwaysTopCheckBox)
        self.innerLayout2.addWidget(self.monitorClipboardCheckBox)
        self.innerLayout2.addWidget(self.label1)
        self.innerLayout2.addWidget(self.sourceCombobox)
        self.innerLayout2.addWidget(self.label2)
        self.innerLayout2.addWidget(self.aimCombobox)
        # self.innerLayout2.addWidget(self.focusModeButton)
        self.innerLayout2.addWidget(self.translateButton)
        self.innerLayout2.addWidget(self.settingButton)
        self.innerLayout2.addStretch(1)

        self.outerLayout.addLayout(self.innerLayout1)
        self.outerLayout.addLayout(self.innerLayout2)

        self.autoCopyCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.autoCopyCheckBox))
        self.incrementCopyCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.incrementCopyCheckBox))
        self.autoHideCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.autoHideCheckBox))
        self.autoShowCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.autoShowCheckBox))
        self.autoFormatCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.autoFormatCheckBox))
        self.enableNotificationCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.enableNotificationCheckBox))
        self.dragCopyCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.dragCopyCheckBox))
        self.alwaysTopCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.alwaysTopCheckBox))
        self.monitorClipboardCheckBox.stateChanged.connect(lambda: self.processCheckBox(self.monitorClipboardCheckBox))

        self.translateButton.clicked.connect(self.translate)

        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        mainWidget.setLayout(self.outerLayout)

    def processCheckBox(self, e):
        checkboxList = [self.autoCopyCheckBox,
                        self.incrementCopyCheckBox,
                        self.autoHideCheckBox,
                        self.autoShowCheckBox,
                        self.autoFormatCheckBox,
                        self.enableNotificationCheckBox,
                        self.dragCopyCheckBox,
                        self.alwaysTopCheckBox,
                        self.monitorClipboardCheckBox]
        settingsList = []
        for i in checkboxList:
            if i.checkState() == 0:
                settingsList.append(False)
            elif i.checkState() ==2:
                settingsList.append(True)
            else:
                pass
        self.settings.setSettings(settingsList)
        # self.settings.showSettings()
        # 检测是否选中了置顶窗口
        if self.settings.alwaysTop:
            self.setWindowFlag(Qt.WindowStaysOnTopHint,True)
            self.show()
        else:
            self.setWindowFlag(Qt.WindowStaysOnTopHint,False)
            self.show()

    def monitorClipboard(self):
        if self.clipboard.text() != self.temp_clipboard and self.settings.monitorClipboard:
            self.temp_clipboard = self.clipboard.text()
            if self.clipboard.text() == self.translatedEdit.toPlainText():
                return
            else:
                if self.settings.increment:
                    if self.plainEdit.toPlainText() != '':
                        temp_string = self.plainEdit.toPlainText() + ' ' + self.clipboard.text()
                    else:
                        temp_string = self.clipboard.text()
                    self.plainEdit.setText(temp_string)
                else:
                    self.plainEdit.setText(self.clipboard.text())
                self.translate()
        else:
            pass

    def translate(self):
        t = Translate()
        target = 'zh'
        plainText = self.plainEdit.toPlainText()
        if len(plainText) == 0:
            return
        else:
            # TODO 处理原始文本
            plainText = self.utils.processPlainText(plainText)
            translatedText = t.translated_content(plainText, target)
            self.translatedEdit.setText(translatedText)
            if self.settings.autoCopy:
                self.clipboard.setText(translatedText)
            else:
                pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CopyTranslator()
    main.show()
    sys.exit(app.exec_())

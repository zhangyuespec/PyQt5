import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import random


# CS=10

class Mywidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.now_money = 100
        self.max_money=0
        self.initUI()
        self.initMenu()
        self.initDice()

    def initDice(self):
        """
        和showDialog一起初始化筛子
        :return:
        """
        self.btn1 = QPushButton('掷色子1', self)
        self.btn1.move(20, 50)
        self.btn1.clicked.connect(self.showDialog)

        self.le1 = QLineEdit(self)
        self.le1.move(20, 22)

        self.btn2 = QPushButton('掷色子2', self)
        self.btn2.move(150, 50)
        self.btn2.clicked.connect(self.showDialog)

        self.le2 = QLineEdit(self)
        self.le2.move(150, 22)

        self.btn3 = QPushButton('掷色子3', self)
        self.btn3.move(280, 50)
        self.btn3.clicked.connect(self.showDialog)

        self.le3 = QLineEdit(self)
        self.le3.move(280, 22)

        self.btn4 = QPushButton('掷色子4', self)
        self.btn4.move(410, 50)
        self.btn4.clicked.connect(self.showDialog)

        self.le4 = QLineEdit(self)
        self.le4.move(410, 22)

        self.btn5 = QPushButton('掷色子5', self)
        self.btn5.move(540, 50)
        self.btn5.clicked.connect(self.showDialog)

        self.le5 = QLineEdit(self)
        self.le5.move(540, 22)

        # 掷所有色子按钮
        self.btn6 = QPushButton('roll all', self)
        self.btn6.move(540, 450)
        self.btn6.clicked.connect(self.showDialog)

        # 确认按钮
        self.btn7 = QPushButton('确认', self)
        self.btn7.move(340, 450)
        self.btn7.clicked.connect(self.showDialog)

        # 当前分数
        self.le7 = QLineEdit(self)
        self.le7.move(740, 22)

    def showDialog(self):
        """
        显示的同时调用game函数去判断游戏分数
        :return:
        """
        sender = self.sender()  # 解决是哪一个筛子掷的问题，get到信号
        if sender.text() == "掷色子1":
            self.text1 = random.randint(1, 6)
            self.le1.setText(str(self.text1))
        elif sender.text() == "掷色子2":
            self.text2 = random.randint(1, 6)
            self.le2.setText(str(self.text2))
        elif sender.text() == "掷色子3":
            self.text3 = random.randint(1, 6)
            self.le3.setText(str(self.text3))

        elif sender.text() == "掷色子4":
            self.text4 = random.randint(1, 6)
            self.le4.setText(str(self.text4))

        elif sender.text() == "掷色子5":
            self.text5 = random.randint(1, 6)
            self.le5.setText(str(self.text5))

        elif sender.text() == "roll all":
            self.text1 = random.randint(1, 6)
            self.le1.setText(str(self.text1))
            self.text2 = random.randint(1, 6)
            self.le2.setText(str(self.text2))
            self.text3 = random.randint(1, 6)
            self.le3.setText(str(self.text3))
            self.text4 = random.randint(1, 6)
            self.le4.setText(str(self.text4))
            self.text5 = random.randint(1, 6)
            self.le5.setText(str(self.text5))
        elif sender.text() == "确认":
            self.score = self.game([self.text1, self.text2, self.text3, self.text4, self.text5])
            self.money()
            self.maxhistory()
            self.le7.setText(str(self.score))

    def game(self, a):
        """
        进行分数计算
        """
        b = np.array(a)
        num1 = np.sum(b == 1)
        num2 = np.sum(b == 2)
        num3 = np.sum(b == 3)
        num4 = np.sum(b == 4)
        num5 = np.sum(b == 4)
        num6 = np.sum(b == 6)
        if num1 == 2 or num2 == 2 or num3 == 2 or num4 == 2 or num5 == 2 or num6 == 2:
            score = 5 - 10
        elif num1 == 3 or num2 == 3 or num3 == 3 or num4 == 3 or num5 == 3 or num6 == 3:
            score = 8 - 10
        elif (num1 == 2 & num2 == 3) or (num1 == 2 & num3 == 3) or (num1 == 2 & num4 == 3) or (
                num1 == 2 & num5 == 3) or (
                num1 == 2 & num6 == 3) or (num2 == 2 & num1 == 3) or \
                (num2 == 2 & num3 == 3) or (num2 == 2 & num4 == 3) or (num2 == 2 & num5 == 3) or (
                num2 == 2 & num6 == 3) or (num3 == 2 & num1 == 3) or \
                (num3 == 2 & num2 == 3) or (num3 == 2 & num4 == 3) or (num3 == 2 & num5 == 3) or (
                num3 == 2 & num6 == 3) or (num4 == 2 & num1 == 3) or (num4 == 2 & num2 == 3) or \
                (num4 == 2 & num3 == 3) or (num4 == 2 & num5 == 3) or (num4 == 2 & num6 == 3) or (
                num5 == 2 & num1 == 3) or \
                (num5 == 2 & num2 == 3) or (num5 == 2 & num3 == 3) or (num5 == 2 & num5 == 3) or (
                num5 == 2 & num6 == 3) or \
                (num6 == 2 & num1 == 3) or (num6 == 2 & num2 == 3) or (num6 == 2 & num3 == 3) or (
                num6 == 2 & num4 == 3) or \
                (num6 == 2 & num5 == 3):
            score = 12 - 10
        elif num1 == 4 or num2 == 4 or num3 == 4 or num4 == 4 or num5 == 4 or num6 == 4:
            score = 15 - 10
        elif (num1 == 1 & num2 == 1 & num3 == 1 & num4 == 1 & num5 == 1 & num6 == 0) or (
                num1 == 0 & num2 == 1 & num3 == 1 & num4 == 1 & num5 == 1 & num6 == 1):
            score = 20 - 10
        elif num1 == 5 or num2 == 5 or num3 == 5 or num4 == 5 or num5 == 5 or num6 == 5:
            score = 30 - 10
        else:
            score = 0 - 10

        return score  # 得到分数

    def money(self):
        """
        计算还有多少钱的函数
        """
        self.now_money += self.score

    def maxhistory(self):
        if self.max_money<self.now_money:
            self.max_money=self.now_money

    def initUI(self):
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle("Dice Poker")
        self.setWindowIcon(QIcon \
                               ("E:\py_code\作业\第三次作业\mm.jpg"))
        self.setToolTip("别发呆")
        QToolTip.setFont(QFont \
                             ("微软雅黑", 12))
        self.statusBar().showMessage("游戏已经就绪")

    def initMenu(self):
        # 菜单栏
        menu_control = self.menuBar().addMenu("Control")
        act_quit = menu_control.addAction("quit")
        act_quit.triggered.connect(self.close)  # 待定

        menu_help = self.menuBar().addMenu("菜单")
        act_about = menu_help.addAction("历史最高分")
        act_about.triggered.connect(self.about)
        act_aboutqt = menu_help.addAction("当前分数")
        act_aboutqt.triggered.connect(self.aboutqt)
        act_rule = menu_help.addAction("规则")
        act_rule.triggered.connect(self.rule)

    def about(self):
        QMessageBox.about(self, "about this software", str(self.max_money))

    def aboutqt(self):
        QMessageBox.about(self, "当前分数", str(self.now_money))

    def rule(self):
        QMessageBox.question(self, "帮助",
                             "Two Paris  5\nThree of a Kind   8\nFull House   12\nFour of a kind  15\nStraight  20\n"
                             "Five of a Kind   30",
                             QMessageBox.Yes)

    def closeEvent(self, event):
        reply = QMessageBox.question \
            (self, "信息",
             "你确定要离开吗",
             QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


myapp = QApplication(sys.argv)
mywidget = Mywidget()
mywidget.show()
sys.exit(myapp.exec_())

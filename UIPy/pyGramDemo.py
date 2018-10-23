#coding:utf-8

import sys, random
from PyQt4 import QtGui, QtCore
import  copy

QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName('utf8'))
class Example(QtGui.QMainWindow):
    def __init__(self,snake,parent=None):
        super(Example, self).__init__(parent)
        self.snake = snake
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(300)
        self.connect(self.timer,QtCore.SIGNAL('timeout()'),self.goOn)
        self.count = 3
        self.step=0
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 350, 280)
        self.setWindowTitle('TCS')
        self.setFixedSize(500,560)
        self.move(300,100)
        self.statusBar().showMessage('ready')
        self.text = 'w a s d '
        self.startbtn = QtGui.QPushButton(self.tr('开始'),self)
        self.startbtn.move(250-self.startbtn.width()/2,150-self.startbtn.height()/2)
        self.startbtn.clicked.connect(self.start)
        self.progressbar = QtGui.QProgressBar(self)
        self.progressbar.setGeometry(0,520,500,20)
        self.progressbar.setMaximum(self.snake.sum)
    def start(self):#开始
        self.count = 1
        self.timer.start()
        self.startbtn.setVisible(False)
    def end(self):#结束
        self.count = 3
        self.timer.stop()
        self.startbtn.setVisible(True)
        self.snake.__init__()
        self.timer.setInterval(300)
    def level_up(self):#显然，level_up
        self.timer.setInterval(self.timer.interval()*0.7)
        pass
    def paintEvent(self, e):#没什么好说的
        if self.count == 1:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.dodrawing(qp)
            qp.end()
            self.count=2
        elif self.count == 2:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.dodrawing_game(qp)
            qp.end()
        elif self.count == 3:
            qp = QtGui.QPainter()
            qp.begin(self)
            self.start_drawing(e,qp)
            qp.end()
            pass
    def start_drawing(self,event,qp):#画开始前的窗口
        self.dodrawing(qp)
        qp.setPen(QtGui.QColor(168,34,3))
        qp.setFont(QtGui.QFont('Decorative',20))
        qp.drawText(event.rect(),QtCore.Qt.AlignCenter,self.text)
        pass
    def dodrawing(self,qp):#画基本的窗口
        qp.setPen(QtCore.Qt.blue)
        size = self.size()
        qp.setBrush(QtCore.Qt.blue)
        qp.drawRect(0,0,size.width(),size.height())
        qp.setBrush(QtCore.Qt.white)
        qp.drawRect(30,30,size.width()-60,size.height()-120)
        if self.count == 1:
            qp.setBrush(QtCore.Qt.green)
            qp.drawRect(30+22*self.snake.head.x(),30+22*self.snake.head.y(),22,22)
            qp.setBrush(QtCore.Qt.yellow)
            for i in self.snake.body:
                qp.drawRect(30+22*i.x(),30+22*i.y(),22,22)

    def dodrawing_game(self,qp):#画在游戏进行时的窗口
        self.dodrawing(qp)
        qp.setBrush(QtCore.Qt.green)
        qp.drawRect(30+22*self.snake.head.x(),30+22*self.snake.head.y(),22,22)
        qp.setBrush(QtCore.Qt.yellow)
        for i in self.snake.body:
            qp.drawRect(30+22*i.x(),30+22*i.y(),22,22)
        qp.setBrush(QtCore.Qt.red)
        qp.drawRect(30+22*self.snake.food.x(),30+22*self.snake.food.y(),22,22)
    def goOn(self):#用来更新画面
        if self.snake.status ==Snake_food.LIVING:
            self.snake.move()
            self.update()
            if self.snake.step == self.snake.sum:
                self.level_up()
                self.snake.step = 0
            self.progressbar.setValue(self.snake.step)
        else:
            self.end()
    def keyPressEvent(self, event):#键盘事件重写
        if event.key() == QtCore.Qt.Key_W and self.snake.direction != Snake_food.DOWN:
            self.snake.change_direction(Snake_food.UP)
        if event.key() == QtCore.Qt.Key_S and self.snake.direction != Snake_food.UP:
            self.snake.change_direction(Snake_food.DOWN)
        if event.key() == QtCore.Qt.Key_A and self.snake.direction != Snake_food.RIGHT:
            self.snake.change_direction(Snake_food.LEFT)
        if event.key() == QtCore.Qt.Key_D and self.snake.direction != Snake_food.LEFT:
            self.snake.change_direction(Snake_food.RIGHT)


class Snake_food(object):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    LIVING = 1
    DEAD = 0
    def __init__(self):
        self.status = self.LIVING
        self.head = QtCore.QPoint(10,10)
        self.length = 4
        self.body = []
        self.direction = self.RIGHT
        self.sum = 10
        self.step = 0
        for i in range(self.length-1):
            self.body.append(QtCore.QPoint(7+i,10))
        #print self.body
        self.food = QtCore.QPoint(self.create_food())
    def change_direction(self,direction):#改变前进方向
        self.direction = direction
    def move(self):#移动，吃到food，增长
        self.body.append(copy.copy(self.head))
        i = self.body.pop(0)
        x = self.head.x()
        y = self.head.y()
        if self.direction == self.UP:
            self.head.setY(y-1)
        if self.direction == self.DOWN:
            self.head.setY(y+1)
        if self.direction == self.LEFT:
            self.head.setX(x-1)
        if self.direction == self.RIGHT:
            self.head.setX(x+1)
        if self.head == self.food:
            self.body.insert(0,i)
            self.step+=1
            self.reset_food()
        if not self.judge():
            self.status = self.DEAD

    def create_food(self):#随机产生food，但不在蛇身上
        while 1:
            x = random.choice(range(20))
            y = random.choice(range(20))
            s = QtCore.QPoint(x,y)
            if (s not in self.body) and s != self.head:
                break
        return s
    def reset_food(self):#重置food，在前一个food被吃掉后使用
        self.food=self.create_food()

    def judge(self):#判断是否碰到四边或自己的身体
        x = self.head.x()
        y = self.head.y()
        return x<20 and x>=0 and y<20 and y>=0 and self.head not in self.body

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example(Snake_food())
    ex.show()
    app.exec_()

if __name__=='__main__':
    main()

#! /usr/bin/env python
# encoding=utf-8
"""
@version:??
@author:都真全
@time:2016/12/16 10:03
"""

import os,sys
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from datetime import datetime
from PyQt5.QtWidgets import (QLabel,QLineEdit,QPushButton,QWidget,
                             QGridLayout,QApplication,QMessageBox,QMainWindow)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
import re


# hosts默认目录
defaultdirpath="C://WINDOWS//System32//drivers//etc"
# HTML解析类
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
        self.con = 1
        self.item = []
    def handle_starttag(self, tag, attrs):
        # print("Encounted a start tag:",tag)
        if tag== "td":
            if "LC" in attrs[0][1]:
                self.flag = True
    def handle_endtag(self, tag):
        # print("Encounted a end tag:",tag)
        if tag == 'td' and self.flag == True:
            flag  = False
    def handle_data(self, data):
        item = str(data)
        if(self.flag == True):
            if str(data) =="Jump to Line":
                self.con = 0
            if (self.con and not item.startswith("\\n")):
                self.item.append(item)
# 保存解析的hosts文件
def saveData(item,saveFile):
    fw = open(saveFile,"w")
    for it in item:
        if "\\t" in it:
            temp = it.split("\\t")
            fw.write(temp[0])
            fw.write("\t")
            fw.write(temp[1])
            fw.write("\n")
        else:
            fw.write(it)
            fw.write("\n")
    fw.close()
    return saveFile

#将系统已经存在的hosts文件重命名保存
def reNameLocalhosts(localhostdirpath):
    # hosts修改时间
    modifyTime = datetime.now().strftime("%Y%m%d%H%M%S")
    hostpath = localhostdirpath+"//hosts"
    try:
        os.rename(hostpath,localhostdirpath+"//hosts."+modifyTime)
    except IOError:
        print("reNameERROR:没有找到hosts文件或者文件读取错误！")

# 爬取github上面的hosts文件，默认的url是"https://github.com/racaljk/hosts/blob/master/hosts"
def getPage(url="https://github.com/racaljk/hosts/blob/master/hosts"):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    thePage = response.read()
    fw = open("./data/data/page","w")
    fw.write(str(thePage))
    # return thePage.decode("UTF8")
    # print(thePage.decode("UTF8"))

# 生成新hosts文件
def generateHosts(file1,file2):
    fw = open(file2,"w")
    for l in open(file1):
        fw.write(l.strip(" "))
    fw.close()
class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget = QWidget(self)
        grid  =QGridLayout(widget)

        self.setCentralWidget(widget)
        positions= [(0,1),(0,2),(1,1),(1,2),(1,3)]

        pathLabel = QLabel("本地hosts路径")
        grid.addWidget(pathLabel,*positions[0])

        self.pathEdit = QLineEdit("默认hosts路径")
        grid.addWidget(self.pathEdit,*positions[1],1,2)

        spiderButton = QPushButton("爬取")
        # spiderButton.setCheckable(True)
        spiderButton.clicked[bool].connect(self.startCrawling)
        grid.addWidget(spiderButton,*positions[2])

        updateButton = QPushButton("更新")
        updateButton.clicked[bool].connect(self.updateLocalhosts)
        grid.addWidget(updateButton, *positions[3])

        exitButton = QPushButton("退出")
        exitButton.clicked[bool].connect(QCoreApplication.instance().quit)
        grid.addWidget(exitButton,*positions[4])


        self.statusBar().showMessage("Ready")
        self.setGeometry(500,500,320,190)
        self.setWindowTitle("HostSwitch")
        self.setWindowIcon(QIcon('./data/icon/switch.png'))
        self.show()

    def closeEvent(self,event):
        reply = QMessageBox.question(self,"Message",
        "确认退出吗？",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    def startCrawling(self):
        self.statusBar().showMessage("开始爬取....")
        getPage()
        self.statusBar().showMessage("爬取完成")
    def updateLocalhosts(self):
        self.statusBar().showMessage("更新本地hosts文件")

        local = defaultdirpath
        newHostsPath = str(self.pathEdit.text())
        print(newHostsPath)
        pattern = re.compile(r'^([a-zA-Z]:|\\\\[a-zA-Z0-9_.$ -]+\\[a-z0-9_.$ -]+)?((?:\\|^)(?:[^\\/:*?"<>|\r\n]+\\)+)')
        match = pattern.match(newHostsPath)
        if match:
            localhostdirpath = newHostsPath
            self.statusBar().showMessage(newHostsPath)
        else:
            localhostdirpath = local
        page = ''
        try:
            for l in open("./data/data/page"):
                page = l.strip()

            reNameLocalhosts(localhostdirpath)

            hostsPath = localhostdirpath + "/hosts"
            parser = MyHTMLParser()
            parser.feed(page)

            saveFile = "./data/data/hosts"
            # print(saveData(parser.item, saveFile))
            generateHosts(saveData(parser.item, saveFile), hostsPath)
            self.statusBar().showMessage("更新完成！")
        except IOError:
            self.statusBar().showMessage("爬取文件不存在，请重新爬取！")
            print("UpdateERROR:没有找到爬取文件或者文件读取错误！")


if __name__ == "__main__":
    app =  QApplication(sys.argv)
    ui =Ui()
    sys.exit(app.exec_())
# if __name__ == '__main__':
#     hostsPath = dirpath + "/hosts"
#     reName()
#     page = getPage()
#     parser = MyHTMLParser()
#     parser.feed(page)
#     saveFile = "./data/data"
#     generateHosts(saveData(parser.item,saveFile),hostsPath)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionData_Admin = QAction(MainWindow)
        self.actionData_Admin.setObjectName(u"actionData_Admin")
        self.actionData_Surat_Masuk = QAction(MainWindow)
        self.actionData_Surat_Masuk.setObjectName(u"actionData_Surat_Masuk")
        self.actionData_Surat_Keluar = QAction(MainWindow)
        self.actionData_Surat_Keluar.setObjectName(u"actionData_Surat_Keluar")
        self.actionData_Disposisi = QAction(MainWindow)
        self.actionData_Disposisi.setObjectName(u"actionData_Disposisi")
        self.actionData_Undangan = QAction(MainWindow)
        self.actionData_Undangan.setObjectName(u"actionData_Undangan")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 17))
        self.menuMenu_Utama = QMenu(self.menubar)
        self.menuMenu_Utama.setObjectName(u"menuMenu_Utama")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Utama.menuAction())
        self.menuMenu_Utama.addAction(self.actionData_Admin)
        self.menuMenu_Utama.addAction(self.actionData_Surat_Masuk)
        self.menuMenu_Utama.addAction(self.actionData_Surat_Keluar)
        self.menuMenu_Utama.addAction(self.actionData_Disposisi)
        self.menuMenu_Utama.addAction(self.actionData_Undangan)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionData_Admin.setText(QCoreApplication.translate("MainWindow", u"Data Admin", None))
        self.actionData_Surat_Masuk.setText(QCoreApplication.translate("MainWindow", u"Data Surat Masuk", None))
        self.actionData_Surat_Keluar.setText(QCoreApplication.translate("MainWindow", u"Data Surat Keluar", None))
        self.actionData_Disposisi.setText(QCoreApplication.translate("MainWindow", u"Data Disposisi", None))
        self.actionData_Undangan.setText(QCoreApplication.translate("MainWindow", u"Data Undangan", None))
        self.menuMenu_Utama.setTitle(QCoreApplication.translate("MainWindow", u"Menu Utama", None))
    # retranslateUi


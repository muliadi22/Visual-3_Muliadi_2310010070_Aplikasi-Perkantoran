# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suratMasuk.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1322, 707)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(60, 30, 251, 384))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.idSuratMasukLabel = QLabel(self.formLayoutWidget)
        self.idSuratMasukLabel.setObjectName(u"idSuratMasukLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idSuratMasukLabel)

        self.idSuratMasukLineEdit = QLineEdit(self.formLayoutWidget)
        self.idSuratMasukLineEdit.setObjectName(u"idSuratMasukLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idSuratMasukLineEdit)

        self.idAdminLabel = QLabel(self.formLayoutWidget)
        self.idAdminLabel.setObjectName(u"idAdminLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.idAdminLabel)

        self.idAdminLineEdit = QLineEdit(self.formLayoutWidget)
        self.idAdminLineEdit.setObjectName(u"idAdminLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.idAdminLineEdit)

        self.tanggalMasukLabel = QLabel(self.formLayoutWidget)
        self.tanggalMasukLabel.setObjectName(u"tanggalMasukLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tanggalMasukLabel)

        self.tanggalMasukDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalMasukDateEdit.setObjectName(u"tanggalMasukDateEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tanggalMasukDateEdit)

        self.noSuratLabel = QLabel(self.formLayoutWidget)
        self.noSuratLabel.setObjectName(u"noSuratLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.noSuratLabel)

        self.noSuratLineEdit = QLineEdit(self.formLayoutWidget)
        self.noSuratLineEdit.setObjectName(u"noSuratLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.noSuratLineEdit)

        self.uraianLabel = QLabel(self.formLayoutWidget)
        self.uraianLabel.setObjectName(u"uraianLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.uraianLabel)

        self.uraianLineEdit = QLineEdit(self.formLayoutWidget)
        self.uraianLineEdit.setObjectName(u"uraianLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.uraianLineEdit)

        self.lanjutKeLabel = QLabel(self.formLayoutWidget)
        self.lanjutKeLabel.setObjectName(u"lanjutKeLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lanjutKeLabel)

        self.lanjutKeLineEdit = QLineEdit(self.formLayoutWidget)
        self.lanjutKeLineEdit.setObjectName(u"lanjutKeLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.lanjutKeLineEdit)

        self.dinasInstansiLabel = QLabel(self.formLayoutWidget)
        self.dinasInstansiLabel.setObjectName(u"dinasInstansiLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.dinasInstansiLabel)

        self.dinasInstansiLineEdit = QLineEdit(self.formLayoutWidget)
        self.dinasInstansiLineEdit.setObjectName(u"dinasInstansiLineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.dinasInstansiLineEdit)

        self.tandaTerimaLabel = QLabel(self.formLayoutWidget)
        self.tandaTerimaLabel.setObjectName(u"tandaTerimaLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.tandaTerimaLabel)

        self.tandaTerimaLineEdit = QLineEdit(self.formLayoutWidget)
        self.tandaTerimaLineEdit.setObjectName(u"tandaTerimaLineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.tandaTerimaLineEdit)

        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.tanggalSuratLabel = QLabel(self.formLayoutWidget)
        self.tanggalSuratLabel.setObjectName(u"tanggalSuratLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.tanggalSuratLabel)

        self.tanggalSuratDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalSuratDateEdit.setObjectName(u"tanggalSuratDateEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tanggalSuratDateEdit)

        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(60, 440, 1181, 115))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.filterDataLabel = QLabel(self.formLayoutWidget_2)
        self.filterDataLabel.setObjectName(u"filterDataLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.filterDataLabel)

        self.comboFilter = QComboBox(self.formLayoutWidget_2)
        self.comboFilter.addItem("")
        self.comboFilter.setObjectName(u"comboFilter")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboFilter)

        self.btnCetak = QPushButton(self.formLayoutWidget_2)
        self.btnCetak.setObjectName(u"btnCetak")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.btnCetak)

        self.tblSuratMasuk = QTableWidget(Form)
        if (self.tblSuratMasuk.columnCount() < 9):
            self.tblSuratMasuk.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblSuratMasuk.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tblSuratMasuk.setObjectName(u"tblSuratMasuk")
        self.tblSuratMasuk.setGeometry(QRect(360, 100, 871, 311))
        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(360, 40, 871, 28))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.idSuratMasukLabel.setText(QCoreApplication.translate("Form", u"Id Surat Masuk", None))
        self.idAdminLabel.setText(QCoreApplication.translate("Form", u"Id Admin", None))
        self.tanggalMasukLabel.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
        self.noSuratLabel.setText(QCoreApplication.translate("Form", u"No Surat", None))
        self.uraianLabel.setText(QCoreApplication.translate("Form", u"Uraian", None))
        self.lanjutKeLabel.setText(QCoreApplication.translate("Form", u"Lanjut Ke", None))
        self.dinasInstansiLabel.setText(QCoreApplication.translate("Form", u"Dinas Instansi", None))
        self.tandaTerimaLabel.setText(QCoreApplication.translate("Form", u"Tanda Terima", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.tanggalSuratLabel.setText(QCoreApplication.translate("Form", u"Tanggal Surat", None))
        self.filterDataLabel.setText(QCoreApplication.translate("Form", u"Filter Data", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
        ___qtablewidgetitem = self.tblSuratMasuk.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Surat Masuk", None));
        ___qtablewidgetitem1 = self.tblSuratMasuk.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Id Admin", None));
        ___qtablewidgetitem2 = self.tblSuratMasuk.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None));
        ___qtablewidgetitem3 = self.tblSuratMasuk.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"No Surat", None));
        ___qtablewidgetitem4 = self.tblSuratMasuk.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tanggal Surat", None));
        ___qtablewidgetitem5 = self.tblSuratMasuk.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Uraian", None));
        ___qtablewidgetitem6 = self.tblSuratMasuk.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Lanjut Ke", None));
        ___qtablewidgetitem7 = self.tblSuratMasuk.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Dinas Instansi", None));
        ___qtablewidgetitem8 = self.tblSuratMasuk.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Tanda Terima", None));
    # retranslateUi


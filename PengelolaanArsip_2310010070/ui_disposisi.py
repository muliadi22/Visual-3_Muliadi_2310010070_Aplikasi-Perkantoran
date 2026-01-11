# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'disposisi.ui'
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
        Form.resize(1219, 633)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(50, 30, 251, 383))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.BtnSimpan = QPushButton(self.formLayoutWidget)
        self.BtnSimpan.setObjectName(u"BtnSimpan")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.BtnSimpan)

        self.BtnUbah = QPushButton(self.formLayoutWidget)
        self.BtnUbah.setObjectName(u"BtnUbah")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.BtnUbah)

        self.BtnHapus = QPushButton(self.formLayoutWidget)
        self.BtnHapus.setObjectName(u"BtnHapus")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.BtnHapus)

        self.idDisposisiLabel = QLabel(self.formLayoutWidget)
        self.idDisposisiLabel.setObjectName(u"idDisposisiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.idDisposisiLabel)

        self.idDisposisiLineEdit = QLineEdit(self.formLayoutWidget)
        self.idDisposisiLineEdit.setObjectName(u"idDisposisiLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.idDisposisiLineEdit)

        self.idAdminLabel = QLabel(self.formLayoutWidget)
        self.idAdminLabel.setObjectName(u"idAdminLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.idAdminLabel)

        self.idAdminLineEdit = QLineEdit(self.formLayoutWidget)
        self.idAdminLineEdit.setObjectName(u"idAdminLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.idAdminLineEdit)

        self.dinasInstansiLabel = QLabel(self.formLayoutWidget)
        self.dinasInstansiLabel.setObjectName(u"dinasInstansiLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.dinasInstansiLabel)

        self.dinasInstansiLineEdit = QLineEdit(self.formLayoutWidget)
        self.dinasInstansiLineEdit.setObjectName(u"dinasInstansiLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.dinasInstansiLineEdit)

        self.tanggalMasukLabel = QLabel(self.formLayoutWidget)
        self.tanggalMasukLabel.setObjectName(u"tanggalMasukLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.tanggalMasukLabel)

        self.tanggalMasukDateEdit = QDateEdit(self.formLayoutWidget)
        self.tanggalMasukDateEdit.setObjectName(u"tanggalMasukDateEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tanggalMasukDateEdit)

        self.noTanggalSuratLabel = QLabel(self.formLayoutWidget)
        self.noTanggalSuratLabel.setObjectName(u"noTanggalSuratLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.noTanggalSuratLabel)

        self.noTanggalSuratLineEdit = QLineEdit(self.formLayoutWidget)
        self.noTanggalSuratLineEdit.setObjectName(u"noTanggalSuratLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.noTanggalSuratLineEdit)

        self.isiDisposisiLabel = QLabel(self.formLayoutWidget)
        self.isiDisposisiLabel.setObjectName(u"isiDisposisiLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.isiDisposisiLabel)

        self.isiDisposisiLineEdit = QLineEdit(self.formLayoutWidget)
        self.isiDisposisiLineEdit.setObjectName(u"isiDisposisiLineEdit")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.isiDisposisiLineEdit)

        self.uraianLabel = QLabel(self.formLayoutWidget)
        self.uraianLabel.setObjectName(u"uraianLabel")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.uraianLabel)

        self.uraianLineEdit = QLineEdit(self.formLayoutWidget)
        self.uraianLineEdit.setObjectName(u"uraianLineEdit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.uraianLineEdit)

        self.lanjutKeLabel = QLabel(self.formLayoutWidget)
        self.lanjutKeLabel.setObjectName(u"lanjutKeLabel")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lanjutKeLabel)

        self.lanjutKeLineEdit = QLineEdit(self.formLayoutWidget)
        self.lanjutKeLineEdit.setObjectName(u"lanjutKeLineEdit")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.lanjutKeLineEdit)

        self.tandaTerimaLabel = QLabel(self.formLayoutWidget)
        self.tandaTerimaLabel.setObjectName(u"tandaTerimaLabel")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.tandaTerimaLabel)

        self.tandaTerimaLineEdit = QLineEdit(self.formLayoutWidget)
        self.tandaTerimaLineEdit.setObjectName(u"tandaTerimaLineEdit")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.tandaTerimaLineEdit)

        self.lineCari = QLineEdit(Form)
        self.lineCari.setObjectName(u"lineCari")
        self.lineCari.setGeometry(QRect(330, 30, 831, 28))
        self.tblDisposisi = QTableWidget(Form)
        if (self.tblDisposisi.columnCount() < 9):
            self.tblDisposisi.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tblDisposisi.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tblDisposisi.setObjectName(u"tblDisposisi")
        self.tblDisposisi.setGeometry(QRect(330, 80, 831, 331))
        self.formLayoutWidget_2 = QWidget(Form)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(50, 430, 1111, 115))
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.BtnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.BtnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.BtnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        self.idDisposisiLabel.setText(QCoreApplication.translate("Form", u"Id Disposisi", None))
        self.idAdminLabel.setText(QCoreApplication.translate("Form", u"Id Admin", None))
        self.dinasInstansiLabel.setText(QCoreApplication.translate("Form", u"Dinas Instansi", None))
        self.tanggalMasukLabel.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None))
        self.noTanggalSuratLabel.setText(QCoreApplication.translate("Form", u"No Tanggal Surat", None))
        self.isiDisposisiLabel.setText(QCoreApplication.translate("Form", u"Isi Disposisi", None))
        self.uraianLabel.setText(QCoreApplication.translate("Form", u"Uraian", None))
        self.lanjutKeLabel.setText(QCoreApplication.translate("Form", u"Lanjut Ke", None))
        self.tandaTerimaLabel.setText(QCoreApplication.translate("Form", u"Tanda Terima", None))
        ___qtablewidgetitem = self.tblDisposisi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Id Disposisi", None));
        ___qtablewidgetitem1 = self.tblDisposisi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Id Admin", None));
        ___qtablewidgetitem2 = self.tblDisposisi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Dinas Instansi", None));
        ___qtablewidgetitem3 = self.tblDisposisi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Tanggal Masuk", None));
        ___qtablewidgetitem4 = self.tblDisposisi.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"No Tanggal Surat", None));
        ___qtablewidgetitem5 = self.tblDisposisi.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Isi Disposisi", None));
        ___qtablewidgetitem6 = self.tblDisposisi.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Uraian", None));
        ___qtablewidgetitem7 = self.tblDisposisi.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Lanjut Ke", None));
        ___qtablewidgetitem8 = self.tblDisposisi.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Tanda Terima", None));
        self.filterDataLabel.setText(QCoreApplication.translate("Form", u"Filter Data", None))
        self.comboFilter.setItemText(0, QCoreApplication.translate("Form", u"Semua", None))

        self.btnCetak.setText(QCoreApplication.translate("Form", u"Cetak", None))
    # retranslateUi


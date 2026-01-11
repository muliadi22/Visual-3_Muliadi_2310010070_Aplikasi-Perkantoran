# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_Admin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Admin")
        filenya = QFile('admin.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formAdmin = muatfile.load(filenya, self)
        self.aksi = crud_arsip()
        self.formAdmin.BtnSimpan.clicked.connect(self.simpanAdmin)
        self.formAdmin.BtnUbah.clicked.connect(self.ubahAdmin)
        self.formAdmin.BtnHapus.clicked.connect(self.hapusAdmin)
        self.tampilDataAdmin()
        self.formAdmin.lineCari.textChanged.connect(self.cariDataAdmin)
        self.formAdmin.btnCetak.clicked.connect(self.laporanAdmin)

    def simpanAdmin(self):
        if not self.formAdmin.idAdminLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Admin belum diisi")
            self.formAdmin.idAdminLineEdit.setFocus()
        elif not self.formAdmin.usernameLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Username belum diisi")
            self.formAdmin.usernameLineEdit.setFocus()
        elif not self.formAdmin.passwordLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "Password belum diisi")
            self.formAdmin.passwordLineEdit.setFocus()
        else:
            id_admin = self.formAdmin.idAdminLineEdit.text()
            username = self.formAdmin.usernameLineEdit.text()
            password = self.formAdmin.passwordLineEdit.text()

            self.aksi.tambahAdmin(id_admin, username, password)
            self.tampilDataAdmin()
            QMessageBox.information(None, "Informasi", "Data Admin berhasil disimpan")

    def ubahAdmin(self):
        id_admin = self.formAdmin.idAdminLineEdit.text()
        username = self.formAdmin.usernameLineEdit.text()
        password = self.formAdmin.passwordLineEdit.text()

        self.aksi.gantiAdmin(id_admin, username, password)
        self.tampilDataAdmin()
        QMessageBox.information(None, "Informasi", "Data Admin berhasil diubah")

    def hapusAdmin(self):
        pesan = QMessageBox.question(None, "Konfirmasi Hapus", "Apakah yakin menghapus data Admin ini?",
        QMessageBox.Yes | QMessageBox.No)

        if pesan == QMessageBox.Yes:
            id_admin = self.formAdmin.idAdminLineEdit.text()
            self.aksi.hapusAdmin(id_admin)
            self.tampilDataAdmin()
            QMessageBox.information(None, "Informasi", "Data Admin berhasil dihapus")

    def tampilDataAdmin(self):
        self.formAdmin.tblAdmin.setRowCount(0)
        data = self.aksi.dataAdmin()

        for i, baris in enumerate(data):
            self.formAdmin.tblAdmin.insertRow(i)
            self.formAdmin.tblAdmin.setItem(i, 0, QTableWidgetItem(str(baris["id_admin"])))
            self.formAdmin.tblAdmin.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
            self.formAdmin.tblAdmin.setItem(i, 2, QTableWidgetItem(str(baris["password"])))

    def cariDataAdmin(self):
        varCari = self.formAdmin.lineCari.text()
        self.formAdmin.tblAdmin.setRowCount(0)
        data = self.aksi.filterAdmin(varCari)

        for i, baris in enumerate(data):
            self.formAdmin.tblAdmin.insertRow(i)
            self.formAdmin.tblAdmin.setItem(i, 0, QTableWidgetItem(str(baris["id_admin"])))
            self.formAdmin.tblAdmin.setItem(i, 1, QTableWidgetItem(str(baris["username"])))
            self.formAdmin.tblAdmin.setItem(i, 2, QTableWidgetItem(str(baris["password"])))

    def laporanAdmin(self):
        self.aksi.cetakAdmin()

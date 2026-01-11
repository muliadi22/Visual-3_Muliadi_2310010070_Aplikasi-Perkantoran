# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_SuratKeluar(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Surat Keluar")
        filenya = QFile('suratKeluar.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formSuratKeluar = muatfile.load(filenya,self)
        self.aksi = crud_arsip()
        self.formSuratKeluar.BtnSimpan.clicked.connect(self.simpanSuratKeluar)
        self.formSuratKeluar.BtnUbah.clicked.connect(self.ubahSuratKeluar)
        self.formSuratKeluar.BtnHapus.clicked.connect(self.hapusSuratKeluar)
        self.tampilDataSuratKeluar()
        self.formSuratKeluar.lineCari.textChanged.connect(self.cariDataSuratKeluar)
        self.formSuratKeluar.btnCetak.clicked.connect(self.laporanSuratKeluar)

    def simpanSuratKeluar(self):
        if not self.formSuratKeluar.idSuratKeluarLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Surat Keluar belum diisi")
            self.formSuratKeluar.idSuratKeluarLineEdit.setFocus()
        else:
            id_surat_keluar = self.formSuratKeluar.idSuratKeluarLineEdit.text()
            id_admin = self.formSuratKeluar.idAdminLineEdit.text()
            tgl_keluar = self.formSuratKeluar.tanggalKeluarDateEdit.date().toString("yyyy-MM-dd")
            instansi = self.formSuratKeluar.dinasInstansiLineEdit.text()
            no_surat = self.formSuratKeluar.noSuratLineEdit.text()
            tgl_surat = self.formSuratKeluar.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
            uraian = self.formSuratKeluar.uraianLineEdit.text()

            self.aksi.tambahSuratKeluar(id_surat_keluar, id_admin, tgl_keluar, instansi, no_surat, tgl_surat, uraian)
            self.tampilDataSuratKeluar()
            QMessageBox.information(None, "Informasi", "Data Surat Keluar berhasil disimpan")

    def ubahSuratKeluar(self):
        id_surat_keluar = self.formSuratKeluar.idSuratKeluarLineEdit.text()
        id_admin = self.formSuratKeluar.idAdminLineEdit.text()
        tgl_keluar = self.formSuratKeluar.tanggalKeluarDateEdit.date().toString("yyyy-MM-dd")
        instansi = self.formSuratKeluar.dinasInstansiLineEdit.text()
        no_surat = self.formSuratKeluar.noSuratLineEdit.text()
        tgl_surat = self.formSuratKeluar.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formSuratKeluar.uraianLineEdit.text()

        self.aksi.gantiSuratKeluar(id_surat_keluar, id_admin, tgl_keluar, instansi, no_surat, tgl_surat, uraian)
        self.tampilDataSuratKeluar()
        QMessageBox.information(None, "Informasi", "Data Surat Keluar berhasil diubah")

    def hapusSuratKeluar(self):
        pesan = QMessageBox.question(None, "Konfirmasi Hapus", "Apakah yakin menghapus data surat ini?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            id_surat_keluar = self.formSuratKeluar.idSuratKeluarLineEdit.text()
            self.aksi.hapusSuratKeluar(id_surat_keluar)
            self.tampilDataSuratKeluar()
            QMessageBox.information(None, "Informasi", "Data Surat Keluar berhasil dihapus")

    def tampilDataSuratKeluar(self):
        self.formSuratKeluar.tblSuratKeluar.setRowCount(0)
        data = self.aksi.dataSuratKeluar()

        for i, baris in enumerate(data):
            self.formSuratKeluar.tblSuratKeluar.insertRow(i)
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 0, QTableWidgetItem(str(baris["id_surat_keluar"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_keluar"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 3, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 4, QTableWidgetItem(str(baris["no_surat"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 5, QTableWidgetItem(str(baris["tanggal_surat"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 6, QTableWidgetItem(str(baris["uraian"])))

    def cariDataSuratKeluar(self):
        varCari = self.formSuratKeluar.lineCari.text()
        self.formSuratKeluar.tblSuratKeluar.setRowCount(0)
        data = self.aksi.filterSuratKeluar(varCari)

        for i, baris in enumerate(data):
            self.formSuratKeluar.tblSuratKeluar.insertRow(i)
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 0, QTableWidgetItem(str(baris["id_surat_keluar"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_keluar"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 3, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 4, QTableWidgetItem(str(baris["no_surat"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 5, QTableWidgetItem(str(baris["tanggal_surat"])))
            self.formSuratKeluar.tblSuratKeluar.setItem(i, 6, QTableWidgetItem(str(baris["uraian"])))

    def laporanSuratKeluar(self):
        self.aksi.cetakSuratKeluar()

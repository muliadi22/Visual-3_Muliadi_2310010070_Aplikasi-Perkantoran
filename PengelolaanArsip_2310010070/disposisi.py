# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_Disposisi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Disposisi")
        filenya = QFile('disposisi.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formDisposisi = muatfile.load(filenya, self)
        self.aksi = crud_arsip()
        self.formDisposisi.BtnSimpan.clicked.connect(self.simpanDisposisi)
        self.formDisposisi.BtnUbah.clicked.connect(self.ubahDisposisi)
        self.formDisposisi.BtnHapus.clicked.connect(self.hapusDisposisi)
        self.tampilDataDisposisi()
        self.formDisposisi.lineCari.textChanged.connect(self.cariDataDisposisi)
        self.formDisposisi.btnCetak.clicked.connect(self.laporanDisposisi)

    def simpanDisposisi(self):
        if not self.formDisposisi.idDisposisiLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Disposisi belum diisi")
            self.formDisposisi.idDisposisiLineEdit.setFocus()
        else:
            id_disposisi = self.formDisposisi.idDisposisiLineEdit.text()
            id_admin = self.formDisposisi.idAdminLineEdit.text()
            instansi = self.formDisposisi.dinasInstansiLineEdit.text()
            tgl_masuk = self.formDisposisi.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
            no_tgl_surat = self.formDisposisi.noTanggalSuratLineEdit.text()
            isi_disposisi = self.formDisposisi.isiDisposisiLineEdit.text()
            uraian = self.formDisposisi.uraianLineEdit.text()
            lanjut_ke = self.formDisposisi.lanjutKeLineEdit.text()
            tanda_terima = self.formDisposisi.tandaTerimaLineEdit.text()

            self.aksi.tambahDisposisi(id_disposisi, id_admin, instansi, tgl_masuk, no_tgl_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima)
            self.tampilDataDisposisi()
            QMessageBox.information(None, "Informasi", "Data Disposisi berhasil disimpan")

    def ubahDisposisi(self):
        id_disposisi = self.formDisposisi.idDisposisiLineEdit.text()
        id_admin = self.formDisposisi.idAdminLineEdit.text()
        instansi = self.formDisposisi.dinasInstansiLineEdit.text()
        tgl_masuk = self.formDisposisi.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_tgl_surat = self.formDisposisi.noTanggalSuratLineEdit.text()
        isi_disposisi = self.formDisposisi.isiDisposisiLineEdit.text()
        uraian = self.formDisposisi.uraianLineEdit.text()
        lanjut_ke = self.formDisposisi.lanjutKeLineEdit.text()
        tanda_terima = self.formDisposisi.tandaTerimaLineEdit.text()

        self.aksi.gantiDisposisi(id_disposisi, id_admin, instansi, tgl_masuk, no_tgl_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima)
        self.tampilDataDisposisi()
        QMessageBox.information(None, "Informasi", "Data Disposisi berhasil diubah")

    def hapusDisposisi(self):
        pesan = QMessageBox.question(None, "Konfirmasi Hapus", "Apakah yakin menghapus data disposisi ini?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            id_disposisi = self.formDisposisi.idDisposisiLineEdit.text()
            self.aksi.hapusDisposisi(id_disposisi)
            self.tampilDataDisposisi()
            QMessageBox.information(None, "Informasi", "Data Disposisi berhasil dihapus")

    def tampilDataDisposisi(self):
        self.formDisposisi.tblDisposisi.setRowCount(0)
        data = self.aksi.dataDisposisi()

        for i, baris in enumerate(data):
            self.formDisposisi.tblDisposisi.insertRow(i)
            self.formDisposisi.tblDisposisi.setItem(i, 0, QTableWidgetItem(str(baris["id_disposisi"])))
            self.formDisposisi.tblDisposisi.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formDisposisi.tblDisposisi.setItem(i, 2, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formDisposisi.tblDisposisi.setItem(i, 3, QTableWidgetItem(str(baris["tanggal_masuk"])))
            self.formDisposisi.tblDisposisi.setItem(i, 4, QTableWidgetItem(str(baris["no_tanggal_surat"])))
            self.formDisposisi.tblDisposisi.setItem(i, 5, QTableWidgetItem(str(baris["isi_disposisi"])))
            self.formDisposisi.tblDisposisi.setItem(i, 6, QTableWidgetItem(str(baris["uraian"])))
            self.formDisposisi.tblDisposisi.setItem(i, 7, QTableWidgetItem(str(baris["lanjut_ke"])))
            self.formDisposisi.tblDisposisi.setItem(i, 8, QTableWidgetItem(str(baris["tanda_terima"])))

    def cariDataDisposisi(self):
        varCari = self.formDisposisi.lineCari.text()
        self.formDisposisi.tblDisposisi.setRowCount(0)
        data = self.aksi.filterDisposisi(varCari)

        for i, baris in enumerate(data):
            self.formDisposisi.tblDisposisi.insertRow(i)
            self.formDisposisi.tblDisposisi.setItem(i, 0, QTableWidgetItem(str(baris["id_disposisi"])))
            self.formDisposisi.tblDisposisi.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formDisposisi.tblDisposisi.setItem(i, 2, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formDisposisi.tblDisposisi.setItem(i, 3, QTableWidgetItem(str(baris["tanggal_masuk"])))
            self.formDisposisi.tblDisposisi.setItem(i, 4, QTableWidgetItem(str(baris["no_tanggal_surat"])))
            self.formDisposisi.tblDisposisi.setItem(i, 5, QTableWidgetItem(str(baris["isi_disposisi"])))
            self.formDisposisi.tblDisposisi.setItem(i, 6, QTableWidgetItem(str(baris["uraian"])))
            self.formDisposisi.tblDisposisi.setItem(i, 7, QTableWidgetItem(str(baris["lanjut_ke"])))
            self.formDisposisi.tblDisposisi.setItem(i, 8, QTableWidgetItem(str(baris["tanda_terima"])))

    def laporanDisposisi(self):
        self.aksi.cetakDisposisi()

# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip


class form_SuratMasuk(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Surat Masuk")
        filenya = QFile('suratMasuk.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formSuratMasuk = muatfile.load(filenya,self)
        self.aksi = crud_arsip()
        self.formSuratMasuk.BtnSimpan.clicked.connect(self.simpanSuratMasuk)
        self.formSuratMasuk.BtnUbah.clicked.connect(self.ubahSuratMasuk)
        self.formSuratMasuk.BtnHapus.clicked.connect(self.hapusSuratMasuk)
        self.tampilDataSuratMasuk()
        self.formSuratMasuk.lineCari.textChanged.connect(self.cariDataSuratMasuk)
        self.formSuratMasuk.btnCetak.clicked.connect(self.laporanSuratMasuk)

    def simpanSuratMasuk(self):
        if not self.formSuratMasuk.idSuratMasukLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Surat Masuk belum diisi")
            self.formSuratMasuk.idSuratMasukLineEdit.setFocus()
        else:
            id_surat = self.formSuratMasuk.idSuratMasukLineEdit.text()
            id_admin = self.formSuratMasuk.idAdminLineEdit.text()
            tgl_masuk = self.formSuratMasuk.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
            no_surat = self.formSuratMasuk.noSuratLineEdit.text()
            tgl_surat = self.formSuratMasuk.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
            uraian = self.formSuratMasuk.uraianLineEdit.text()
            lanjut_ke = self.formSuratMasuk.lanjutKeLineEdit.text()
            instansi = self.formSuratMasuk.dinasInstansiLineEdit.text()
            tanda_terima = self.formSuratMasuk.tandaTerimaLineEdit.text()

            self.aksi.tambahSuratMasuk(id_surat, id_admin, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, instansi, tanda_terima)
            self.tampilDataSuratMasuk()
            QMessageBox.information(None, "Informasi", "Data Surat Masuk berhasil disimpan")

    def ubahSuratMasuk(self):
        id_surat = self.formSuratMasuk.idSuratMasukLineEdit.text()
        id_admin = self.formSuratMasuk.idAdminLineEdit.text()
        tgl_masuk = self.formSuratMasuk.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formSuratMasuk.noSuratLineEdit.text()
        tgl_surat = self.formSuratMasuk.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formSuratMasuk.uraianLineEdit.text()
        lanjut_ke = self.formSuratMasuk.lanjutKeLineEdit.text()
        instansi = self.formSuratMasuk.dinasInstansiLineEdit.text()
        tanda_terima = self.formSuratMasuk.tandaTerimaLineEdit.text()

        self.aksi.gantiSuratMasuk(id_surat, id_admin, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, instansi, tanda_terima)
        self.tampilDataSuratMasuk()
        QMessageBox.information(None, "Informasi", "Data Surat Masuk berhasil diubah")

    def hapusSuratMasuk(self):
        pesan = QMessageBox.question(None, "Konfirmasi Hapus", "Apakah yakin menghapus data surat ini?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            id_surat = self.formSuratMasuk.idSuratMasukLineEdit.text()
            self.aksi.hapusSuratMasuk(id_surat)
            self.tampilDataSuratMasuk()
            QMessageBox.information(None, "Informasi", "Data Surat Masuk berhasil dihapus")

    def tampilDataSuratMasuk(self):
        self.formSuratMasuk.tblSuratMasuk.setRowCount(0)
        data = self.aksi.dataSuratMasuk()

        for i, baris in enumerate(data):
            self.formSuratMasuk.tblSuratMasuk.insertRow(i)
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 0, QTableWidgetItem(str(baris["id_surat_masuk"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_masuk"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 3, QTableWidgetItem(str(baris["no_surat"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 4, QTableWidgetItem(str(baris["tanggal_surat"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 5, QTableWidgetItem(str(baris["uraian"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 6, QTableWidgetItem(str(baris["lanjut_ke"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 7, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 8, QTableWidgetItem(str(baris["tanda_terima"])))

    def cariDataSuratMasuk(self):
        varCari = self.formSuratMasuk.lineCari.text()
        self.formSuratMasuk.tblSuratMasuk.setRowCount(0)
        data = self.aksi.filterSuratMasuk(varCari)

        for i, baris in enumerate(data):
            self.formSuratMasuk.tblSuratMasuk.insertRow(i)
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 0, QTableWidgetItem(str(baris["id_surat_masuk"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 2, QTableWidgetItem(str(baris["tanggal_masuk"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 3, QTableWidgetItem(str(baris["no_surat"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 4, QTableWidgetItem(str(baris["tanggal_surat"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 5, QTableWidgetItem(str(baris["uraian"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 6, QTableWidgetItem(str(baris["lanjut_ke"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 7, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formSuratMasuk.tblSuratMasuk.setItem(i, 8, QTableWidgetItem(str(baris["tanda_terima"])))

    def laporanSuratMasuk(self):
        self.aksi.cetakSuratMasuk()

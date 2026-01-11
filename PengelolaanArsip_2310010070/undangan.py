# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from crud import crud_arsip

class form_Undangan(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Undangan")
        filenya = QFile('undangan.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formUndangan = muatfile.load(filenya,self)
        self.aksi = crud_arsip()
        self.formUndangan.BtnSimpan.clicked.connect(self.simpanUndangan)
        self.formUndangan.BtnUbah.clicked.connect(self.ubahUndangan)
        self.formUndangan.BtnHapus.clicked.connect(self.hapusUndangan)
        self.tampilDataUndangan()
        self.formUndangan.lineCari.textChanged.connect(self.cariDataUndangan)
        self.formUndangan.btnCetak.clicked.connect(self.laporanUndangan)

    def simpanUndangan(self):
        if not self.formUndangan.idUndanganLineEdit.text().strip():
            QMessageBox.information(None, "Informasi", "ID Undangan belum diisi")
            self.formUndangan.idUndanganLineEdit.setFocus()
        else:
            id_undangan = self.formUndangan.idUndanganLineEdit.text()
            id_admin = self.formUndangan.idAdminLineEdit.text()
            instansi = self.formUndangan.dinasInstansiLineEdit.text()
            tgl_masuk = self.formUndangan.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
            no_surat = self.formUndangan.noSuratLineEdit.text()
            tgl_surat = self.formUndangan.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
            uraian = self.formUndangan.uraianLineEdit.text()
            lanjut_ke = self.formUndangan.lanjutKeLineEdit.text()
            tanda_terima = self.formUndangan.tandaTerimaLineEdit.text()

            self.aksi.tambahUndangan(id_undangan, id_admin, instansi, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima)
            self.tampilDataUndangan()
            QMessageBox.information(None, "Informasi", "Data Undangan berhasil disimpan")

    def ubahUndangan(self):
        id_undangan = self.formUndangan.idUndanganLineEdit.text()
        id_admin = self.formUndangan.idAdminLineEdit.text()
        instansi = self.formUndangan.dinasInstansiLineEdit.text()
        tgl_masuk = self.formUndangan.tanggalMasukDateEdit.date().toString("yyyy-MM-dd")
        no_surat = self.formUndangan.noSuratLineEdit.text()
        tgl_surat = self.formUndangan.tanggalSuratDateEdit.date().toString("yyyy-MM-dd")
        uraian = self.formUndangan.uraianLineEdit.text()
        lanjut_ke = self.formUndangan.lanjutKeLineEdit.text()
        tanda_terima = self.formUndangan.tandaTerimaLineEdit.text()

        self.aksi.gantiUndangan(id_undangan, id_admin, instansi, tgl_masuk, no_surat, tgl_surat, uraian, lanjut_ke, tanda_terima)
        self.tampilDataUndangan()
        QMessageBox.information(None, "Informasi", "Data Undangan berhasil diubah")

    def hapusUndangan(self):
        pesan = QMessageBox.question(None, "Konfirmasi", "Yakin menghapus data undangan ini?",
                                     QMessageBox.Yes | QMessageBox.No)
        if pesan == QMessageBox.Yes:
            id_undangan = self.formUndangan.idUndanganLineEdit.text()
            self.aksi.hapusUndangan(id_undangan)
            self.tampilDataUndangan()
            QMessageBox.information(None, "Informasi", "Data Undangan berhasil dihapus")

    def tampilDataUndangan(self):
        self.formUndangan.tblUndangan.setRowCount(0)
        data = self.aksi.dataUndangan()
        for i, baris in enumerate(data):
            self.formUndangan.tblUndangan.insertRow(i)
            self.formUndangan.tblUndangan.setItem(i, 0, QTableWidgetItem(str(baris["id_undangan"])))
            self.formUndangan.tblUndangan.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formUndangan.tblUndangan.setItem(i, 2, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formUndangan.tblUndangan.setItem(i, 3, QTableWidgetItem(str(baris["tanggal_masuk"])))
            self.formUndangan.tblUndangan.setItem(i, 4, QTableWidgetItem(str(baris["no_surat"])))
            self.formUndangan.tblUndangan.setItem(i, 5, QTableWidgetItem(str(baris["tanggal_surat"])))
            self.formUndangan.tblUndangan.setItem(i, 6, QTableWidgetItem(str(baris["uraian"])))
            self.formUndangan.tblUndangan.setItem(i, 7, QTableWidgetItem(str(baris["lanjut_ke"])))
            self.formUndangan.tblUndangan.setItem(i, 8, QTableWidgetItem(str(baris["tanda_terima"])))

    def cariDataUndangan(self):
        varCari = self.formUndangan.lineCari.text()
        self.formUndangan.tblUndangan.setRowCount(0)
        data = self.aksi.filterUndangan(varCari)
        for i, baris in enumerate(data):
            self.formUndangan.tblUndangan.insertRow(i)
            self.formUndangan.tblUndangan.setItem(i, 0, QTableWidgetItem(str(baris["id_undangan"])))
            self.formUndangan.tblUndangan.setItem(i, 1, QTableWidgetItem(str(baris["id_admin"])))
            self.formUndangan.tblUndangan.setItem(i, 2, QTableWidgetItem(str(baris["dinas_instansi"])))
            self.formUndangan.tblUndangan.setItem(i, 3, QTableWidgetItem(str(baris["tanggal_masuk"])))
            self.formUndangan.tblUndangan.setItem(i, 4, QTableWidgetItem(str(baris["no_surat"])))
            self.formUndangan.tblUndangan.setItem(i, 5, QTableWidgetItem(str(baris["tanggal_surat"])))
            self.formUndangan.tblUndangan.setItem(i, 6, QTableWidgetItem(str(baris["uraian"])))
            self.formUndangan.tblUndangan.setItem(i, 7, QTableWidgetItem(str(baris["lanjut_ke"])))
            self.formUndangan.tblUndangan.setItem(i, 8, QTableWidgetItem(str(baris["tanda_terima"])))

    def laporanUndangan(self):
        self.aksi.cetakUndangan()

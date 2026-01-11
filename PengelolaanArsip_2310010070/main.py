# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from admin import form_Admin
from suratMasuk import form_SuratMasuk
from suratKeluar import form_SuratKeluar
from disposisi import form_Disposisi
from undangan import form_Undangan

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pengelolaan Arsip - Halaman Utama")
        filenya = QFile('main.ui')
        filenya.open(QFile.ReadOnly)
        muatfile = QUiLoader()
        self.formutama = muatfile.load(filenya,self)
        self.resize(self.formutama.size())
        self.setMenuBar(self.formutama.menuBar())

        self.formutama.actionData_Admin.triggered.connect(self.bukaAdmin)
        self.formutama.actionData_Surat_Masuk.triggered.connect(self.bukaSuratMasuk)
        self.formutama.actionData_Surat_Keluar.triggered.connect(self.bukaSuratKeluar)
        self.formutama.actionData_Disposisi.triggered.connect(self.bukaDisposisi)
        self.formutama.actionData_Undangan.triggered.connect(self.bukaUndangan)

    def bukaAdmin(self):
        self.formAdm = form_Admin()
        self.formAdm.show()

    def bukaSuratMasuk(self):
        self.formSurMas = form_SuratMasuk()
        self.formSurMas.show()

    def bukaSuratKeluar(self):
        self.formSurKel = form_SuratKeluar()
        self.formSurKel.show()

    def bukaDisposisi(self):
        self.formDis = form_Disposisi()
        self.formDis.show()

    def bukaUndangan(self):
        self.formUnd = form_Undangan()
        self.formUnd.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    jendela = MainWindow()
    jendela.show()
    sys.exit(app.exec())

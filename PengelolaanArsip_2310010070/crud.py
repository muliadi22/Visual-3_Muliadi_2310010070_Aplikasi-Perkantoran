# This Python file uses the following encoding: utf-8
import mysql.connector
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

class crud_arsip:
    def __init__(self):
        self.koneksi = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pengelolaanarsip_2310010070'
        )

    # ===== CRUD ADMIN =====
    def tambahAdmin(self, id, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("INSERT INTO admin (id_admin, username, password) VALUES (%s, %s, %s)",
                    (id, username, password))
        self.koneksi.commit()
        aksi.close()

    def gantiAdmin(self, id, username, password):
        aksi = self.koneksi.cursor()
        aksi.execute("UPDATE admin SET username=%s, password=%s WHERE id_admin=%s",
                    (username, password, id))
        self.koneksi.commit()
        aksi.close()

    def hapusAdmin(self, id):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM admin WHERE id_admin=%s", (id,))
        self.koneksi.commit()
        aksi.close()

    def dataAdmin(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("SELECT * FROM admin ORDER BY id_admin ASC")
        return aksi.fetchall()

    def filterAdmin(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        sql = "SELECT * FROM admin WHERE id_admin LIKE %s OR username LIKE %s OR password LIKE %s"
        val = (f"%{cari}%", f"%{cari}%", f"%{cari}%")
        aksi.execute(sql, val)
        return aksi.fetchall()

    def cetakAdmin(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM admin")
        data = aksi.fetchall()
        barisData = [["Id Admin", "Username", "Password"]] + list(data)
        fileLaporan = "Laporan Admin.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize=A4)
        isiData = Table(barisData, colWidths=[80, 80, 80])
        pdf.build([isiData])

    # ===== CRUD SURAT MASUK =====
    def tambahSuratMasuk(self, id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO surat_masuk (id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def gantiSuratMasuk(self, id_surat_masuk, id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """UPDATE surat_masuk SET id_admin=%s, tanggal_masuk=%s, no_surat=%s,
                    tanggal_surat=%s, uraian=%s, lanjut_ke=%s, dinas_instansi=%s, tanda_terima=%s WHERE id_surat_masuk=%s"""
        aksi.execute(sql, (id_admin, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, dinas_instansi, tanda_terima, id_surat_masuk))
        self.koneksi.commit()
        aksi.close()

    def hapusSuratMasuk(self, id_surat_masuk):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM surat_masuk WHERE id_surat_masuk=%s", (id_surat_masuk,))
        self.koneksi.commit()
        aksi.close()

    def dataSuratMasuk(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("SELECT * FROM surat_masuk ORDER BY id_surat_masuk ASC")
        return aksi.fetchall()

    def filterSuratMasuk(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT * FROM surat_masuk
            WHERE id_surat_masuk LIKE %s OR id_admin LIKE %s OR tanggal_masuk LIKE %s
            OR no_surat LIKE %s OR tanggal_surat LIKE %s OR uraian LIKE %s
            OR lanjut_ke LIKE %s OR dinas_instansi LIKE %s OR tanda_terima LIKE %s
            """,
            ([f"%{cari}%"] * 9)
        )
        return aksi.fetchall()

    def cetakSuratMasuk(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM surat_masuk")
        data = aksi.fetchall()
        barisData = [["Id SM", "Id Adm", "Tgl Masuk", "No Surat", "Tgl Surat", "Uraian", "Lanjut", "Instansi", "Terima"]] + list(data)
        fileLaporan = "Laporan Surat Masuk.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize=A4)
        isiData = Table(barisData, colWidths=[40, 45, 70, 70, 70, 70, 80, 70, 80])
        pdf.build([isiData])

    # ===== CRUD SURAT KELUAR =====
    def tambahSuratKeluar(self, id_surat_keluar, id_admin, tanggal_keluar, dinas_instansi, no_surat, tanggal_surat, uraian):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO surat_keluar
                    (id_surat_keluar, id_admin, tanggal_keluar, dinas_instansi, no_surat, tanggal_surat, uraian)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_surat_keluar, id_admin, tanggal_keluar, dinas_instansi, no_surat, tanggal_surat, uraian))
        self.koneksi.commit()
        aksi.close()

    def gantiSuratKeluar(self, id_surat_keluar, id_admin, tanggal_keluar, dinas_instansi, no_surat, tanggal_surat, uraian):
        aksi = self.koneksi.cursor()
        sql = """UPDATE surat_keluar SET id_admin=%s, tanggal_keluar=%s, dinas_instansi=%s,
                    no_surat=%s, tanggal_surat=%s, uraian=%s WHERE id_surat_keluar=%s"""
        aksi.execute(sql, (id_admin, tanggal_keluar, dinas_instansi, no_surat, tanggal_surat, uraian, id_surat_keluar))
        self.koneksi.commit()
        aksi.close()

    def hapusSuratKeluar(self, id_surat_keluar):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM surat_keluar WHERE id_surat_keluar=%s", (id_surat_keluar,))
        self.koneksi.commit()
        aksi.close()

    def dataSuratKeluar(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("SELECT * FROM surat_keluar ORDER BY id_surat_keluar ASC")
        return aksi.fetchall()

    def filterSuratKeluar(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT * FROM surat_keluar
            WHERE id_surat_keluar LIKE %s OR id_admin LIKE %s OR tanggal_keluar LIKE %s
            OR dinas_instansi LIKE %s OR no_surat LIKE %s OR tanggal_surat LIKE %s
            OR uraian LIKE %s
            """,
            ([f"%{cari}%"] * 7)
        )
        return aksi.fetchall()

    def cetakSuratKeluar(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM surat_keluar")
        data = aksi.fetchall()
        barisData = [["Id SK", "Id Adm", "Tgl Keluar", "Instansi", "No Surat", "Tgl Surat", "Uraian"]] + list(data)
        fileLaporan = "Laporan Surat Keluar.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize=A4)
        isiData = Table(barisData, colWidths=[50, 50, 80, 80, 60, 80, 200])
        pdf.build([isiData])

    # ===== CRUD DISPOSISI =====
    def tambahDisposisi(self, id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO disposisi (id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def gantiDisposisi(self, id_disposisi, id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """UPDATE disposisi SET id_admin=%s, dinas_instansi=%s, tanggal_masuk=%s, no_tanggal_surat=%s,
                    isi_disposisi=%s, uraian=%s, lanjut_ke=%s, tanda_terima=%s WHERE id_disposisi=%s"""
        aksi.execute(sql, (id_admin, dinas_instansi, tanggal_masuk, no_tanggal_surat, isi_disposisi, uraian, lanjut_ke, tanda_terima, id_disposisi))
        self.koneksi.commit()
        aksi.close()

    def hapusDisposisi(self, id_disposisi):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM disposisi WHERE id_disposisi=%s", (id_disposisi,))
        self.koneksi.commit()
        aksi.close()

    def dataDisposisi(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("SELECT * FROM disposisi ORDER BY id_disposisi ASC")
        return aksi.fetchall()

    def filterDisposisi(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT * FROM disposisi
            WHERE id_disposisi LIKE %s OR id_admin LIKE %s OR dinas_instansi LIKE %s
            OR tanggal_masuk LIKE %s OR no_tanggal_surat LIKE %s OR isi_disposisi LIKE %s
            OR uraian LIKE %s OR lanjut_ke LIKE %s OR tanda_terima LIKE %s
            """,
            ([f"%{cari}%"] * 9)
        )
        return aksi.fetchall()

    def cetakDisposisi(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM disposisi")
        data = aksi.fetchall()
        barisData = [["ID Disp", "ID Adm", "Instansi", "Tgl Masuk", "No Tgl Surat", "Isi", "Uraian", "Lanjut", "Terima"]] + list(data)
        fileLaporan = "Laporan Disposisi.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize=A4)
        isiData = Table(barisData, colWidths=[45, 45, 70, 70, 80, 60, 60, 60, 80])
        pdf.build([isiData])

    # ===== CRUD UNDANGAN =====
    def tambahUndangan(self, id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """INSERT INTO undangan
                    (id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima)
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        aksi.execute(sql, (id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima))
        self.koneksi.commit()
        aksi.close()

    def gantiUndangan(self, id_undangan, id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima):
        aksi = self.koneksi.cursor()
        sql = """UPDATE undangan SET id_admin=%s, dinas_instansi=%s, tanggal_masuk=%s,
                    no_surat=%s, tanggal_surat=%s, uraian=%s, lanjut_ke=%s, tanda_terima=%s WHERE id_undangan=%s"""
        aksi.execute(sql, (id_admin, dinas_instansi, tanggal_masuk, no_surat, tanggal_surat, uraian, lanjut_ke, tanda_terima, id_undangan))
        self.koneksi.commit()
        aksi.close()

    def hapusUndangan(self, id_undangan):
        aksi = self.koneksi.cursor()
        aksi.execute("DELETE FROM undangan WHERE id_undangan=%s", (id_undangan,))
        self.koneksi.commit()
        aksi.close()

    def dataUndangan(self):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("SELECT * FROM undangan ORDER BY id_undangan ASC")
        return aksi.fetchall()

    def filterUndangan(self, cari):
        aksi = self.koneksi.cursor(dictionary=True)
        aksi.execute("""
            SELECT * FROM undangan
            WHERE id_undangan LIKE %s OR id_admin LIKE %s OR dinas_instansi LIKE %s
            OR tanggal_masuk LIKE %s OR no_surat LIKE %s OR tanggal_surat LIKE %s
            OR uraian LIKE %s OR lanjut_ke LIKE %s OR tanda_terima LIKE %s
            """,
            ([f"%{cari}%"] * 9)
        )
        return aksi.fetchall()

    def cetakUndangan(self):
        aksi = self.koneksi.cursor()
        aksi.execute("SELECT * FROM undangan")
        data = aksi.fetchall()
        barisData = [["ID Und", "ID Adm", "Instansi", "Tgl Masuk", "No Surat", "Tgl Surat", "Uraian", "Lanjut", "Terima"]] + list(data)
        fileLaporan = "Laporan Undangan.pdf"
        pdf = SimpleDocTemplate(fileLaporan, pagesize=A4)
        isiData = Table(barisData, colWidths=[45, 45, 60, 70, 60, 70, 60, 60, 80])
        pdf.build([isiData])

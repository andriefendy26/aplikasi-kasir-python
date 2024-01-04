from PyQt5.QtWidgets import QDialog, QApplication, QDesktopWidget, QStackedWidget, QWidget, QMessageBox
from PyQt5 import QtWidgets, uic, QtCore
#import konekDB
import mysql.connector
import sys

class login(QDialog):
	def __init__(self):
		super(login, self).__init__()
		uic.loadUi("Login.ui", self)
		self.masuk.clicked.connect(self.loginfungsion)
	
	def loginfungsion(self):
		username = self.emailfield.text()
		password = self.passwordfield.text()
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
		curr = conn.cursor()
		sql = "SELECT * FROM auth where username = '" + username + "' and pass = '" + password + "'"
		curr.execute(sql)
		user = curr.fetchone()
		if user is not None:
			self.masukkasir()
			QMessageBox.information(self, 'Alert', 'login berhasil')
		else:
			self.error.setText("masukkan akun yang benar")

	def masukkasir(self):
		self.openkasir = Pilihan()
		self.openkasir.show()
		self.close()

class Pilihan(QDialog):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		uic.loadUi("Pilihan.ui", self)
		self.tombol()
		
	def tombol(self):
		self.Menu.clicked.connect(self.Dftrmenu)
		self.Lprn.clicked.connect(self.Lapar)
		self.logout.clicked.connect(self.Keluar)
		
	def Dftrmenu(self):
		self.openkasir = DftrMenu()
		self.openkasir.show()
		self.close()
		 
	def Lapar(self):
		self.openkasir = Laporan()
		self.openkasir.show()
		self.close()
		
	def Keluar(self):
		self.openkasir = login()
		self.openkasir.show()
		self.close()

class DftrMenu(QDialog):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		uic.loadUi("DaftarMenu.ui", self)
		self.tombol()
		self.tabelWidtg()
		self.loaddata()
		self.activeText(False)
		
	def tombol(self):
		self.keluar.clicked.connect(self.kembali)
		self.batal.clicked.connect(self.batals)
		self.edit.clicked.connect(self.edittext)
		self.tableWidget.clicked.connect(self.getitem)
		self.hapus.clicked.connect(self.hapusData)
		self.simpan.clicked.connect(self.simpandata)
	
	def tabelWidtg(self):   #untuk mengatur ukuran kolom pada tabel
		#Tabel Daftar Menu
		self.tableWidget.setColumnWidth(0,100)
		self.tableWidget.setColumnWidth(1,150)
		self.tableWidget.setColumnWidth(2,180)
		self.tableWidget.setColumnWidth(3,165)
		

	def loaddata(self): #untuk menampilkan data pada tabel
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')	
		curr = conn.cursor()
		querry = "SELECT * FROM tbbarang ORDER BY total DESC"
		curr.execute(querry)
		result = curr.fetchall()
		print(result)
		row = 0
		self.tableWidget.setRowCount(len(result))
		for item in result:
			self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(item[0]))
			self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(item[1]))
			self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(item[2]))
			self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(item[3])))
			row += 1


	def clearform(self):
		self.textIdMenu.setFocus()
		self.textIdMenu.setText('')
		self.cbKategori.setCurrentText('')
		self.textMenu.setText('')
		self.textHarga.setText('')
		
	def activeText(self,bool):
		self.textIdMenu.setEnabled(bool)
		self.cbKategori.setEnabled(bool)
		self.textMenu.setEnabled(bool)
		self.textHarga.setEnabled(bool)
		
	def getitem(self):
		row = self.tableWidget.currentRow()
		idMenu = self.tableWidget.item(row,0).text()
		tipeMenu = self.tableWidget.item(row,1).text()
		namaMenu = self.tableWidget.item(row,2).text()
		hargaa = self.tableWidget.item(row,3).text()
		self.textIdMenu.setText(idMenu)
		self.cbKategori.setCurrentText(tipeMenu)
		self.textMenu.setText(namaMenu)
		self.textHarga.setText(hargaa)
		
	def edittext(self):
		cb = self.edit.text()
		print(cb)
		if cb == 'edit tabel':
			self.activeText(True)
			self.clearform()
			self.edit.setText('simpan')
		elif cb == 'simpan':
			conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
			curr = conn.cursor()
			self.activeText(True)
			idMenu = self.textIdMenu.text()
			tipeMenu = self.cbKategori.currentText()
			namaMenu = self.textMenu.text()
			hargaa = self.textHarga.text()
			query = f"UPDATE tbbarang SET kategori = '{tipeMenu}', namaMenu = '{namaMenu}', harga = '{hargaa}' WHERE idMenu = '{idMenu}'"
			curr.execute(query)
			print("Edit berhasil")
			conn.commit()
			curr.close()
			conn.close()
			self.loaddata()
			self.activeText(False)
			self.clearform()
			self.edit.setText('edit tabel')
		
	def hapusData(self):
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
		curr = conn.cursor()
		idMenu = self.textIdMenu.text()
		query = f"DELETE FROM tbbarang Where idMenu = '{idMenu}'"
		curr.execute(query)
		print("Hapus berhasil")
		conn.commit()
		curr.close()
		conn.close()
		self.loaddata()
			
	def batals(self):
		cb = self.simpan.text()
		ed = self.edit.text()
		if cb == 'simpan':
			self.simpan.setText('baru')
			self.clearform()
			self.activeText(False)
		elif ed == 'simpan':	
			self.edit.setText('edit table')
			self.clearform()
			self.activeText(False)
				
	def simpandata(self):
		cb = self.simpan.text()
		print(cb)
		if cb == 'baru':
			self.activeText(True)
			self.clearform()
			self.simpan.setText('simpan')

		elif cb == 'simpan':
			conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
			curr = conn.cursor()
			self.simpan.setText('baru')
			idMenu = self.textIdMenu.text()
			tipeMenu = self.cbKategori.currentText()
			namaMenu = self.textMenu.text()
			hargaa = self.textHarga.text()
			query = f"INSERT INTO tbbarang (idMenu, kategori, namaMenu, harga) VALUES ('{idMenu}', '{tipeMenu}', '{namaMenu}', '{hargaa}')"
			curr.execute(query)
			print("Simpan berhasil")
			conn.commit()
			curr.close()
			conn.close()
			self.loaddata()
			self.activeText(False)
			self.clearform()
		
	def kembali(self):
		self.openkasir = Pilihan()
		self.openkasir.show()
		self.close()
		

class Laporan(QDialog):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		uic.loadUi("Data.ui", self)
		self.tombol()
		self.loaddata2()
		self.tabelWidtg()
		self.tot()

	def tabelWidtg(self):
		#Tabel Data Pendapatan
		self.tableWidget_2.setColumnWidth(0,330)
		self.tableWidget_2.setColumnWidth(1,250)
		self.tableWidget_2.setColumnWidth(2,280)
		
	def tombol(self):
		self.keluar.clicked.connect(self.kembali)
		
	def loaddata2(self):
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')	
		curr = conn.cursor()
		querry = "SELECT * FROM laporan"
		curr.execute(querry)
		result = curr.fetchall()
		print(result)
		row = 0
		self.tableWidget_2.setRowCount(len(result))
		for item in result:
			self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(item[1]))
			self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(str(item[2])))
			self.tableWidget_2.setItem(row,2,QtWidgets.QTableWidgetItem(str(item[3])))
			row += 1
			
	def tot(self):
		tota = 0
		conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='warungme')    
		curr = conn.cursor()
		query = "SELECT total FROM laporan"
		curr.execute(query)
		rows = curr.fetchall()  # Mengambil semua baris hasil query
		conn.commit()
		for row in rows:
			total = float(row[0])
			tota += total
		conn.close()
		self.Total.setStyleSheet("font-size: 18px")
		self.Total.setText("RP.{:.0f}".format(tota))
		
	def kembali(self):
		self.openkasir = Pilihan()
		self.openkasir.show()
		self.close()
		

if __name__ == "__main__":
	MainApp = QtWidgets.QApplication(sys.argv)
	widget = QWidget()
	App = login()
	App.show()
	sys.exit(MainApp.exec_())
